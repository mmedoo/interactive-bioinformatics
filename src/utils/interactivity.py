from typing import Callable
from manim import *
from manim.typing import Point3D

def onObjectHover(object: Mobject):
	"""
	Handles the hover effect on a given Mobject.

	When the specified Mobject is hovered over, this function modifies its
	appearance by setting its stroke color to white and increasing the stroke
	width to 5.

	Args:
		object (Mobject): The Mobject instance to apply the hover effect to.
	"""
	object.set_stroke(WHITE, width=5)
	# object.set_color(RED)


def onObjectUnhover(object: Mobject):
	"""
	Handles the event when the mouse pointer stops hovering over a Mobject.

	This function modifies the appearance of the given Mobject by resetting its stroke color 
	to white and setting the stroke width to 0. This can be used to visually indicate that 
	the object is no longer being hovered over.

	Args:
		object (Mobject): The Mobject instance that the unhover event applies to.
	"""
	object.set_stroke(WHITE, width=0)
	# object.set_color(WHITE)


def isPositionWithInObject(pos: Point3D, obj: Mobject) -> bool:
	bounding_box = obj.get_bounding_box()
	x_min, y_min = bounding_box[0][0], bounding_box[0][1]
	x_max, y_max = bounding_box[2][0], bounding_box[2][1]

	return x_min <= pos[0] <= x_max and y_min <= pos[1] <= y_max


def watch_mouse_motion(mousePosition: Point3D, hoverables: list[Mobject]):
	"""
	Monitors the mouse position and triggers hover or unhover events for a list of objects.

	Args:
		mousePosition (Point3D): The current position of the mouse in 3D space.
		hoverables (list[Mobject]): A list of objects to check for hover interactions.

	Behavior:
		- If the mouse position is within an object in the `hoverables` list, the `onObjectHover` 
		  function is called for that object.
		- If the mouse position is not within an object, the `onObjectUnhover` function is called 
		  for that object.

	Note:
		This function assumes the existence of `isPositionWithInObject`, `onObjectHover`, and 
		`onObjectUnhover` functions, which handle the logic for detecting hover states and 
		responding to them.
	"""
	for obj in hoverables:
		if isPositionWithInObject(mousePosition, obj):
			onObjectHover(obj)
		else:
			onObjectUnhover(obj)


def makeClickable(self, obj: Mobject, handler: Callable):
	"""
	This method allows you to make a graphical object (Mobject) interactive by 
	registering it as a clickable button. When the object is clicked, the 
	associated handler function will be executed.


	Registers a Mobject as clickable and associates it with a handler function.

	This method adds the given Mobject to the list of clickable buttons and 
	maps it to a corresponding handler function that will be executed when 
	the Mobject is clicked.

	Args:
		obj (Mobject): The graphical object to be made clickable.
		handler (Callable[[Mobject], None]): A function that takes the Mobject 
			as an argument and defines the action to be performed when the 
			object is clicked.

	Returns:
		None
	"""
	self.buttons.append(obj)
	self.onClickHandlers[obj] = handler


def makeButtonMobs(buttonLabel: str) -> VGroup:
	label = Text(buttonLabel, font_size=42, color=WHITE)
	box = Rectangle(
		width=label.width + 0.5,  # Add padding to the width
		height=label.height + 0.3,  # Add padding to the height
	).set_stroke(WHITE, width=0).move_to(label.get_center())
	return VGroup(label, box)

def makeOptions(buttonLabels: list[str]) -> list[tuple[Text, Rectangle]]:
	"""
	Creates a list of button objects, each consisting of a text label and a surrounding rectangle.
	Args:
		buttonLabels (list[str]): A list of strings representing the labels for the buttons.
	Returns:
		list[tuple[Text, Rectangle]]: A list of tuples, where each tuple contains a `Text` object 
		for the button label and a `Rectangle` object representing the button's bounding box.
	"""
	objects = []

	n = len(buttonLabels)
	for j in range(n):
		buttonLabel = buttonLabels[j]

		pos = j * (n / (n-1)) - (n / 2)

		[label, box] = makeButtonMobs(buttonLabel).move_to(ORIGIN + pos * RIGHT * 2.5)

		objects.append([label, box])

	return objects


def update_input(self):
	"""
	Updates the input display by removing the previous temporary input object,
	creating a new text object based on the current input, and adding it to the scene.

	This method temporarily disables input acceptance while updating the display
	and re-enables it after the update is complete.

	Behavior:
		- Removes the existing temporary input object if it exists.
		- Joins the current input list into a single string with double spaces.
		- Creates a new text object and positions it next to the input position.
		- Adds the new text object to the scene.
		- Re-enables input acceptance.
	"""
	self.accept_input = False

	if self.temp_input_mobject:
		self.remove(self.temp_input_mobject)

	input_text = "  ".join(self.current_input)
	self.temp_input_mobject = Text(input_text).next_to(self.input_position, RIGHT, buff=0)
	# self.play(Write(self.input_object), run_time=run_time)
	self.add(self.temp_input_mobject)
	self.accept_input = True


def take_input(self, label: str, position: Point3D):
	"""
	Displays a text label at a specified position and prepares for user input.

	Args:
		label (str): The text to display as the label.
		pos (Point3D): The 3D position where the label should be placed.

	Side Effects:
		- Creates a text label and adds it to the scene.
		- Updates the input position to the right of the label.
		- Sets the `accept_input` flag to True, indicating readiness for input.
	"""
	mlabel = Text(label, font_size=48).move_to(position)
	self.labels_mobjects.append(mlabel)
	self.input_position = mlabel.get_right() + RIGHT * 0.25
	self.add((mlabel))
	self.accept_input = True
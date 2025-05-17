from manim import *

def onObjectHover(object):
	object.set_stroke(WHITE, width=5)
	# object.set_color(RED)

def onObjectUnhover(object):
	object.set_stroke(WHITE, width=0)
	# object.set_color(WHITE)

def isPositionWithInObject(pos, obj):
	bounding_box = obj.get_bounding_box()
	x_min, y_min = bounding_box[0][0], bounding_box[0][1]
	x_max, y_max = bounding_box[2][0], bounding_box[2][1]

	return x_min <= pos[0] <= x_max and y_min <= pos[1] <= y_max

def watch_mouse_motion(mousePosition, hoverables):
	for obj in hoverables:
		if isPositionWithInObject(mousePosition, obj):
			onObjectHover(obj)
		else:
			onObjectUnhover(obj)

def makeClickable(self, obj, handler):
	self.buttons.append(obj)
	self.onClickHandlers[obj] = handler

def on_mouse_press(self, mousePressPosition):
	for obj in self.buttons:
		if isPositionWithInObject(mousePressPosition, obj) and obj in self.onClickHandlers:
			self.onClickHandlers[obj](obj)

def on_mouse_motion(self, mousePosition):
	# self.cursor_obj.move_to(mousePosition)
	watch_mouse_motion(mousePosition, self.buttons)

def makeButtons(buttonLabels):

	objects = []

	n = len(buttonLabels)
	for j in range(n):
		buttonLabel = buttonLabels[j]

		pos = j * (n / (n-1)) - (n / 2)

		label = Text(buttonLabel, font_size=42, color=WHITE).move_to(ORIGIN).move_to(pos * RIGHT * 2.5)
		
		box = Rectangle(
			width=label.width + 0.5,  # Add padding to the width
			height=label.height + 0.3,  # Add padding to the height
		).set_stroke(WHITE, width=0).move_to(label.get_center())
		
		objects.append([label, box])

	return objects
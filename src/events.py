from manim.typing import Point3D
from .utils.interactivity import isPositionWithInObject, watch_mouse_motion
from pyglet.window import key as keys
from .utils.public import check_if_char

def handleMousePress(self, point: Point3D, button, modifiers):
	for obj in self.buttons:
		if isPositionWithInObject(point, obj) and obj in self.onClickHandlers:
			self.onClickHandlers[obj](obj)

def handleMouseMotion(self, point: Point3D, d_point):
	# self.cursor_obj.move_to(mousePosition)
	watch_mouse_motion(point, self.buttons)

def handleKeyPress(self, symbol, modifiers):
	if not self.accept_input:
		return
	
	if self.error_message is not None:
		self.remove(self.error_message)
	
	if symbol == keys.BACKSPACE:
		if len(self.current_input) > 0:
			self.current_input.pop()
			self.update_input()
		return

	if symbol in (keys.ENTER, keys.NUM_ENTER):
		if (len(self.current_input) == 0):
			self.displayError("Empty input")
			return

		valid = self.submitChecker()
		if not valid:
			return
		self.inputs_mobjects.append(self.temp_input_mobject.copy())
		self.input_history.append(self.current_input)
		self.current_input = []
		self.remove(self.temp_input_mobject)
		self.accept_input = False
		self.play_next_stage()
		return
	
	str = check_if_char(symbol)
	if not str:
		self.displayError("Invalid character")
		return
		
	valid = self.inputChecker(str)
	if not valid:
		return

	if (len(self.current_input) + 1) > self.max_input_len:
		self.displayError("Max length reached")
		return

	if str in self.current_input:
		self.displayError("Duplicate characters are not allowed")
		return

	self.current_input.append(str)
	self.update_input()

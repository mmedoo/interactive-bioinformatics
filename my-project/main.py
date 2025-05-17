from manim import *
from manim.opengl import *
from interactivity_utils import *
from pyglet.window import key as keys
from linear.linear import runLinear
from circular import runCircular

# constants
run_time = 0.5

def check_if_char(symbol):
	if symbol in (keys.NUM_0, keys.NUM_1, keys.NUM_2, keys.NUM_3, keys.NUM_4, keys.NUM_5, keys.NUM_6, keys.NUM_7, keys.NUM_8, keys.NUM_9):
		return str(symbol - keys.NUM_0)
	if chr(symbol).isalnum():
		return str(chr(symbol).upper())
	return False

class Run(Scene):
	error_message = None

	inputs = []
	labels_object = []
	inputs_object = []

	input_pos = None
	accept_input = False
	temp_input_object = None
	input_array = []
	max_input_len = 10
	i = 1
	
	cursor_obj = Circle(radius=0.1, color=WHITE).set_fill(WHITE, opacity=0.75)

	buttons = []
	
	onClickHandlers = {}
	onHoverHandlers = {}
	
	def displayError(self, text):
		self.error_message = Text(text, color=RED, font_size=48).to_edge(DOWN, buff=1.5).shift(DOWN * 0.5)
		self.add(self.error_message)

	def update_text(self):
		self.accept_input = False

		if self.temp_input_object:
			self.remove(self.temp_input_object)

		input_text = "  ".join(self.input_array)
		self.temp_input_object = Text(input_text).next_to(self.input_pos, RIGHT, buff=0)
		# self.play(Write(self.input_object), run_time=run_time)
		self.add(self.temp_input_object)
		self.accept_input = True

	def take_input(self, label, pos):
		label = Text(label, font_size=48).move_to(pos)
		self.labels_object.append(label)
		self.input_pos = label.get_right() + RIGHT * 0.25
		self.add((label))
		self.accept_input = True

	def on_mouse_press(self, mousePressPosition, button, mod):
		on_mouse_press(self, mousePressPosition)
		
	def on_mouse_motion(self, mousePosition, mod):
		on_mouse_motion(self, mousePosition)

	def makeClickable(self, obj, handler):
		makeClickable(self, obj, handler)

	def construct(self):
		# self.add(self.cursor_obj)
		self.play_next_stage()
		self.interactive_embed()

	def inputChecker(self):
		return True

	def stage_1(self):
		self.take_input("Initial Sequence:", 3*UP + 4*LEFT)
		
	def stage_2(self):
		self.add(self.inputs_object[0])
		self.max_input_len = len(self.inputs[0])
		def inputChecker():
			fseq = self.inputs[0]
			seq = self.input_array
			for char in seq:
				if char not in fseq:
					self.displayError("Both Sequences should have same characters")
					return False
			return True
		self.inputChecker = inputChecker
		self.take_input("Target Sequence:", 2*UP + 4*LEFT)
	
	def stage_3(self):
		self.play(
			*[FadeOut(label) for label in self.labels_object],
			self.inputs_object[0].animate.to_edge(LEFT + UP),
			self.inputs_object[1].animate.to_edge(RIGHT + UP),
			run_time=run_time
		)

		buttons = makeButtons(["Linear", "Circular"])

		[
			[_, linearBox],
			[_, circularBox]
		] = buttons

	
		self.play(*[ Write(label) for label, _ in buttons])
		self.add(*[box for _, box in buttons])

		def removeOptions():
			self.buttons = []
			self.remove(
				*[
					label
					for label, _ in buttons
				],
				*[
					box
					for _, box in buttons
				]
			)

		self.makeClickable(linearBox, lambda x: (
			removeOptions(),
			runLinear(self, self.inputs[0], self.inputs[1])
		))
		self.makeClickable(circularBox, lambda x: (
			removeOptions(),
			runCircular(self, self.inputs[0], self.inputs[1])
		))

	def play_next_stage(self):
		getattr(self, f"stage_{self.i}")()
		self.i += 1

	def on_key_press(self, symbol, mod):
		if not self.accept_input:
			return
		
		if self.error_message:
			self.remove(self.error_message)
		
		if symbol == keys.BACKSPACE:
			if len(self.input_array) > 0:
				self.input_array.pop()
				self.update_text()
			return

		if symbol in (keys.ENTER, keys.NUM_ENTER):
			if (len(self.input_array) == 0):
				self.displayError("Empty input")
				return
						
			valid = self.inputChecker()
			if not valid:
				return
			self.inputs_object.append(self.temp_input_object.copy())
			self.inputs.append(self.input_array)
			self.input_array = []
			self.remove(self.temp_input_object)
			self.accept_input = False
			self.play_next_stage()
			return
		
		str = check_if_char(symbol)
		if not str:
			self.displayError("Invalid character")
			return
			
		if (len(self.input_array) + 1) > self.max_input_len:
			self.displayError("Max length reached")
			return

		if str in self.input_array:
			self.displayError("Duplicate characters are not allowed")
			return
					
		self.input_array.append(str)
		self.update_text()

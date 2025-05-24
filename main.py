from manim import *
from manim.opengl import *
from manim.typing import Point3D
from typing import Callable, Any
from src.events import *
from src.utils.interactivity import *
from src.stages import stages

class Run(Scene):
	error_message: Text = Text("")
	submitChecker: Callable[[], bool] = lambda x = None: True
	inputChecker: Callable[[Any, str], bool] = lambda x, y = None: True
	input_position: Point3D
	input_history: list[list[str]] = []
	accept_input: bool = False
	current_input: list[str] = []
	labels_mobjects: list[Text] = []
	inputs_mobjects: list[Text] = []
	temp_input_mobject: Text = Text("")
	message_to_user: Text = Text("")

	max_input_len: int = 10
	current_stage: int = 0
	
	cursor_obj: Circle = Circle(radius=0.1, color=WHITE).set_fill(WHITE, opacity=0.75)
	buttons: list[Mobject] = []
	onClickHandlers: dict[Mobject, Callable] = {}
	onHoverHandlers: dict[Mobject, Callable] = {}
	
	update_input = update_input
	take_input = take_input
	
	on_mouse_press = handleMousePress
	on_mouse_motion = handleMouseMotion
	on_key_press = handleKeyPress
	makeClickable = makeClickable
	
	def construct(self):
		# self.add(self.cursor_obj)
		self.play_next_stage()
		self.interactive_embed()
	
	def displayMessage(self, text: str):
		self.message_to_user = Text(text, color=WHITE, font_size=48).to_edge(DOWN, buff=1.5).shift(DOWN * 0.5)
		self.add(self.message_to_user)
		
	def removeMessage(self):
		self.remove(self.message_to_user)
	
	def displayError(self, text):
		self.error_message = Text(text, color=RED, font_size=40).to_edge(DOWN, buff=1.5).shift(DOWN * 0.5)
		self.add(self.error_message)

	def removeError(self):
		self.remove(self.error_message)

	def play_next_stage(self):
		stages[self.current_stage](self)
		self.current_stage += 1
	
	def resetAll(self):
		self.clear()
		self.buttons = []
		self.current_stage = 0
		self.input_history = []
		self.current_input = []
		self.submitChecker = lambda x = None: True
		self.inputChecker = lambda x, y = None: True
		self.labels_mobjects = []
		self.inputs_mobjects = []
		self.onClickHandlers = {}
		self.onHoverHandlers = {}
		self.max_input_len = 10
		self.play_next_stage()

	def resetAndKeepSeqs(self):
		self.buttons = []
		self.clear()
		self.labels_mobjects = []
		self.add(
			self.inputs_mobjects[0],
			self.inputs_mobjects[1]
		)
		self.current_stage = 2
		self.play_next_stage()
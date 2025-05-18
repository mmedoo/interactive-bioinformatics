from manim import *
from .circular import runCircular
from .utils.interactivity import makeButtons
from .linear.entry import runLinear

run_time = 0.5

def stage_1(self):
	self.take_input("Initial Sequence:", 3*UP + 4*LEFT)

def stage_2(self):
	self.add(self.inputs_mobjects[0])
	self.max_input_len = len(self.input_history[0])
	def inputChecker():
		fseq = self.input_history[0]
		seq = self.current_input
		for char in seq:
			if char not in fseq:
				self.displayError("Both Sequences should have same characters")
				return False
		return True
	self.inputChecker = inputChecker
	self.take_input("Target Sequence:", 2*UP + 4*LEFT)

def stage_3(self):
	self.play(
		*[FadeOut(label) for label in self.labels_mobjects],
		self.inputs_mobjects[0].animate.to_edge(LEFT + UP),
		self.inputs_mobjects[1].animate.to_edge(RIGHT + UP),
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
		runLinear(self, self.input_history[0], self.input_history[1])
	))
	self.makeClickable(circularBox, lambda x: (
		removeOptions(),
		runCircular(self, self.input_history[0], self.input_history[1])
	))

stages = [
	stage_1,
	stage_2,
	stage_3
]
from manim import *
from .circular import runCircular
from .utils.interactivity import makeOptions
from .linear.entry import runLinear
from .utils.interactivity import makeButtonMobs
from .config import run_time

def stage_1(self):
	def inputChecker(incoming):
		if len(self.current_input) == 0:
			return True

		seq = self.current_input

		is_prev_digit = seq[0].isdigit()
		is_prev_alpha = seq[0].isalpha()

		if (is_prev_digit and not incoming.isdigit()) or (is_prev_alpha and not incoming.isalpha()):
			self.displayError("Input must be all digits or all letters")
			return False

		return True
		
	self.inputChecker = inputChecker

	self.take_input("Initial Sequence:", 3*UP + 4*LEFT)

def stage_2(self):
	self.add(self.inputs_mobjects[0])
	self.max_input_len = len(self.input_history[0])
	
	def submitChecker():
		fseq = self.input_history[0]
		seq = self.current_input
		if len(seq) != len(fseq):
			self.displayError("Both Sequences should have the same length")
			return False
		return True
	self.submitChecker = submitChecker

	def inputChecker(str):
		fseq = self.input_history[0]
		if str not in fseq:
			self.displayError("Both Sequences should have the same characters")
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

	self.remove(*self.labels_mobjects)

	[label, box] = makeButtonMobs("Reset").next_to(self.inputs_mobjects[0], DOWN).scale(0.75).to_edge(LEFT, buff=0.25)
	self.makeClickable(box, lambda x: self.resetAll())
	self.add(box, label)

	[label, box] = makeButtonMobs("Back").next_to(box, DOWN).scale(0.75).to_edge(LEFT, buff=0.25)
	self.makeClickable(box, lambda x: self.resetAndKeepSeqs())
	self.add(box, label)

	buttons = makeOptions(["Linear", "Circular"])

	[
		[_, linearBox],
		[_, circularBox]
	] = buttons


	self.play(*[ Write(label) for label, _ in buttons], run_time=run_time)
	self.add(*[box for _, box in buttons])

	def removeOptions():
		self.buttons.remove(linearBox)
		self.buttons.remove(circularBox)
		self.remove(
			*[label for label, _ in buttons],
			*[box for _, box in buttons]
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
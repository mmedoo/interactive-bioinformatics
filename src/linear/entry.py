from manim import *
from manim.opengl import *
from ..utils.interactivity import *
from .greedy import runGreedy
from .breakpoint import runBps

def runLinear(self, init, target):

	buttons = makeButtons(["Greedy", "Breakpoints"])

	[
		[_, greedyBox],
		[_, bpBox]
	] = buttons

	def removeButtons():
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

	self.makeClickable(greedyBox, lambda x: (
		removeButtons(),
		runGreedy(self, init, target)
	))

	self.makeClickable(bpBox, lambda x: (
		removeButtons(),
		runBps(self, init, target)
	))
	
	self.play(
		*[
			anim
			for label, box in buttons
			for anim in (Write(label), Create(box))
		]
	)
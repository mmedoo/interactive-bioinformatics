from manim import *
from manim.opengl import *
from ..utils.interactivity import *
from .greedy import runGreedy
from .breakpoint import runBps
from ..config import run_time

def runLinear(self, init, target):

	buttons = makeOptions(["Greedy", "Breakpoints"])

	[
		[_, greedyBox],
		[_, bpBox]
	] = buttons

	def removeButtons():
		self.buttons.remove(greedyBox)
		self.buttons.remove(bpBox)
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
		],
		run_time=run_time
	)
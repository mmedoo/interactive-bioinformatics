from circular import runCircular
from manim import Scene

class Run(Scene):
	def construct(self):
		runCircular(
			self,
			['4', '3', '2', '1'],
			['1', '2', '3', '4']
		)
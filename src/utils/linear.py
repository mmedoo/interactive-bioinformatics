from manim import *
from manim.typing import Point3D
from ..config import run_time

gap_size = 1.25

def checkMaxLength(self, all_steps: list[list[Mobject]]):
	if (len(all_steps) < 6):
		return
	self.play(
		*[
			mob.animate.shift(UP)
			for step_mobs in all_steps
			for mob in step_mobs
		],
		*[FadeOut(mob) for mob in all_steps[0]],
		run_time=run_time
	)
	all_steps.pop(0)

def getSeqObjects(seq: list, pos: Point3D) -> VGroup:
	step_text = VGroup()
	n = len(seq)
	for j in range(n):
		letter = Text(str(seq[j]), font_size=55)
		letter.move_to(pos + ( ( (n-2)/2 ) - j ) * LEFT * gap_size)
		step_text.add(letter)

	return step_text

def putMarkOnRange(seqObject: VGroup, start: int, end: int) -> tuple[Circle, Circle]:
	start_position = seqObject[start].get_center() + gap_size * LEFT/2
	sx_marker = Circle(radius=0.1).set_fill(RED,opacity=1).move_to(start_position + UP * 0.3)

	end_position = seqObject[end].get_center() + gap_size * RIGHT/2
	fx_marker = Circle(radius=0.1).set_fill(RED,opacity=1).move_to(end_position + UP * 0.3)
	
	return sx_marker, fx_marker

def putMarkOnBlockRight(mobject: Mobject) -> Circle:
	pos = mobject.get_center() + gap_size * RIGHT/2
	# marker = Text("X", font_size=24, color=RED).move_to(pos + UP * 0.3)
	marker = Circle(radius=0.125).set_fill(RED,opacity=0.7).move_to(pos + UP * 0.3)
	return marker

def getBreakPointsIndices(seq: list, target: list) -> list[int]:
	indices = []
	n = len(seq)
	for i in range(n-1):
		curr = target.index(seq[i])
		next = target.index(seq[i+1])
		if next - curr != 1:
			indices.append(i)
	return indices

def addStepToTheSide(self, step, order):
	origin = VGroup(*[mob.copy() for mob in step])
	newStep = origin.copy().scale(0.5).to_edge(RIGHT + DOWN * (order + 1),buff=0.5)
	self.add(origin)
	self.play(
		Transform(
			origin,
			newStep
		),
		run_time=run_time
	)


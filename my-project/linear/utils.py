from manim import *

gap_size = 1.5

def removeFirstAndShifStepUp(self, all_steps):
	self.play(
		*[
			letter.animate.shift(UP)
			for step_text in all_steps
			for letter in step_text
		],
		*[FadeOut(letter) for letter in all_steps[0]],
		run_time=0.4
	)

def checkMaxLength(self, all_steps):
	if (len(all_steps) < 6):
		return

	removeFirstAndShifStepUp(self, all_steps)
	all_steps.pop(0)

def getSeqObjects(seq, pos):
	step_text = []
	n = len(seq)
	for j in range(n):
		
		letter = Text(str(seq[j]), font_size=55)
		letter.move_to(pos + ( ( (n-2)/2 ) - j ) * LEFT * gap_size)
		step_text.append(letter)

	return step_text

def putMarkOnRange(seqObject, start, end):
	start_position = seqObject[start].get_center() + gap_size * LEFT/2
	sx_marker = Text("X", font_size=24, color=RED).move_to(start_position + UP * 0.3)

	end_position = seqObject[end].get_center() + gap_size * RIGHT/2
	fx_marker = Text("X", font_size=24, color=RED).move_to(end_position + UP * 0.3)
	
	return sx_marker, fx_marker

def putMarkOnBetweenIndices(seqObject, left, right):
	pos = seqObject[left].get_center() + gap_size * RIGHT/2
	# marker = Text("X", font_size=24, color=RED).move_to(pos + UP * 0.3)
	marker = Circle(radius=0.15).set_fill(RED,opacity=0.7).move_to(pos + UP * 0.3)
	return marker

def getBreakPointsIndices(seq, target):
	indices = []
	n = len(seq)
	for i in range(n-1):
		curr = target.index(seq[i])
		next = target.index(seq[i+1])
		if next - curr != 1:
			indices.append(i)
	return indices
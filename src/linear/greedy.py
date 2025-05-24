from manim import *
from ..utils.public import *
from ..utils.linear import *
from ..config import run_time

all_steps = []
operations_count = 0

def runGreedy(self, init: list, target: list):
	global operations_count
	init_current = init.copy()
	init_abs = init.copy()
	n = len(init)

	i = 0

	step_text = getSeqObjects(init_current, ORIGIN).to_edge(LEFT, buff=1)

	self.play(*[Write(text) for text in step_text], run_time=run_time)

	addStepToTheSide(self, step_text, 0)

	while init_current != target:
		
		if target[i] == init_current[i]:
			i = (i + 1) % n
			continue

		target_index = init_abs.index(target[i])

		# checkMaxLength(self, all_steps)

		start_mark, end_mark = putMarkOnRange(step_text, i, target_index)

		self.play(
			Write(start_mark),
			Write(end_mark),
			run_time=run_time
		)

		init_current = reverseWithSignForStr(init_current, i, target_index)

		updated_step_text = getSeqObjects(init_current, ORIGIN).move_to(step_text)

		for j in range(i, target_index + 1):
			updated_step_text[j].set_color(GREY)

		end_mark.set_color(GREY)
		start_mark.set_color(GREY)

		self.play(
			*[
				Transform(step_text[j], updated_step_text[j])
				for j in range(len(init_current))
			],
			FadeOut(start_mark),
			FadeOut(end_mark),
			run_time=run_time
		)

		init_abs = reverseWithoutSign(init_abs, i, target_index)
		
		operations_count += 1

		addStepToTheSide(self, step_text, operations_count)
		
		for j in range(len(init_current)):
			step_text[j].set_color(WHITE)
		
		i = (i + 1) % n

	print("success")
	operations_text = Text(f"Operations: {operations_count}", font_size=46).to_edge(LEFT + DOWN)
	self.play(Write(operations_text), run_time=run_time)
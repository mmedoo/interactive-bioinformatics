from manim import *
from ..utils.public import *
from ..utils.linear import *

all_steps = []
operations_count = 0

def runGreedy(self, init: list, target: list):
	global operations_count
	init_current = init.copy()
	init_abs = init.copy()
	n = len(init)

	i = 0
	while init_current != target:
		
		if target[i] == init_current[i]:
			i = (i + 1) % n
			continue

		target_index = init_abs.index(target[i])

		checkMaxLength(self, all_steps)

		step_pos = 3*UP + len(all_steps) * DOWN

		step_text = getSeqObjects(init_current, step_pos)

		self.play(*[Write(text) for text in step_text], run_time=0.5)

		start_mark, end_mark = putMarkOnRange(step_text, i, target_index)

		self.play(
			Write(start_mark),
			Write(end_mark),
			run_time=0.25
		)

		init_current = reverseWithSignForStr(init_current, i, target_index)

		updated_step_text = getSeqObjects(init_current, step_pos)

		for j in range(i, target_index + 1):
			updated_step_text[j].set_color(GREY)

		self.play(
			*[
				Transform(step_text[j], updated_step_text[j])
				for j in range(n)
			],
			Transform(end_mark, end_mark.set_color(GREY)),
			Transform(start_mark, start_mark.set_color(GREY)),
			run_time=0.5
		)

		init_abs = reverseWithoutSign(init_abs, i, target_index)

		operations_count += 1
		
		all_steps.append([step_text + [start_mark, end_mark]])

		i = (i + 1) % n

	print("success")
	operations_text = Text(f"Operations: {operations_count}", font_size=36).to_edge(RIGHT)
	self.play(Write(operations_text))
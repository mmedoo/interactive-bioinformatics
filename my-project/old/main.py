from math import sin, cos
from manim import *
from manim.opengl import *

# constants
seq = ['A', 'B', 'C', 'D', 'E', 'F']
sorted_sq = sorted(seq)
r = 2.5
clockwise = True
dot_radius = 0.11
label_distance_from_center = 1.3
label_font_size = 42
run_time = 0.5

# derived values
n = len(seq)
dir = -1 if clockwise else 1
# begin_angle = 0
# gap_angle = 4*PI / (n*n)
total_gap = PI
gap_angle = total_gap / n
block_angle = (2*PI / n) - gap_angle
begin_angle = PI/2 - block_angle/2 * dir



def getPointFromAngle(angle):
	return [r * cos(angle), r * sin(angle), 0]



def getNextBlockTail(block):
	next_block_index = (seq.index(block) + 1) % n
	next_block_order = sorted_sq.index(seq[next_block_index])
	angle = begin_angle + next_block_order * (block_angle + gap_angle) * dir
	return getPointFromAngle(angle)

map = {}

class DefaultTemplate(Scene):
	def construct(self):

		starts = []
		ends = []
		arcs = []
		start_labels = []
		end_labels = []
		gaps = []

		for i in range(n):

			st_angle = begin_angle + i * (block_angle + gap_angle) * dir
			st_point = getPointFromAngle(st_angle)
			st_dot = Annulus(0, dot_radius, color=RED)
			st_dot.move_to(st_point)

			ed_angle = st_angle + block_angle * dir
			ed_point = getPointFromAngle(ed_angle)
			ed_dot = Annulus(0, dot_radius, color=GREEN)
			ed_dot.move_to(ed_point)
			
			
			segment = ArcBetweenPoints(st_point, ed_point, radius=r * dir)

			
			arrow_ed_pt = getNextBlockTail(sorted_sq[i])

			arrow = Arrow(ed_point, arrow_ed_pt, color=BLUE_E)
			# arc = CurvedArrow(st_point, ed_point, radius= r * dir)
			# arc = CurvedArrow(st_point, arrow_ed_pt, radius= r * dir)

			
			label_position = segment.get_center() * label_distance_from_center
			label = Text(f"{sorted_sq[i]}", font_size=label_font_size)
			label.move_to([label_position])

			# map[sorted_sq[i]] = {
			# 	'start': st_dot,
			# 	'end': ed_dot,
			# 	'segment': segment,
			# 	'arrow': arrow,
			# 	'label': label
			# }

			# self.play(Create(st_dot),Create(ed_dot), run_time=run_time)
			# self.play(Create(segment), run_time=run_time)
			# self.play(Write(label), run_time=run_time)
			# self.play(Create(arrow), run_time=run_time)
			
			self.add(segment)
			self.add(st_dot)
			self.add(arrow)
			self.add(ed_dot)
			self.add(label)
			
			# starts.append(Create(st_dot))
			arcs.append(Create(arrow))
			# start_labels.append(Write(st_label))
			# ends.append(Create(ed_dot))

		
		self.interactive_embed()
		
		# for arc in arcs:
		# 	self.play(arc, run_time=run_time)

		# self.play(*starts, run_time=run_time - 0.25)
		# self.play(*start_labels, run_time=run_time)
		# self.play(*ends, run_time=run_time - 0.25)
		# self.play(*gaps, run_time=run_time)
		# self.play(*arcs, run_time=run_time)
		# self.wait(1.5)

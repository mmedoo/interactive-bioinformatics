from math import sin, cos, pi
from manim import *

# Constants
iseq = ['A', 'E', 'C', 'F', 'D', 'B']
fseq = ['A', 'D', 'C', 'B', 'E', 'F']
iseq_color = BLUE
fseq_color = RED

declare_dist_from_edge = 1
declare_font_size = 40

st_dot_color = PURPLE_C
ed_dot_color = GREEN
dot_radius = 0.11
total_gap = PI

r = 2.5
clockwise = True
label_distance_from_center = 1.3
label_font_size = 36
run_time = 0.75

# Derived values
sorted_sq = sorted(fseq)
n = len(sorted_sq)
dir = -1 if clockwise else 1
r = r * dir
gap_angle = dir * total_gap / n
block_angle = (2 * dir * pi / n) - gap_angle
begin_angle = dir * pi / 2 - block_angle / 2


class DefaultTemplate(Scene):
	def construct(self):
		starts = []
		ends = []
		arcs = []
		labels = []

		def getCoordFromAngle(angle):
			return [r * cos(angle), r * sin(angle), 0]
			
		for i in range(n):
			st_angle = begin_angle + i * (block_angle + gap_angle)
			st_point = getCoordFromAngle(st_angle)
			st_dot = Annulus(0, dot_radius, color=st_dot_color)
			st_dot.move_to(st_point)

			ed_angle = st_angle + block_angle
			ed_point = getCoordFromAngle(ed_angle)
			ed_dot = Annulus(0, dot_radius, color=ed_dot_color)
			ed_dot.move_to(ed_point)

			segment = ArcBetweenPoints(st_point, ed_point, radius=r)

			label_position = segment.get_center() * label_distance_from_center
			label = Text(f"{sorted_sq[i]}", font_size=label_font_size)
			label.move_to(label_position)

			starts.append(st_dot)
			ends.append(ed_dot)
			arcs.append(segment)
			labels.append(label)

		# Draw the circle and labels
		for st_dot, ed_dot, segment, label in zip(starts, ends, arcs, labels):
			# self.play(Create(segment), Create(st_dot), Create(ed_dot), run_time=run_time)
			# self.play(Write(label), run_time=run_time)
			self.add((segment), (st_dot), (ed_dot))
			self.add((label))
			
		def drawSequenceArrows(seq, declare_position, color):
			seq_text = Text("".join(seq), font_size=declare_font_size, color=color)
			seq_text.to_edge(declare_position, buff=declare_dist_from_edge)  # Adjusted for clarity
			self.play(Write(seq_text), run_time=run_time)

			for i in range(n):
				start_label = seq[i]
				end_label = seq[(i + 1) % n]

				start_idx = sorted_sq.index(start_label)
				end_idx = sorted_sq.index(end_label)

				start_point = starts[start_idx].get_center()
				end_point = ends[end_idx].get_center()

				arrow_blue = Arrow(start_point, end_point, color=color)

				highlight_text = Text(f"{start_label} → {end_label}", font_size=declare_font_size, color=color)
				highlight_text.move_to(seq_text.get_center() + DOWN * 1.2)

				self.play(Write(highlight_text), Create(arrow_blue), run_time=run_time)
				self.play(FadeOut(highlight_text), run_time=run_time)
				# self.add((highlighted_text), (arrow_blue))
				# self.remove((highlighted_text))
		
		drawSequenceArrows(iseq, UP + LEFT, iseq_color)
		drawSequenceArrows(fseq, UP + RIGHT, fseq_color)
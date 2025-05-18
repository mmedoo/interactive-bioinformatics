from manim import *
from manim.typing import Point3D
from math import sin, cos, pi

r = 2.5
clockwise = True
dot_radius = 0.1225
label_distance_from_center = 1.1
label_font_size = 36
run_time = 0.7

start_dot_color = GREEN
end_dot_color = GREEN
initial_lines_color = RED_C
target_lines_color = BLUE_C

dir = -1 if clockwise else 1
total_gap = pi

def isPointEndOfLine(point: Point3D, line: Line) -> bool:
	return np.array_equal(point, line.get_end())

def getPointFromAngle(angle: float) -> Point3D:
	return np.array([r * cos(angle), r * sin(angle), 0])

def count_cycles(permutation):
	seen = set()
	cycles = 0
	for i in range(len(permutation)):
		if i not in seen:
			cycles += 1
			current = i
			while permutation[current] not in seen:
				seen.add(current)
				current = permutation[current]
	return cycles

def runCircular(self, Initial: list[str], Target: list[str]):

	n = len(Target)
	gap_angle = total_gap / n
	block_angle = (2 * pi / n) - gap_angle
	begin_angle = pi / 2 - block_angle / 2 * dir

	starts: list[Annulus] = []
	ends: list[Annulus] = []

	startsMap: dict[str, Point3D] = {}
	endsMap: dict[str, Point3D] = {}
	
	for j in range(n):
		st_angle = begin_angle + j * (block_angle + gap_angle) * dir
		st_point = getPointFromAngle(st_angle)
		st_dot = Annulus(inner_radius=0, outer_radius=dot_radius, color=start_dot_color).move_to(st_point)

		ed_angle = st_angle + block_angle * dir
		ed_point = getPointFromAngle(ed_angle)
		ed_dot = Annulus(inner_radius=0, outer_radius=dot_radius, color=end_dot_color).move_to(ed_point)

		segment = ArcBetweenPoints(st_point, ed_point, radius=r * dir, color=GREEN_C)

		label_position = segment.get_center() * label_distance_from_center
		label = Text(f"{Target[j]}", font_size=label_font_size).move_to(label_position)

		starts.append(st_dot)
		ends.append(ed_dot)
		startsMap[Target[j]] = st_point
		endsMap[Target[j]] = ed_point

		self.play(
			FadeIn(st_dot),
			FadeIn(ed_dot),
			Write(label),
			run_time=run_time
		)

	temp = []
	for j in range(n):
		st_point = endsMap[Target[j]]
		ed_point = startsMap[Target[(j + 1) % n]]
		line = ArcBetweenPoints(st_point, ed_point, radius=r * dir, color=target_lines_color)
		temp.append(line)

	self.play(*[Create(line) for line in temp])

	linesMap: dict[tuple[float, float, float], Line] = {}

	temp = []
	for j in range(n):
		st_point = endsMap[Initial[j]]
		ed_point = startsMap[Initial[(j + 1) % n]]
		line = Line(st_point, ed_point, radius=r * dir, color=initial_lines_color)
		temp.append(line)
		linesMap[tuple(st_point)] = line
		linesMap[tuple(ed_point)] = line

	self.play(*[Create(line) for line in temp])

	switchFirstDot: Annulus | None = None
	switchSecondDot: Annulus | None = None

	def switchEdges():
		nonlocal switchFirstDot, switchSecondDot
		assert switchFirstDot is not None
		assert switchSecondDot is not None

		p1 = switchFirstDot.get_center()
		p2 = switchSecondDot.get_center()

		line1 = linesMap[tuple(p1)]
		line2 = linesMap[tuple(p2)]

		switchFirstDot.set_color(WHITE)
		switchSecondDot.set_color(WHITE)
		switchFirstDot = None
		switchSecondDot = None

		if line1 == line2:
			return
		
		p1_is_line1_end: bool = isPointEndOfLine(p1, line1)
		p2_is_line2_end: bool = isPointEndOfLine(p2, line2)

		newLine1 = Line(line1.get_start(), p2) if p1_is_line1_end else Line(p2, line1.get_end())
		newLine2 = Line(line2.get_start(), p1) if p2_is_line2_end else Line(p1, line2.get_end())

		newLine1.set_color(initial_lines_color)
		newLine2.set_color(initial_lines_color)

		self.play(
			Transform(line1, newLine1),
			Transform(line2, newLine2),
			run_time=run_time
		)

		linesMap[tuple(p1)] = line2
		linesMap[tuple(p2)] = line1
	
	def addPointToSwitch(dot: Annulus):
		nonlocal switchFirstDot, switchSecondDot

		if switchFirstDot is None:
			switchFirstDot = dot
			dot.set_color(PURPLE)

		elif switchSecondDot is None:
			switchSecondDot = dot
			dot.set_color(PURPLE)
			switchEdges()

		else:
			switchFirstDot = dot
			dot.set_color(PURPLE)
			switchSecondDot = None

	for j in range(n):
		st_dot: Annulus = ends[j]
		ed_dot: Annulus = starts[j]
		self.makeClickable(st_dot, lambda m: addPointToSwitch(m))
		self.makeClickable(ed_dot, lambda m: addPointToSwitch(m))
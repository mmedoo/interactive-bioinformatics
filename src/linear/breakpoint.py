from ..utils.linear import *
from ..utils.public import reverseWithSignForInts

def Find_Breakpoints(p: list[int]) -> list[int]:
	return [i for i in range(len(p) - 1) if p[i + 1] - p[i] != 1]

def runBps(self, init, target):
	init = [int(x) for x in init]
	target = [int(x) for x in target]

	init_current = init.copy()
	markers: list[Circle] = []
	bps_no: Text | None = None

	smallest = min(target)
	largest = max(target)
	init_current = [smallest - 1] + init + [largest + 1]
	target = [smallest - 1] + target + [largest + 1]

	step_text = getSeqObjects(init_current, ORIGIN)
	
	step_text[0].set_color(GREY)
	step_text[-1].set_color(GREY)

	self.play(*[Write(text) for text in step_text], run_time=0.5)

	def applyReversal(start: int, end: int):
		nonlocal init_current

		if start > end:
			start, end = end, start

		init_current = reverseWithSignForInts(init_current, start+1, end)

		updated_text = getSeqObjects(init_current, ORIGIN)
		self.play(
			*[Transform(step_text[j], updated_text[j]) for j in range(1, len(init_current)-1)],
			run_time=0.5
		)

	def updateMarkers():
		nonlocal markers

		self.remove(*[m for m in markers])
		self.buttons = []
		markers = []
		
		bps_indices = Find_Breakpoints(init_current)

		if len(bps_indices) == 0:
			update_bps_number(len(bps_indices))
			return	

		start_point = None
		end_point = None

		def fixMarker(marker, index):
			nonlocal start_point, end_point
			marker.set_color(BLUE)

			if start_point is None:
				start_point = index
				end_point = None
				return

			if end_point is None:
				end_point = index
				applyReversal(start_point, end_point)
				updateMarkers()

		for index in bps_indices:
			marker = putMarkOnBlockRight(step_text[index])
			markers.append(marker)
			self.makeClickable(marker, lambda x, idx=index: fixMarker(x, idx))

		self.play(*[Write(m) for m in markers], run_time=0.5)
		update_bps_number(len(bps_indices))

	def update_bps_number(no):
		nonlocal bps_no
		bps_no_text = Text(f"Breaks: {no}", font_size=46).to_edge(DOWN, buff=0.5)
		if bps_no is not None:
			# self.play(Transform(bps_no, bps_no_text), run_time=0.5)
			self.remove(bps_no)
			self.add(bps_no_text)
			bps_no = bps_no_text
		else:
			bps_no = bps_no_text
			self.add(bps_no)

	updateMarkers()
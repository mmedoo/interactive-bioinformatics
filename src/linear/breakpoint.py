from ..utils.linear import *
from ..utils.public import reverseWithSignForInts, reverseWithSignForStr
from ..config import run_time

def orderBlocks(p: list, t: list) -> list:
	n = len(p)
	init = []

	for block in p:
		init.append(-t.index(block[1]) if block.startswith('-') else t.index(block))

	return init

def Find_Breakpoints(p: list, t: list) -> list[int]:
	init = orderBlocks(p, t)
	
	n = len(p)
	bps = []

	for i in range(n-1):
		if (init[i+1] - init[i]) != 1:
			bps.append(i)

	return bps

def runBps(self, init, target):
	# init = [int(x) for x in init]
	# target = [int(x) for x in target]

	operations_count = 0

	init_current = init.copy()
	markers: list[Circle] = []
	bps_no: Text | None = None

	# smallest = min(target)
	# largest = max(target)
	init_current = ['0'] + init + [f"{len(init)+1}"]
	target = ['0'] + target + [f"{len(init)+1}"]

	step_text = getSeqObjects(init_current, ORIGIN).to_edge(LEFT, buff=1)
	
	step_text[0].set_color(GREY)
	step_text[-1].set_color(GREY)

	self.play(*[Write(text) for text in step_text], run_time=run_time)

	addStepToTheSide(self, step_text[1:-1], operations_count)

	def applyReversal(start: int, end: int):
		nonlocal init_current, operations_count, markers, step_text

		if start > end:
			start, end = end, start

		init_current = reverseWithSignForStr(init_current, start+1, end)

		updated_text = getSeqObjects(init_current, ORIGIN).move_to(step_text)
		
		for j in range(start+1, end+1):
			updated_text[j].set_color(GREY)
		
		updated_text[0].set_color(GREY)
		updated_text[-1].set_color(GREY)
		
		self.play(
			*[
				Transform(step_text[j], updated_text[j])
				for j in range(1, len(init_current)-1)
			],
			run_time=run_time
		)

		for m in markers:
			self.buttons.remove(m)
			self.remove(m)

		operations_count += 1

		addStepToTheSide(self, step_text[1:-1], operations_count)

		step_text[1:-1].set_color(WHITE)

	def updateMarkers():
		nonlocal markers

		markers = []
		
		bps_indices = Find_Breakpoints(init_current, target)

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

		self.play(*[Write(m) for m in markers], run_time=run_time)
		update_bps_number(len(bps_indices))

	def update_bps_number(no):
		nonlocal bps_no
		bps_no_text = Text(f"Breaks: {no}", font_size=46).to_edge(DOWN + LEFT, buff=0.5)
		if bps_no is not None:
			# self.play(Transform(bps_no, bps_no_text), run_time=0.5)
			self.remove(bps_no)
			self.add(bps_no_text)
			bps_no = bps_no_text
		else:
			bps_no = bps_no_text
			self.add(bps_no)

	updateMarkers()
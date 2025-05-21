from typing import Literal
from pyglet.window import key as keys


def toggle_sign(x: str) -> str:
	if x.startswith('-'):
		return x[1:]
	return '-' + x

def reverseWithSignForStr(p: list[str], start: int, end: int) -> list[str]:
	reversed_subarray = [toggle_sign(x) for x in p[start:end+1][::-1]]
	return p[:start] + reversed_subarray + p[end+1:]

def reverseWithSignForInts(p: list[int], start: int, end: int) -> list[int]:
	reversed_subarray = [-x for x in p[start:end+1][::-1]]
	return p[:start] + reversed_subarray + p[end+1:]

def reverseWithoutSign(p: list[str], start: int, end: int) -> list[str]:
	reversed_subarray = p[start:end+1][::-1]
	return p[:start] + reversed_subarray + p[end+1:]

def check_if_char(symbol) -> str | Literal[False]:
	if symbol in (keys.NUM_0, keys.NUM_1, keys.NUM_2, keys.NUM_3, keys.NUM_4, keys.NUM_5, keys.NUM_6, keys.NUM_7, keys.NUM_8, keys.NUM_9):
		return str(symbol - keys.NUM_0)
	# if chr(symbol).isalnum() or chr(symbol) == '-':
	if chr(symbol).isalnum():
		return str(chr(symbol).upper())
	return False
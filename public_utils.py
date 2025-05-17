# Function to reverse a section of a list between two indices (inclusive)
def toggle_sign(x):
	if x.startswith('-'):
		return x[1:]
	return '-' + x

def reverseWithSign(p, start, end):
	reversed_subarray = [toggle_sign(x) for x in p[start:end+1][::-1]]
	return p[:start] + reversed_subarray + p[end+1:]

def reverseWithSignForNumbers(p, start, end):
	reversed_subarray = [-x for x in p[start:end+1][::-1]]
	return p[:start] + reversed_subarray + p[end+1:]

def reverseWithoutSign(p, start, end):
	reversed_subarray = p[start:end+1][::-1]
	return p[:start] + reversed_subarray + p[end+1:]

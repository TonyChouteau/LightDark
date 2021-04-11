import sys
import re
import itertools
from string import ascii_lowercase

def LightDark(file):
	if not file:
		exit(1)

	if len(sys.argv)>=2:
		fileIn = sys.argv[1]
	else:
		raise "You must specify a file in argument of the call"

	fileOut = sys.argv[2] if len(sys.argv)>=3 else "out"

	with open(fileIn, "r") as f:
		data = f.read().replace("\t","").split("\n")

		#print(data[:20])

		commentStarted = False
		lineToRemove = []
		for line in data:
			line = re.sub(" *", "", line)
			if re.search("^/\*", line):
				commentStarted = True
				lineToRemove.append(True)
			elif commentStarted:
				lineToRemove.append(True)
				if re.search("^.*\*/", line):
					commentStarted = False
			else:
				lineToRemove.append(False)
		
		data2 = []
		for i in range(len(data)):
			if not lineToRemove[i]:
				data2.append(data[i])

		for i in range(len(data2)):
			data2[i] = re.sub("//.*$", "", data2[i])

		result = ("").join(list(filter(lambda d: d is not "", data2)))

		# javascriptNamespaces = [
		# 	"function", "let", "const", "var", "true", "false", "class", "this", "if", 
		# 	"switch", "else", "while", "for", "window", "G", "oldG", "in", "fillText",
		# 	"Math", "beginPath", "stroke", "min", "max", "moveTo", "lineTo", "rect",
		# 	"fillRect", "push", "floor", "ceil", "round", "toFixed", "measureText",
		# 	"getElementById", "getElementsByTagName", "getElementsByClassName", "document", 
		# 	"canvas", "black", "white", "width", "height", "body", "Infinity", "return", 
		# 	"console", "log", "warn", "error", "getContext", "createElement", "fillStyle",
		# 	"strokeStyle", "px", "Arial", "append", "font", "length", "err", "id",
		# 	"i", "x", "y", "j", "d", "stroke", "str", "plot", "scatter", "type", "size"]

		# namespaces = list(set(list(filter(lambda l:l is not "" and l not in javascriptNamespaces, re.findall("[A-Za-z_][A-Za-z0-9_]*", result)))))
		# print(namespaces)

		# replacement = list(itertools.chain.from_iterable([[i+j for j in list(ascii_lowercase)] for i in list(ascii_lowercase)]))

		# index_replacement = 0
		# for name in namespaces[:20]:
		# 	print(name+" "+replacement[index_replacement])
		# 	result = result.replace(name, replacement[index_replacement])
		# 	index_replacement += 1

		with open(fileOut, "w") as f2:
			f2.write(result)

if __name__ == "__main__":
    LightDark(sys.argv)
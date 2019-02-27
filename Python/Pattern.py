import re

p = re.compile("ab")

it = p.finditer("abaaabaabaddbbbbabbab")

while(it.has):
	print(it.start(),"....",it.end(),".....",it.group())
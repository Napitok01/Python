s = input()
s = s.replace("a", "").replace("o", "").replace("y", "").replace("e", "").replace("u", "").replace("i", "").replace("A", "").replace("O", "").replace("Y", "").replace("E", "").replace("U", "").replace("I", "").lower()
s = ".".join(s)
print('.' + s.lower(), sep="")

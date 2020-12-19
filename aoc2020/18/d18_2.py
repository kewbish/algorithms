from re import sub, findall

with open("input.txt") as x:
    lines = x.read().splitlines()
    lines = [li.replace("*", "-").replace("+", "*") for li in lines]
    lines = [sub(r"(\d+)", r"Xmaths(\1)", li) for li in lines]

class Xmaths(int):
    def __sub__(self, n):
        # apparently overloading operators is a thing, thxu Reddit
        return Xmaths(self.real * n.real)
        # real is real component
    def __mul__(self, n):
        return Xmaths(self.real + n.real)

liarr = [eval(li) for li in lines]
print(sum(liarr))


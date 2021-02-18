import string

class Solution:
    def __init__(self):
        self.visited = set()
        self.equations_possible = True

    def equationsPossible(self, equations: List[str]) -> bool:
        self.uf = dict.fromkeys(string.ascii_lowercase, None)
        for eq in equations:
            if eq[1] == "=":
                x = eq[0]
                y = eq[3]
                self.union(x, y)
        for eq in equations:
            if eq[1] == "!":
                x = eq[0]
                y = eq[3]
                self.connected(x, y)
        return self.equations_possible

    def union(self, x, y):
        if x == y:
            return
        if not self.uf[x]:
            self.uf[x] = [y]
        else:
            self.uf[x].append(y)
        if not self.uf[y]:
            self.uf[y] = [x]
        else:
            self.uf[y].append(x)

    def connected(self, x, y):
        if x == y:
            self.equations_possible = False
            return
        elif self.uf[x] is None:
            return
        elif y in self.uf[x]:
            self.equations_possible = False
        for item in self.uf[x]:
            if (item, y) not in self.visited:
                self.visited.add((item, y))
                self.connected(item, y)

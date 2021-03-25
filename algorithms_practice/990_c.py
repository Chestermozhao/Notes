class DSU:
    def __init__(self):
        self.l = list(range(1000))
        return
    def find(self, x):
        print("====", x, self.l[x])
        if self.l[x] != x:
            self.l[x] = self.find(self.l[x])
        return self.l[x]

    def union(self,x,y):
        xx = self.find(x)
        yy = self.find(y)
        self.l[xx] = yy
        return  

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU()
        record = []
        for eq in equations:
            if "!" in eq:
                record.append(eq)
            else:
                print(ord(eq[0]), ord(eq[-1]))
                dsu.union(ord(eq[0]),ord(eq[-1]))
        #print("====", dsu.l)
        for rest in record:
            if dsu.find(ord(rest[0])) == dsu.find(ord(rest[-1])):
                return False
        return True

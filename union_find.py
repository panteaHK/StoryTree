class UnionFind:
    def __init__(self):
        self.parent = []
        self.birth = []
        self.death = []
        self.children = {}

    def make_set(self, x, birth):
        self.parent.append(x)
        self.birth.append(birth)
        self.death.append(1)
        self.children[x] = []
        if self.parent[x] != x:
            print("Parent {} = {}".format(x, self.parent[x]))

    def find_set(self, x):
        if self.parent[x] == x:
            return x
        return self.find_set(self.parent[x])

    def union(self, x, y, death):
        # surviver, dead
        a = self.find_set(x)
        b = self.find_set(y)
        if a == b:
            return a
        if self.birth[a] <= self.birth[b]:
            self.parent[b] = a
            self.death[b] = death
            self.children[a].append(b)
            return a
        elif self.birth[a] > self.birth[b]:
            self.parent[a] = b
            self.death[a] = death
            self.children[b].append(a)
            return b
            

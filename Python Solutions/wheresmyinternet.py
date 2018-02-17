class Graph:
    def __init__(self):
        self.par  = dict()
        self.tree = dict()

    def addEdge(self, a, b):
        A = self.getParent(a)
        B = self.getParent(b)
        if(B == A): return self.tree[A]

        # Swap A and B based on size
        if(self.tree[A] < self.tree[B]):
            A = B
            B = A

        self.par[B] = A
        self.tree[A] += self.tree[B]

        return self.tree[A]

    def getParent(self, i):

        if(i not in self.par):
            self.par[i] = None
            self.tree[i] = 1
            return i

        if(self.par[i] != None):
            return self.par[i]



        return i


    def getConnection(self, a, b):
        return self.getParent(str(a)) == self.getParent(str(b))

numOfNotConnected = 0
house = 2

N, M = map(int, input().split())
g = Graph()

# Create Graph
for i in range(M):
    a, b = input().split()
    g.addEdge(a, b)

# check connections
while(house < N + 1):
    if(not g.getConnection(1, house)):
        numOfNotConnected += 1
        print(house)
    house += 1


if(numOfNotConnected == 0): print("Connected")

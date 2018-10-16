from collections import defaultdict
from heapq import *

pieces = defaultdict(set)
N = int(input())

# Create Dictionary of a map pieces
for i in range(N):
    line = input().split()
    frm = line.pop(0)
    loc = line
    pieces[frm].update(loc)
    for j in loc:
        pieces[j].add(frm)






visited = {}
s, e = input().split()



# Depth First Search using heap
heap = [s]
while(heap):
    node = heappop(heap)
    if(e == node): break
    for p in pieces[node]:
        if not p in visited:
            visited[p] = node
            heappush(heap, p)



if e in visited:
    result = ""
    result = e + result
    e = visited[e]
    while e != s:
        result = e + " " + result
        e = visited[e]
    result = s + " " + result
    print(result)
else: print("no route found")

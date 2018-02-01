import sys

needsPointlessIndent = False


for line in sys.stdin:
    task = line.split()
    if(len(task) == 1):
        a = 0
        b = 0
        if(int(task[0]) == 0): break
        else: N = task[0]

        if(needsPointlessIndent): print()
        needsPointlessIndent = True
    else:
        act = task[0]
        amt = int(task[1])
        if(act == "DROP"):
            b += amt
            print("DROP 2 " + str(amt))

        if(act == "TAKE"):
            d = a - amt
            if(a >= amt):
                a -= amt
                print("TAKE 1 " + str(amt))
            else:
                if(a != 0):
                    print("TAKE 1 " + str(amt))
                    a = 0
                print("MOVE 2->1 " + str(b))
                a = b
                b = 0
                print("TAKE 1 " + str(amt))
                a += d

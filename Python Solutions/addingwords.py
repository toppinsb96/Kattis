import sys
diction = {}


for line in sys.stdin:
    cLine = line.split()

    command = cLine[0]

    if command == "def": diction.update({cLine[1]: int(cLine[2])})

    elif command == "calc":
        r = 0
        op = "+"

        calc = (cLine[1:len(cLine)-1])

        for i in calc:
            if(i == "+"):   op = "+"
            elif(i == "-"): op = "-"

            else:
                var = diction.get(i)
                if(var == None):
                    r = "unknown"
                    break
                else:
                    if(op == "+"): r += var
                    else:          r -= var

        print((line[5:len(line)].splitlines())[0], end = " ")

        if(r == "unknown"):
            print("unknown")
        elif(r not in diction.values()):
            print("unknown")
        else:
            print(list(diction.keys())[list(diction.values()).index(r)])

    elif(command == "clear"):
        diction.clear()

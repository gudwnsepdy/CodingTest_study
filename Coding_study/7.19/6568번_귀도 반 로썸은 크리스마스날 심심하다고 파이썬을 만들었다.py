pc = 0
adder = 0
mem = [0 for i in range(32)]
while 1:
    try:
        pc += 1
        command = str(input())
        if command == "d":
            print(format(adder,'b'))
            exit()
        p = command[3:]
        command = command[:3]
        p = int("0b" + p, 2)



        if command == "000":

            mem[p] = adder

        elif command == "001":

            adder = mem[p]

        elif command == "010":

            if adder == 0:
                pc = p

        elif command == "011":
            continue

        elif command == "100":
            # print("DEC")
            adder -= 1

        elif command == "101":
            # print("INC")
            adder += 1
            if adder >= 32:
                adder = 0

        elif command == "110":
            # print("JMP")
            pc = p

        else:

            print(adder, "HTL")
        print(adder)

    except EOFError:
        print(adder)
        exit()
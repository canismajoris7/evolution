import random
def op(x, num):
    plist = []
    for i in x:
        plist.append(i[num])
    return plist
if str(input('default variables, y or n')) == 'y':
    d = -16
    e = 2
    d2 = -10
    e2 = 2
    d3 = -10
    e3 = 2
    de = -16
    ed = 2
    de2 = -3
    ed2 = 3
    de3 = -3
    ed3 = 3
    a = -1
    b = -1
    c = -1
    tites = 9
    big = 100

elif str(input('default variables, y or n')) == 'n':
    d = int(input())
    e = int(input())
    d2 = int(input())
    e2 = int(input())
    d3 = int(input())
    e3 = int(input())
    de = int(input())
    ed = int(input())
    de2 = int(input())
    ed2 = int(input())
    de3 = int(input())
    ed3 = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    tites = int(input())
    big = int(input())
def p(x):
    r1 = ''
    r2 = ''
    r3 = ''
    r4 = ''
    r5 = ''
    r6 = ''
    r7 = ''
    r8 = ''
    r9 = ''
    r10 = ''
    r11 = ''
    r12 = ''
    for i in x:
        if i[0] <= 0:
            r1 += "     .{{}}}}}}.        |"
            r2 += "    {{{{{{(" + str(i) + ")}}}.      "
            r3 += "   {{{(" + str(i) + ")}}}}}}}}}     "
            r4 += "  }}}}}}}}}{{(" + str(i) + "){{{    "
            r5 += "  }}}}{{{{(" + str(i) + ")}}{{{{    "
            r6 += " {{{(" + str(i) + ")}}}}}}}{}}}}}   "
            r7 += "{{{{{{{{(" + str(i) + ")}}}}}}}}}}  "
            r8 += "{{{{{{{}{{{{(" + str(i) + ")}}}}}}  "
            r9 += " {{{{{(" + str(i) + ")   {{{{(" + str(i) + ")}' "
            r10 += """  `""'" |   | "'"'`    |"""
            r11 += "  (" + str(i) + ")  /     \         "
            r12 += " ~~~~~~~~~~~~~~~~~~~   |"
        else:
            r1 += "     .{{}}}}}}.        |"
            r2 += "    {{{{{{(" + str(i) + ")}}}.      |"
            r3 += "   {{{(" + str(i) + ")}}}}}}}}}     |"
            r4 += "  }}}}}}}}}{{(" + str(i) + "){{{    |"
            r5 += "  }}}}{{{{(" + str(i) + ")}}{{{{    |"
            r6 += " {{{(" + str(i) + ")}}}}}}}{}}}}}   |"
            r7 += "{{{{{{{{(" + str(i) + ")}}}}}}}}}}  |"
            r8 += "{{{{{{{}{{{{(" + str(i) + ")}}}}}}  |"
            r9 += " {{{{{(" + str(i) + ")   {{{{(" + str(i) + ")}'  |"
            r10 += """  `""'" |   | "'"'`    |"""
            r11 += "  (" + str(i) + ")  /     \         |"
            r12 += " ~~~~~~~~~~~~~~~~~~~   |"
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)
    print(r7)
    print(r8)
    print(r9)
    print(r10)
    print(r11)
    print(r12)
global pop
pop = []
for i in range(0, tites):
    pop.append([0, 0, 0])
for ele in range(0, len(pop)):
    pop[ele][0] += random.randint(de, ed)
for ele in range(0, len(pop)):
    pop[ele][1] += random.randint(de2, ed2)
for ele in range(0, len(pop)):
    pop[ele][2] += random.randint(de3, ed3)
print('this is the first generation of bananas, the values of each element is the sweetness of the bananas')
print(op(pop, 0))
t = 0
n = 1
while n != big:

    if str(input()) == '':
        n += 1
        global pi
        pi = pop[0][0]
        for i in range(0, len(pop)):
            if pop[i][0] >= pi:
                pi = pop[i][0]
            else:
                continue
        global ri
        ri = pop[0][1]
        for i in range(0, len(pop)):
            if pop[i][1] >= ri:
                ri = pop[i][1]
            else:
                continue
        global di
        di = pop[0][2]
        for i in range(0, len(pop)):
            if pop[i][2] >= di:
                di = pop[i][2]
            else:
                continue
        print('the best trees are these ones: ' + str(pi)) #+ ' ' + str(ri) + ' ' + str(di))
        print(' ')
        print('he gets to make children with sweetness mutations')
        print('the mutations are usually bad, but every once in a while they are good')
        print(' ')
        print(' ')

        for i in range(0, len(pop)):
            if random.randint(0, 10) >= a:
                ter = random.randint(d, e)

                pop[i][0] = pi + ter
        for i in range(0, len(pop)):
            if random.randint(0, 10) >= b:
                ter2 = random.randint(d2, e2)
                pop[i][1] = ri + ter2

        for i in range(0, len(pop)):
            if random.randint(0, 10) >= c:
                pop[i][2] = di + random.randint(d3, e3)

        print('this is the next population, gen ' + str(n))

        print(op(pop, 0))
        print(' ')

# -*- coding: utf-8 -*-
import sys
import time

state = " "
ASN = 15835
prefix = "195.209.148.0/24"

def scr(path):
    global state
    try:
        f = open(path, 'r')
        lst1 = []
        L1 = f.readline()
        for x in L1.split():
            lst1.append(int(x))
        print (lst1)

        lst2 = []
        L2 = f.readline()
        for x in L2.split():
            lst2.append(x)
        print (lst2)

        c = 0
        if search(lst1, ASN) & search(lst2, prefix):
             c = 1

        if c == 1:
            if (len(lst1) == 1) & (len(lst2) == 1):
                printing("OK")
            elif (len(lst1) == 1) & (len(lst2) != 1):
                printing("CRITICAL_1")
            elif (len(lst1) != 1) & (len(lst2) == 1):
                printing("CRITICAL_2")
            else:
                printing("UNKNOWN")
        else:
            printing("UNKNOWN")
        f.close()
    except Exception:
        sys.stdout.write("WARNING\n")
        exit(1)

def search(A, key):
    i = 0
    while i < len(A) and A[i] != key:
        i += 1
    return i < len(A)

def printing(state):
    if state == "OK": # в списке more specific будет только один префикс, в списке as-origin будет только один номер
        print "OK\n"
        exit(0)
    elif state == "CRITICAL_1": # в списке more specific будет/будут префикс/ы отличные от заданного
        print "CRITICAL, type = 1\n"
        exit(2)
    elif state == "CRITICAL_2": # в списке as-origin будет/будут номер/а отличные от заданого
        print "CRITICAL, type = 2\n"
        exit(2)
    else:
        print "UNKNOWN\n"
        exit(3)

print  "Input data: ASN --", ASN, ", prefix --", prefix

pathfile = sys.argv[1]
scr(pathfile)



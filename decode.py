#!/usr/bin/python3

import sys

f = open(sys.argv[1], "r")
tempArr = f.read().splitlines()
arr = []
i = 0
arr.append([])

#convert to a 2D arr
for a in tempArr:
    if a == ';':
        arr.append([])
        i+=1
    else:
        arr[i].append(a)

arr.remove([])

"""
for a in range(len(arr)):
    for s in range(2,len(arr[a])):
        if len(arr[a][s]) == 2: arr[a][s] = '0'+arr[a][s]+'0'
"""

for a in arr:
    a[0] = int(a[0])

outArr = []
for a in arr:
    while len(outArr) < a[0]:
        outArr.append([])
    outArr[a[0]-1].append(a[1])
    for s in range(2,len(a)):
        outArr[a[0]-1].append([])
        #outArr[a[0]-1][s-1].append([])
        for c in a[s]:
            if c == 'F':
                for x in range(4): outArr[a[0]-1][s-1].append(True)
            elif c == 'E':
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(False)
            elif c == 'D':
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(True)
            elif c == 'C':
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(False)
            elif c == 'B':
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(True)
            elif c == 'A': 
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(False)
            elif c == '9':
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(True)
            elif c == '8':
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(False)
            elif c == '7':
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(True)
            elif c == '6':
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(False)
            elif c == '5':
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(True)
            elif c == '4':
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(False)
            elif c == '3':
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(True)
            elif c == '2':
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(True)
                outArr[a[0]-1][s-1].append(False)
            elif c == '1':
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(False)
                outArr[a[0]-1][s-1].append(True)
            elif c == '0': 
                for x in range(4): outArr[a[0]-1][s-1].append(False)

for a in outArr:
    print(outArr.index(a))
    for s in a:
        print(s)
print(outArr)

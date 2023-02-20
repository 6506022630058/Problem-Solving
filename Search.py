def sequentialSearch(alist,item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    
    return found

testlist1 = [1,2,32,8,17,19,42,13,0]
print(sequentialSearch(testlist1,3))
print(sequentialSearch(testlist1,13))














def binarySearch(alist,item):
    first = 0
    last = len(alist)-1
    found = False
    count = 0
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
        count += 1
    print(count)
    return found

testlist3 = [17,20,26,31,44,54,55,65,77,93]
testlist2 = [0,1,2,8,13,17,19,32,42]
print(binarySearch(testlist2,3))
print(binarySearch(testlist2,13))
print(binarySearch(testlist3,55))

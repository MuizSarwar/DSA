a = [2,-23,23,5]


def recursionCount(a,idx):
    if idx > len(a):
        return
    bubbleSort(a,1)
    recursionCount(a,idx+1)

def bubbleSort(a,i):
    if i < len(a):
        if a[i-1] > a[i]:
            a[i],a[i-1]=a[i-1],a[i]
        bubbleSort(a,i+1)
    else:
        return



recursionCount(a,1)
print(*a)


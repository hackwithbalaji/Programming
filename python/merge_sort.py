def merge(x, y):
    z = []
    i = j = 0
    while i<len(x) or j<len(y):
        if j == len(y):
            z.append(x[i])
            i = i+1
        elif i == len(x):
            z.append(y[j])
            j = j+1
        elif x[i] <= y[j]:
            z.append(x[i])
            i = i+1
        elif y[j] <= x[i]:
            z.append(y[j])
            j = j+1
    return z

def mergeSort(l, h, nums):
    mid = (l+h)//2
    if l < h:
        return merge(mergeSort(l, mid, nums), mergeSort(mid+1, h, nums))
    return [nums[l]]

nums = [3,1,2,5,9,4]
res=mergeSort(0, len(nums)-1, nums)
print(res)
'''#quick sort 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]

    left = []
    right = []
    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)

nums = input("Enter numbers separated by spaces: ").split()
sorted_nums = quick_sort(nums)
print("Sorted numbers:", sorted_nums)'''
'''
arr = list(map (int, input("Enter numbers separated by spaces: ").split()))

print("Before sorting :", arr)

n = len(arr)

for i in range(n):
    mi = i
    for j in range (i+1 , n):
        if arr[j]<arr[mi]:
            mi = j
    temp = arr[i]
    arr[i] = arr[mi]
    arr[mi] = temp
print("After sorting:",arr)'''


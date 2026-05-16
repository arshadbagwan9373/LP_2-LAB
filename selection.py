def sel_sort(arr):
    n = len(arr)

    for i in range(0,n):
        min_index =i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index=j
        
        arr[i],arr[min_index] = arr[min_index],arr[i]




arr = [50,70,40,60,10]
print("Before sort :\n")
print(arr)
print("After sort :\n")
sel_sort(arr)

print(arr)

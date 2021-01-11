def quiq_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        supporting = arr[0]
        left = [i for i in arr[1:] if i <= supporting]
        right = [i for i in arr[1:] if i > supporting]
        return quiq_sort(left) + [supporting] + quiq_sort(right)

print(quiq_sort([45, 45, 88, 94, 34, 23, 77, 97, 43]))


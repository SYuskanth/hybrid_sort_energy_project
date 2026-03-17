def hybrid_quick_insertion(arr, threshold=16):
    if len(arr) <= threshold:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return hybrid_quick_insertion(left, threshold) + mid + hybrid_quick_insertion(right, threshold)


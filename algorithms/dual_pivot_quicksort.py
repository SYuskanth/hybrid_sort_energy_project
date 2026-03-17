def dual_pivot_quicksort(arr):
    arr = arr.copy()

    def sort(a, low, high):
        if low < high:
            lp, rp = partition(a, low, high)
            sort(a, low, lp - 1)
            sort(a, lp + 1, rp - 1)
            sort(a, rp + 1, high)

    def partition(a, low, high):
        if a[low] > a[high]:
            a[low], a[high] = a[high], a[low]
        pivot1 = a[low]
        pivot2 = a[high]
        i = low + 1
        lt = low + 1
        gt = high - 1

        while i <= gt:
            if a[i] < pivot1:
                a[i], a[lt] = a[lt], a[i]
                lt += 1
            elif a[i] > pivot2:
                a[i], a[gt] = a[gt], a[i]
                gt -= 1
                i -= 1
            i += 1

        lt -= 1
        gt += 1
        a[low], a[lt] = a[lt], a[low]
        a[high], a[gt] = a[gt], a[high]
        return lt, gt

    sort(arr, 0, len(arr) - 1)
    return arr


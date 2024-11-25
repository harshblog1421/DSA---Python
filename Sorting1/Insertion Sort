def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):  # Start from the second element
        key = arr[i]  # The element to be inserted
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key, one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key element in its correct position
        arr[j + 1] = key


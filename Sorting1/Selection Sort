def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Start with the current index as the minimum
        for j in range(i + 1, n):
            # Find the index of the minimum element in the unsorted portion
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]

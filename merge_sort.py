"""Merge Sort - Divide and Conquer (Tasks 1 and 2)"""


def merge_sort(arr):
    # BASE CASE: an array of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # DIVIDE: split the array at the midpoint
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # CONQUER: recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # COMBINE: merge the two sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    i = j = 0

    # Compare the front elements of both halves and take the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Copy whatever remains in either half
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    test_cases = {
        "A (Unsorted)": [64, 25, 12, 22, 11, 90, 5],
        "B (Already sorted)": [1, 2, 3, 4, 5, 6, 7],
        "C (Reverse-sorted)": [9, 8, 7, 6, 5, 4, 3, 2, 1],
    }

    for name, data in test_cases.items():
        sorted_data = merge_sort(data)
        print(f"Test Case {name}")
        print(f"  Original: {data}")
        print(f"  Sorted:   {sorted_data}")
        print(f"  Correct:  {sorted_data == sorted(data)}")
        print()

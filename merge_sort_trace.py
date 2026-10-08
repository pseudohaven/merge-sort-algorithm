"""Merge Sort with execution trace (Task 3)"""


def merge_sort(arr, depth=0):
    indent = "    " * depth
    print(f"{indent}SPLIT : {arr}")

    # BASE CASE
    if len(arr) <= 1:
        print(f"{indent}BASE  : {arr} (single element, already sorted)")
        return arr

    # DIVIDE
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], depth + 1)
    right = merge_sort(arr[mid:], depth + 1)

    # COMBINE
    merged = merge(left, right)
    print(f"{indent}MERGE : {left} + {right} -> {merged}")
    return merged


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    data = [38, 27, 43, 3]
    print(f"Input: {data}\n")
    result = merge_sort(data)
    print(f"\nFinal sorted array: {result}")

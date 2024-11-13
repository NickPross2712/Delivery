def binary_search(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


array_input = input()
target_input = input()

arr = [int(num) for num in array_input.split()]
target = int(target_input)

index = binary_search(arr, target)

print(index)

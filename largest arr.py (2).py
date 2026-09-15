def second_largest(arr):
    largest = float('-inf')
    second = float('-inf')
    for num in arr:
        if num != max(arr):
            if num > largest:
                second = largest
                largest = num
            elif num > second and num != largest:
                second = num
    return second

arr = [10,20,4,45,99] 
print("second largest number is ", second _largest(arr))

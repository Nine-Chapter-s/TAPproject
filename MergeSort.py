def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # median of array --> for splitting array into 2
        left_half = arr[:mid]  # split left array
        right_half = arr[mid:] # split right array
        
        # doing recursion until len of array just 1 or 2
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        
        # using while loop while left array AND right array still have a value
        while i < len(left_half) and j < len(right_half):
            # placing smallest number on the left
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i] 
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1


        # using while loop to do only left/right array
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1



# Example of using merge sort:
list_of_numbers = [9, 0, 3, 4, 5, 7, 8, 1, 2]
merge_sort(list_of_numbers) # Sort the list_of_numbers in Ascending order
print(list_of_numbers)
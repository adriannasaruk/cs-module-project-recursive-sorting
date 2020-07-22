# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    indexA = 0
    indexB = 0
    for i, v in enumerate(merged_arr):
        if indexA >= len(arrA):
            merged_arr[i] = arrB[indexB]
            indexB += 1
        elif indexB >= len(arrB):
            merged_arr[i] = arrA[indexA]
            indexA += 1
        elif arrA[indexA] <= arrB[indexB]:
            merged_arr[i] = arrA[indexA]
            indexA += 1
        else:
            merged_arr[i] = arrB[indexB]
            indexB += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    else:
        midIndex = int(len(arr) / 2)
        left = merge_sort(arr[0:midIndex])
        right = merge_sort(arr[midIndex:])
        return merge(left, right)


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here


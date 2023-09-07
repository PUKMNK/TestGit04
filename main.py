# Sorting Algorithm Functions

# Function 1: Selection Sort
def selection_sort(arr):
    """
    Selection Sort: Sorts a list in ascending order by repeatedly selecting the minimum element and placing it
    at the beginning of the list.

    :param arr: The input list to be sorted.
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example Usage:
my_list1 = [64, 25, 12, 22, 11]
selection_sort(my_list1)
print("Selection Sort:", my_list1)  # Output: [11, 12, 22, 25, 64]

# Function 2: Selection Sort (Newer Ver.)
def selectionSort2(arr2):
    # Create a copy of the original list to keep track of the unsorted values
    unsorted_arr = arr2.copy()
    sorted_arr = []  # The new sorted list

    while unsorted_arr:  # Continue until all elements are sorted
        # Find the minimum value from the unsorted list
        min_val = min(unsorted_arr)
        # Append it to the sorted list
        sorted_arr.append(min_val)
        # Remove this value from the unsorted list
        unsorted_arr.remove(min_val)

    return sorted_arr
arr2 = [64, 25, 12, 22, 11]
sorted_array = selectionSort2(arr2)
print("Selection Sort (Newer):", sorted_array)  # [11, 12, 22, 25, 64]

# Function 3: DNA and Text Sequence
def match_sequence(dna1, dna2):
    length = min(len(dna1), len(dna2))
    match_count = 0

    for i in range(length):
        if dna1[i] == dna2[i]:
            match_count += 1

    return match_count / length

dna1 = "ATGCARUSKPAA"
dna2 = "ATGAABTSRIAMELATGAABTSRIAMEL"
similarity = match_sequence(dna1, dna2)
print(f"Similarity between '{dna1}' and '{dna2}' is: {similarity}")





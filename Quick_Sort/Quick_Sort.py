# Conquer
def Parition(array, left, right):
    pivot = array[left]
    index = right
    for j in range(right, left - 1, -1):
        if array[j] > pivot:
            array[index], array[j] = array[j], array[index]
            index -= 1
    array[index], array[left] = array[left], array[index]
    return index

# Divide array into halves
def Quick(array, left, right):
    if left < right:
        pivot = Parition(array, left, right)

        Quick(array, left, pivot - 1)
        Quick(array, pivot + 1, right)

def Quick_Sort(array):
    Quick(array, 0, len(array) - 1)

# function to print array
def Print_Array(array):
    for i in range(0, len(array)):
        print(array[i],end=" ")
    print()

array = [2, 4, 3, 1, 6, 8, 4]

Quick_Sort(array)

Print_Array(array)

# Output
# 1 2 3 4 4 6 8
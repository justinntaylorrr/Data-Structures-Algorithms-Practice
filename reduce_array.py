#Takes an array of x length and removes the first two numbers, adds them together, and adds them to the end of the list. Keeps going until array = [n]. However the first two numbers cannot be equal, if they are, one is removed so no duplicates

def reduce_array(arr):
    while len(arr) > 1:
        if arr[0] != arr[1]:
            arr.append(arr[0] + arr[1])
            arr.pop(0)
            arr.pop(0)
            
        else:
            arr.pop(1)
            

    return arr[0] if arr else None

# Example usage:

numbers = [1,3,2,3]
result = reduce_array(numbers)
print(result)

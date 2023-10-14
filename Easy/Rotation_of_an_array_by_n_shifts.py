
def leftRotation(array,n):

    n = int(input("How many shifts do you want to perform? "))

    for i in range(0,n):
        temp = array[0]
        for j in range(0,len(array)-1):
            array[j] = array[j+1]
        array[len(array)-1] = temp
    new_array = array

    print(new_array)

def rightRotation(array,n):

    n = int(input("How many shifts do you want to perform? "))

    for i in range(0,n):
        temp = array[-1]
        for j in range(len(array)-1,0, -1):
            array[j] = array[j-1]
        array[0] = temp
    new_array = array
    
    print(new_array)


def binary_search(arr, item):
    first = 0
    last = len(arr)-1
    middle = (first + last) // 2
    while(last>=first):
        if(item>arr[middle]):
            first = middle + 1
        elif(item == arr[middle]):
            print("{} is in index {}.".format(item, middle))
            break
        else:
            last = middle-1
        middle = (first + last) // 2
    if(first>last):
        print("There is no item.")

arr1 = [2,5,10,25,40,41,50,60]
binary_search(arr1,5)
binary_search(arr1,50)
binary_search(arr1, 612)

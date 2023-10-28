def sequential_search(arr, item):
    for i in range(len(arr)):
        if(arr[i] == item):
            print("{} is in index {}.".format(item, i))
            break
    else:
        print("There is no item.")


arr1 = [3,12,15,90,22,33,-3,5] # define list
sequential_search(arr1, 15)
sequential_search(arr1, 100)
sequential_search(arr1, -3)
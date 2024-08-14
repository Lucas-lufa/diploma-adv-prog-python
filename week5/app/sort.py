from re import U


def selection_sort(lt):
    """ select and swap """
    for i in range(len(lt)):
        min_index = i
        for j in range(i +1, len(lt)):
            if lt[j] < lt[min_index]:
                min_index =j
        tem = lt[i]
        lt[i] = lt[min_index]
        lt[min_index] = tem

    return lt

def bubble_sort(lt):
    n = len(lt)
    for i in range(n):
        for j in range(0,n-i-1):
            if lt[j] > lt[j+1]:
                temp = lt[j]
                lt[j] = lt[j+1]
                lt[j+1] = temp
    return lt


def insertion_sort(lt):
    """ take value and insert into the correct location in a sorted list """
    n = len(lt)
    for i in range(n):
        sort = lt[i]
        j = i - 1
        while j >= 0 and lt[j] > sort:
            lt[j + 1] = lt[j]
            j = j-1
        lt[j+1] = sort
    return lt
    

if __name__ == "__main__":
    unsorted = [50,40,10,15,60,6]
    print(selection_sort(unsorted))
    unsorted = [50,40,10,15,60,6]
    print(bubble_sort(unsorted))
    unsorted = [50,40,10,15,60,6]
    print(insertion_sort(unsorted))
import random
import time
import csv
from SortingAlgorithms import *

def ReadList():
    """
    Reads csv file row by row.
    Creates a list containing a list of each row.
    :return:
    """
    l=[]
    with open('values.txt', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            for i in range(0, len(row)):
                if row[i]=='':
                    row.pop(i)
                    break
                row[i] = int(row[i])
            l.append(row)
    print("Successfully read {} lists".format(len(l)))
    return l

def SortList(array,order):
    time_start=time.time()
    match order:
        case "reverse":
            sorted_list = SelectionSort_Reverse(array)
        case "bubble":
            sorted_list = BubbleSort(array)
        case "select":
            sorted_list = SelectionSort1(array)
        case "insert":
            sorted_list = InsertSort(array)
        case "quick":
            sorted_list = quicksort_(array)
        case "merge":
            sorted_list = mergesort(array)
        case "quick_r":
            sorted_list = quicksort_(array)[::-1]
        case _:
            print("No valid option. Quitting program..")
            exit()
    time_end=time.time()
    exec_time = time_end - time_start
    print("{}\n".format(sorted_list))
    print("Execution time {:.4f} s\n".format(exec_time))
    with open("coord.txt","a") as f:
        f.write("({},{:.4f})\n".format(len(sorted_list),exec_time))
    with open("latex.txt","a") as p:
        p.write("& {:.4f} ".format(exec_time))
    return sorted_list

def ListToFile(lest):
    with open('values.txt', 'a') as file:
        for i in range(len(lest)):
            file.write("{},".format(lest[i]))
        file.write("\n")

# SIZE SAMPLES
k = [20000,22500,25000,27500,30000,32000,35000
    ,38000,40000,45000,50000,100000,150000,200000,250000,300000,500000,1000000,1500000,2000000,2500000,3000000,3500000,
     4000000,4500000,5000000]  #Tests for recursive alg

z = [500,7000,10000,15000,20000,30000]

p = [5000,7500, 10000,12500,15000,17500,20000,22500,25000,27500,30000]

l=[1000,5000] #Misc


def ToSort(lists, order):
    for j in range(len(lists)):
        SortList(lists[j],order)


def GenerateLists(sizes):
    sort_type = input("What type of list?\n 's'- Sorted\n 'rs'- Sorted in reverse\n 'r'- Random\n")
    rang_size = input("What range for the elements?\n Empty means -k/2 to k/2, where k is the length of the list.\n")

    for i in range(len(sizes)):
        list_to_process = []
        for j in range(sizes[i]):
            if rang_size=='':
                num = random.randint(-sizes[i]//2, sizes[i]//2)
            else:
                num = random.randint(-int(rang_size),int(rang_size))
            list_to_process.append(num)
        match sort_type:
            case "s":
                print("Array to sort:{}\n".format(list_to_process))
                ListToFile(SortList(list_to_process, "quick"))
            case "rs":
                ListToFile(SortList(list_to_process, "quick_r"))
            case "r":
                ListToFile(list_to_process)
            case _:
                print("No such case. Quitting program...")
                exit()
    list_to_send = ReadList()
    return list_to_send


def main():
    while True:
        option = input("Pick option: \n[1] Generate lists (clears values.txt) \n[2] Read from file \n[3] Clear file\n")
        match option:
            case "2":
                ToSort(ReadList(),input("Select sorting algorithm.\n - bubble\n - select\n - insert\n - quick\n - merge"))
            case "1":
                with open("values.txt","w") as f:
                    f.truncate()
                # LIST SIZES
                ToSort(GenerateLists(k),input("Select sorting algorithm.\n - bubble\n - select\n - insert\n - quick\n - merge\n"))
            case "3":
                file_ = input("Select file:\n- values.txt\n- coord.txt\n- latex.txt\n ")
                with open(file_,"w") as f:
                    f.truncate()
            case _:
                print("No valid input. Quitting program.")
                break
    quit()



main()

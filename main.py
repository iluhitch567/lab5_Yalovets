def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
def ex1():
    hat_list = [1, 2, 3, 4, 5]
    hat_list[2] = int(input("Введіть ціле число для заміни середнього числа у списку: "))
    del hat_list[-1]
    print(len(hat_list))
    print(hat_list)
    print("=================================")
def ex2():
    arr = [5, 3, 10, 23, 1, 4, 3]
    print(arr)
    bubble_sort(arr)
    print(arr)
    print("=================================")

def ex3():
    arr = [1, 3, 6, 8, 3, 1, 3, 2, 2, 7, 8, 1, 3, 4, 6, 8]

    for i in range(0, len(arr), 1):
        for j in range(i+1, len(arr), 1):
            if arr[j] == arr[i]:
                del arr[j]

    print(arr)
    print("===================================")

def ex4():
        matrix = [["_" for _ in range(8)] for _ in range(8)]
        matrix[0][0] = "тура"
        matrix[7][0] = "тура"
        matrix[0][7] = "тура"
        matrix[7][7] = "тура"

        print(matrix)
        print("=================================")

ex1()
ex2()
ex3()
ex4()

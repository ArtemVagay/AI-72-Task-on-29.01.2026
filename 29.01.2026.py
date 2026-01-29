import time, random

# написать генератор куб матрицы, написать алгоритм для поиска пар значений

def geekbench(sort):
    def wrapper(*args, **kwargs):
        time1 = time.time()
        sort(*args, **kwargs)
        print("Сортировка", sort.__name__)
        print(int((time.time() - time1) * 1_000_000_000), "нн")
        print("-" * 30)
    return wrapper

matrix = [[[random.randint(0, 1000) for i in range(100)] for j in range(100)] for n in range(100)]
def main(i, _system):
    global matrix
    if _system == "hex":
        i = hex(i)
    elif _system == "oct":
        i = oct(i)
    elif _system == "bin":
        i = bin(i)
    else:
        pass
    return i

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

@geekbench
def quick_search(arr, num):
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i][j].sort()
            a = binary_search(arr[i][j], num)
            if a != -1:
                print(f"x: {n}", f"y: {j}", f"z: {i}")


@geekbench
def find_pair(arr, num):
    for i in range(len(arr)):
        for j in range(len(arr)):
            for n in range(len(arr)):
                if matrix[i][j][n] == num:
                    print(f"x: {n}", f"y: {j}", f"z: {i}")

_system = input()
for i in range(len(matrix)):
    for j in range(len(matrix)):
        for n in range(len(matrix)):
            matrix[i][j][n] = main(matrix[i][j][n], _system)

find_pair(matrix, main(2, _system))
quick_search(matrix, main(2, _system))

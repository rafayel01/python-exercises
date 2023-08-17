### 401 ###
def program_401(arr: list[float]) -> float:
    """This function returns multiply of elements between
    first and last zeros

    Args:
        arr (list[float]): List of float elements

    Returns:
        (float): multiply of elements
    """
    mul: float = 1
    first = last = None
    # finding indexes of first and last zeros
    for i in range(len(arr)):
        if (first is not None) and (arr[i] == 0):
            last = i
        if (arr[i] == 0) and (first is None):
            first = i
    # multiply elements
    for el in arr[first + 1: last]:
        mul *= el
    return mul
        

# n: int = int(input("Enter a number N: "))
# arr: list[float] = [float(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_401(arr)}")


### 402 ###
def program_402(arr: list[float], b: int, c: int) -> float:
    """
    Returning maximum element of List from elements between [b, c] interval

    Args:
        arr (list[float]): List of float elements
        b (int): first border of interval
        c (int): last border of interval

    Returns:
        float: Maximum element of List from elements between [b, c] interval
    """
    max_: None = None
    for i in range(len(arr)):
        if (max_ is None) and (b <= arr[i] <= c):
            max_ = arr[i]
        if max_ and (b <= arr[i] <= c):
            if arr[i] > max_:
                max_ = arr[i]
    return max_


# n: int = int(input("Enter a number N: "))
# b: int = int(input("Enter a number B: "))
# c: int = int(input("Enter a number C: "))
# arr: list[float] = [float(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_402(arr, b, c)}")


### 403 ###
def program_403(arr: list[float]) -> float:
    """
    Returns sum of two minimum numbers, if in array one minimum number returns minimum number

    Args:
        arr (list[float]): List of float elements

    Returns:
        float: sum of minimum numbers or minimum number
    """
    min_: float = arr[0]
    sum_: float = min_
    for i in range(len(arr)):
        if arr[i] == min_:
            sum_ += arr[i]
        elif arr[i] < min_:
            min_ = arr[i]
            sum_ = min_
    return sum_


# n: int = int(input("Enter a number N: "))
# arr: list[float] = [float(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_403(arr)}")


### 404 ###
def program_404(arr: list[float]) -> int:
    """
    Returns count of minimum numbers

    Args:
        arr (list[float]): List of float elements

    Returns:
        int: count of minimum elements
    """
    min_: float = arr[0]
    cnt: int = 1
    for i in range(len(arr)):
        if arr[i] == min_:
            cnt += 1
        elif arr[i] < min_:
            min_ = arr[i]
            cnt = 1
    return cnt


# n: int = int(input("Enter a number N: "))
# arr: list[float] = [float(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_404(arr)}")


### 405 ###
def program_405(arr: list[float]) -> tuple[float, float, float]:
    """
    Returns Maximum three numbers (Ordered)

    Args:
        arr (list[float]): List of float elements

    Returns:
        tuple[float, float, float]: Maximum three numbers
    """
    return sorted(arr)[-3:]    


# n: int = int(input("Enter a number N: "))
# arr: list[float] = [float(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_405(arr)}")

from typing import Union
### 406 ###
def program_406(arr: list[float]) -> int:
    """
    Return ind of element of maximum value of sum of digits

    Args:
        arr (list[float]): List of float elements

    Returns:
        int: ind of element of maximum value of sum of digits
    """
    sum_: int = 0
    ind: Union([int, None]) = None
    for i in range(len(arr)):
        sum_el: int = 0
        while True:
            if arr[i] // 10 == 0:
                sum_el += arr[i]
                break
            else:
                sum_el += arr[i] % 10
                arr[i] //= 10
        if sum_el > sum_:
            sum_ = sum_el
            ind = i
    return ind


# n: int = int(input("Enter a number N: "))
# arr: list[float] = [float(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_406(arr)}")


### 407 ###
def program_407(arr: list[float]) -> float:
    """
    Returns difference if array is arithmetic progression else 0

    Args:
        arr (list[float]): List of float elements

    Returns:
        float: difference if array is arithmetic progression else 0
    """
    d: float = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i + 1] - arr[i] == d:
            continue
        else:
            return 0
    return d


# n: int = int(input("Enter a number N: "))
# arr: list[float] = [float(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_407(arr)}")


### 408 ###
def program_408(arr: list[float]) -> float:
    """
    Returns difference if array is geometric progression else 1

    Args:
        arr (list[float]): List of float elements

    Returns:
        float: difference if array is geometric progression else 1
    """
    ք: float = arr[1] / arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i + 1] / arr[i] == ք:
            continue
        else:
            return 1
    return ք


# n: int = int(input("Enter a number N: "))
# arr: list[float] = [float(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_408(arr)}")


### 409 ###
def program_409(arr: list[int]) -> int:
    """_summary_

    Args:
        arr (list[int]): _description_

    Returns:
        int: _description_
    """
    max_prime: Union([None, int]) = None
    for el in arr:
        t: bool = True
        for i in range(2, (el // 2) + 1):
            if el % i == 0:
                t = False
                break

        if (max_prime is None) and t:
            max_prime = el
        elif t:
            if el > max_prime:
                max_prime = el
    return max_prime


# n: int = int(input("Enter a number N: "))
# arr: list[int] = [int(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_409(arr)}")


### 410 ###
def program_410(arr: list[float]) -> int:
    """_summary_

    Args:
        arr (list[float]): _description_

    Returns:
        int: _description_
    """
    cnt: int = 0
    t: bool = False
    for i in range(len(arr) - 1):
        if arr[i + 1] >= arr[i]:
            t = True
            continue
        else:
            if t:
                cnt += 1
                t = False
    if t:
        cnt += 1
    return cnt


# n: int = int(input("Enter a number N: "))
# arr: list[int] = [int(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_410(arr)}")

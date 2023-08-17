### 21 ###
def max_number(a: float, b: float, c: float) -> float:
    """
        Returns the max value:
        Args:
            a (float): number
            b (float): number
            c (float): number
        Returns:
            float: Max value of (a, b, c)
    """
    max_: float = a
    if b > max_:
        max_ = b
        if c > max_:
            max_ = c
            return max_
        else:
            return max_
    elif c > max_:
        max_ = c
        return max_
    else:
        return max_
    
    # version 2 
    #return max(a, b, c)

    #version 3
    # max_ = a
    # for el in (b, c):
    #    if el > max_:
    #       max_ = el
    # return max_
    

#For running 21 uncomment following code  
#a: float = float(input("Enter a number A: "))
#b: float = float(input("Enter a number B: "))
#c: float = float(input("Enter a number C: "))
#print(f"The max number of ({a}, {b}, {c}) is: {max_number(a, b, c)}")

### 23 ###
def least_one_equal_1(a: float, b: float, c: float) -> bool:
    """
        Returns True if at least one of numbers is 1 else otherwise
        Args:
            a (float): number
            b (float): number
            c (float): number
        Returns:
            bool: True if at least one of numbers is 1 else otherwise
    """
    return (a == 1) or (b == 1) or (c == 1)


#For running 23 uncomment following code  
#a: float = float(input("Enter a number A: "))
#b: float = float(input("Enter a number B: "))
#c: float = float(input("Enter a number C: "))
#print("At least one is equal to 1" if least_one_equal_1(a, b, c) else "No one is not equal to 1")

### 24 ###
def two_num_equal_2(a: float, b: float, c: float) -> bool:
    """
        Returns True if exactly two of numbers are equal 2 else otherwise
        Args:
            a (float): number
            b (float): number
            c (float): number
        Returns:
            bool: True if exactly two of numbers are equal 2 else otherwise
    """
    return ((a == 2) and (b == 2) and (c != 2)) or ((a != 2) and (b == 2) and (c == 2)) or ((a == 2) and (b != 2) and (c == 2))

#For running 23 uncomment following code  
#a: float = float(input("Enter a number A: "))
#b: float = float(input("Enter a number B: "))
#c: float = float(input("Enter a number C: "))
#print("Exactly two numbers are equal to 2" if two_num_equal_2(a, b, c) else "Exactly two numbers are not equal to 2")


### 25 ###
def is_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c >a):
        return "y=1"
    else:
        return "y=2"
    
#a: float = float(input("Enter a number A: "))
#b: float = float(input("Enter a number B: "))
#c: float = float(input("Enter a number C: "))
#print(is_triangle(a, b, c))


### 26 ###
def is_even(a, b, c):
    if (a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0):
        return 1
    else:
        return 2
    

#a: float = float(input("Enter a number A: "))
#b: float = float(input("Enter a number B: "))
#c: float = float(input("Enter a number C: "))
#print(is_even(a, b, c)) 


### 27 ###
def is_arith_prog(a, b, c):
    if (c - b) == (b - a):
        return True
    else:
        return False
    
#a: float = float(input("Enter a number A: "))
#b: float = float(input("Enter a number B: "))
#c: float = float(input("Enter a number C: "))
#print(is_arith_prog(a, b, c))

### 28 ###
def is_geo_prog(a, b, c):
    if (c / b) == (b / a):
        return True
    else:
        return False
    
#a: float = float(input("Enter a number A: "))
#b: float = float(input("Enter a number B: "))
#c: float = float(input("Enter a number C: "))
#print(is_geo_prog(a, b, c))


### 29 ###
def sort(a, b, c):
    t = [a, b, c]
    for i in range(len(t)):
        for j in range(len(t)-1):
            if t[j] > t[j+1]:
                t[j], t[j+1] = t[j+1], t[j]
    return tuple(t)


#a: float = float(input("Enter a number A: "))
#b: float = float(input("Enter a number B: "))
#c: float = float(input("Enter a number C: "))
#print(sort(a, b, c))


### 30 ###
def sort_reverse(a, b, c):
    t = [a, b, c]
    for i in range(len(t)):
        for j in range(len(t)-1):
            if t[j] < t[j+1]:
                t[j], t[j+1] = t[j+1], t[j]
    return tuple(t)


#a: float = float(input("Enter a number A: "))
#b: float = float(input("Enter a number B: "))
#c: float = float(input("Enter a number C: "))
#print(sort_reverse(a, b, c))


### 34 ###
def any_two_eq(a, b, c, d):
    if a + b != c + d:
        if a + c != b + d:
            if a + d != b + c:
                return False
        else:
            return True
    else:
        return True



#a: float = float(input("Enter a number A: "))
#b: float = float(input("Enter a number B: "))
#c: float = float(input("Enter a number C: "))
#d: float = float(input("Enter a number D: "))
#print(any_two_eq(a, b, c, d))


### 35 ###
def program_35(a, b, c, d):
    t = (a, b, c, d)
    for el in t:
        if 2*el == sum(t):
            return True
    else:
        return False
    

#a: float = float(input("Enter a number A: "))
#b: float = float(input("Enter a number B: "))
#c: float = float(input("Enter a number C: "))
#d: float = float(input("Enter a number D: "))
#print(program_35(a, b, c, d))


### 36 ###
def program_36(a, b, c, d):
    t = (a, b, c, d)
    cnt = 0
    for el in t:
        if el % 2 == 1:
            cnt += 1
        if cnt == 2:
            return 1
    else:
        return 2
    

#a: float = float(input("Enter a number A: "))
#b: float = float(input("Enter a number B: "))
#c: float = float(input("Enter a number C: "))
#d: float = float(input("Enter a number D: "))
#print(program_36(a, b, c, d))


### 51 ###
def problem_51(num):
    t = False
    if int(str(num)[-1]) == (int(str(num)[-2]) + int(str(num)[-3])):
        t = True
    return t

#num = int(input("Please Enter three digit number: "))
#print(problem_51(num))


### 52 ###
def problem_52(num):
    s_num = str(num)
    t = False
    for i in range(2):
        for j in range(i, 3):
            if s_num[i] == s_num[j]:
                t =True
    ### version two with if else ###
    #if (s_num[0] == s_num[1]) or (s_num[0] == s_num[2]) or (s_num[1] == s_num[2]):
    #    t = True

#num = int(input("Please Enter three digit number: "))
#print(problem_52(num))


### 53 ###
def problem_53(num, k):
    if num > k:
        return num / (int(str(num)[0])+int(str(num)[1])+int(str(num)[2]))
    else:
        return int(str(num)[-1]) / num
    
#num = int(input("Please Enter three digit number: "))
#k = float(input("Enter a number K: "))
#print(problem_53(num, k))


### 55 ###
def problem_55(num):
    l = []
    num2 = num
    for i in range(4):
        el = num2 // (4-i)
        l.append(el)
        num2 -= 10**(4-i)
    return min(l)

#num = int(input("Please Enter three digit number: "))
#print(problem_55(num))


### 57 ###
def program_57(num):
    l = []
    num2 = num
    for i in range(4):
        el = num2 // (4-i)
        l.append(el)
        num2 -= 10**(4-i)
    return l[2] + l[1] if num > 300 else l[0] / l[2]


#num = int(input("Please Enter three digit number: "))
#print(problem_57(num))


### 59 ###
def program_59(num):
    l = []
    for i in range(3):
        el = num // (3-i)
        l.append(el)
        num -= 10**(3-i)
    for _ in range(len(l)):
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
    print(l)


#num = int(input("Please Enter three digit number: "))
#program_59(num)


### 61 ###
def program_61(num):
    t = False
    l = []
    for i in range(4):
        el = num // (4-i)
        l.append(el)
        num -= 10**(4-i)
    if l[0] + l[1] == l[2] + l[3]:
        t = True
    return t


#while True:
#    num = int(input("Please Enter four digit number: "))
#    if len(str(num)) == 4:
#        break
#print(program_61(num))



### 63 ###
def program_63(num):
    l = []
    for i in range(4):
        el = num // (4-i)
        l.append(el)
        num -= 10**(4-i)
    if  1 in l:
        return 1
    else:
        return 0
    
#while True:
#    num = int(input("Please Enter four digit number: "))
#    if len(str(num)) == 4:
#        break
#print(program_63(num))


### 65 ###
def program_65(num):
    l = []
    for i in range(4):
        el = num // (4-i)
        l.append(el)
        num -= 10**(4-i)
    if l[-1]*l[-2] == 12:
        return "y=12"
    else:
        return "y=0"


#while True:
#    num = int(input("Please Enter four digit number: "))
#    if len(str(num)) == 4:
#        break
#print(program_65(num))


### 67 ###
def program_67(num):
    l = []
    for i in range(4):
        el = num // (4-i)
        l.append(el)
        num -= 10**(4-i)
    if sum(l)**2 == num:
        return "YES"
    else:
        return "NO"
    

#while True:
#    num = int(input("Please Enter four digit number: "))
#    if len(str(num)) == 4:
#        break
#print(program_67(num))


### 69 ###
def program_69(num):
    l = []
    y = 0
    for i in range(4):
        el = num // (4-i)
        l.append(el)
        num -= 10**(4-i)
    if sum(l) > 20:
        y = 1
    print(y)

#while True:
#    num = int(input("Please Enter four digit number: "))
#    if len(str(num)) == 4:
#        break
#program_69(num)


import math
### 71 ###
def program_71(x):
    return math.tan(2*x+x*x)


#x = [el/10 for el in range(24, 76, 2)]
#print(list(map(program_71, x)))


### 73 ###
def program_73():
    return [(x/10+1)**2 for x in range(75, 125, 2)]

#print(program_73())


from queue import Queue
### 75 ###
def program_75():
    x = -math.pi
    queue = Queue(maxsize=20)
    while x <= math.pi:
        queue.put(math.sin(x)**2+math.cos(x))
        x += math.pi/8
    #return queue
    for item in range(queue.qsize()):
        print(queue.get())

#program_75()
    
'''
a = 15
b = [1,2,3,4,10,11]
d = {}
for i in range(len(b)):
    sub = a - b[i]
    try:
        if d.get(sub):
            print(sub, b[i])
            break
    except:
        pass
    finally:
        d[b[i]] = i
'''

### 76 ###
def program_76():
    return [x*x+4*x**8 if x > 0 else 0 for x in range(-5, 6, 2)]

#print(program_77())


### 79 ###
def program_79():
    return [math.log2(x)/2 if x > 1 else -9 for x in range(-4, 6)]

#print(program_79())


### 151 ###
def program_151(n: int) -> None:
    q = Queue()
    for i in range(1, n//2 + 1):
        if n % i == 0:
            q.put(i)
    s = 0
    for _ in range(q.qsize()):
        s += q.get()
    print(s)

#while 1:
#    n = int(input("Enter a number(Integer): "))
#    if isinstance(n, int):
#        break
#program_151(n)


### 153 ###
def program_153(n: int) -> float:
    s = 0
    for i in range(1, n - 1):
        if n % i == 2:
            s += i
    print(s)


#while 1:
#    n = int(input("Enter a number(Integer): "))
#    if isinstance(n, int):
#        break
#program_153(n)


### 155 ###
def program_155() -> None:
    s = 0
    for i in range(12, 100):
        if i % 3 == 0:
            s += i
    print(s)
    #print(sum([x for x in range(12, 100) if x % 3 == 0]))


#program_155()


### 157 ###
def program_157() -> None:
    s = 0
    for i in range(11, 100):
        if i % 5 != 0:
            s += i
    print(s)
    #print(sum([x for x in range(11, 100) if x % 5 != 0]))


#program_157()


### 159 ###
def program_159():
    p = 1
    for i in range(100, 1000):
        if (i % 3 == 1) and (i % 4 == 2):
            p *= i
    print(p)


#program_159()


### 161 ###
def program_161():
    for i in range(1000, 10000):
        if int(math.sqrt(i*26)) - math.sqrt(i*26) == 0:
            print(i)
            break


#program_161()


### 164 ###
def program_164(n):
    for i in range(100, 1000):
        if math.sqrt(i) > n:
            print(i)
            break

#n = int(input("Enter a number: "))
#program_164(n)


### 165 ###
def program_165(n):
    t = False
    p = 0
    while True:
        if 3 ** p == n:
            t = True
            break
        elif 3 ** p > n:
            break
        p += 1
    print(t)

#n = int(input("Enter a number: "))
#program_165(n)


### 167 ###
def program_167(x):
    y = False
    n = 1
    while n <= 30:
        if math.sin(x**n) < 0:
            y = True
            break
        n += 1
    print(y)

#x = float(input("Enter a number: "))
#program_167(x)


### 169 ###
def program_169(x, y):
    thresh = math.sqrt(x+y)
    z = 5
    num = 2
    while num <= thresh:
        if (x+y) % num == 0:
            z = 6
            break
        num += 1
    print(z)

#x = int(input("Enter a number X: "))
#y = int(input("Enter a number Y: "))
#program_169(x, y)


### 171 ###
# Recursion
def program_171(n):
    return 1 if n == 1 else n * program_171(n-1)

#Reduce
from functools import reduce
def program_171_v2(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

#print(f"N! = {program_171(5)}")
#print(f"N! = {program_171_v2(5)}")


### 173 ###
def program_173(a, b, n):
    h = (b - a)/n
    print(f"H = {h}")
    coord = a
    while coord <= b:
        print(coord, end = " ")
        coord += h
    

#a = float(input("Enter a number A: "))
#b = float(input("Enter a number B: "))
#n = int(input("Enter a number N: "))
#program_173(a, b, n)


### 175 ###
def program_175(n):
    x = 1
    print(x, end=" ")
    i = 1
    while i <= n:
        x = (x + 1)/i
        print(x, end=" ")
        i += 1
    print("\n")


#n = int(input("Enter a number N(N>0): "))
#program_175(10)

from typing import NoReturn
from array import array
### 177 ###
def program_177(n) -> NoReturn:
    arr = array('d', [0]*n)
    arr[0] = 1
    arr[1] = 2
    i = 2
    while i < n:
        arr[i] = (arr[i-2] + 2*arr[i-1]) / 3
        i += 1
    print(arr) 


#program_177(10)

### 179 ###
def divmod_with_plus_minus(n: float, k: float) -> tuple[(int, float)]:
    """Returns N // K and N % K using only +-"""
    div = 0
    while n > k:
        div += 1
        n -= k
    mod = n
    return (div, mod)

#n = float(input("Enter a number N: "))
#k = float(input("Enter a number K: "))
#print(divmod_with_plus_minus(n, k))


### 181 ###
def log2(n: int) -> int:
    return math.log2(n)
    #v2
    #cnt = 0
    #while 2 ** cnt < n:
    #    cnt += 1
    #return cnt

#n = float(input("Enter a number N: "))
#print(log2(n))


### 182 ###
def biggest_square_number_until_N(n: int) -> int:
    k = 1
    while (k+1)**2 <= n:
        k += 1
    return k


#n = float(input("Enter a number N: "))
#print(biggest_square_number_until_N(n))


### 183 ###
def smallest_k_for_condition(n: int) -> int:
    k: int = 1
    while 3**k <= n:
        k += 1
    return k

#n = float(input("Enter a number N: "))
#print(smallest_k_for_condition(n))


### 185 ###
def deposit(p: float) -> int:
    start: float = 30000
    month: int = 0
    while start <= 100000:
        month += 1
        start *= (100 + p)/100
    return (month, round(start, 2))


#p = float(input("Enter a deposit percentage P: "))
#print(deposit(p))


### 187 ###
def is_prime(num: int) -> bool:
    t = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            t = False
            break
    return t


# num = int(input("Enter a number: "))
#print(is_prime(num))


### 189 ###
def first_big_fib_number_after_N_th(n: int) -> int:
    a: int = 1 
    b: int = 1
    while b <= n:
        a, b = b, b+a
    return b

#n = int(input("Enter a number: "))
#print(first_big_fib_number_after_N_th(n))


### 191 ###
def sum_sequence(n, x):
    return sum((x**i for i in range(n+1)))

#n = int(input("Enter a number N: "))
#x = float(input("Enter a number X: "))
#print(sum_sequence(n, x))


### 193 ###
def sum_of_factorials(n: int) -> int:
    sum_ = 0
    p = 1
    for i in range(1, n + 1):
        p *= i
        sum_ += p
    return sum_


#n = int(input("Enter a number N: "))
#print(sum_of_factorials(n))


### 195 ### 
def sum_of(n: int, x: float) -> float:
    sum_ = 0
    p = 1
    for i in range(0, n + 1):
        if i == 0:
            p = 1
        else:
            p *= i 
        sum_ += x**i/p
    return sum_


#n = int(input("Enter a number N: "))
#x = float(input("Enter a number X: "))
#print(sum_of(n, x))


### 197 ###
def sum_of_even(n: int, x: float) -> float:
    sum_ = 0
    p = 1
    for i in range(0, n + 1):
        if i == 0:
            p = 1
        elif i == 1:
            p = 2
        else:
            print(i, (2*i-1), (2*i), (2*i-1)*(2*i))
            p *= (2*i-1)*(2*i) 
        sum_ += (-1)**i * x**(2 * i)/p
    return sum_


#n = int(input("Enter a number N: "))
#x = float(input("Enter a number X: "))
#print(sum_of_even(n, x))


### 199 ###
def sum_of_seq(n: int, x: float) -> float:
    return sum(((-1)**(i)*x**(2*i+1)/(2*i+1) for i in range(n + 1)))

#n = int(input("Enter a number N: "))
#x = float(input("Enter a number X: "))
#print(sum_of_seq(n, x))


### 200 ###
def sum_of_long(n: int, x: float) -> float:
    ham = 1
    hayt = 2
    sum_ = 1
    for i in range(1, n + 1):
        sum_ +=(-1)**(i-1) * ham * x**i/hayt   
        print(sum_)
        ham *= (2 * (i + 1) - 3)
        hayt *= 2 * (i + 1)
    return sum_


#n = int(input("Enter a number N: "))
#x = float(input("Enter a number X: "))
#print(sum_of_long(n, x))


### 201 ### // %
def cnt_of_num_digits(num: int) -> int:
    """DocString"""
    cnt = 0
    while num > 0:
        if num // 10**cnt > 0:
            cnt += 1
        else:
            break
    return cnt

#num = int(input("Enter a number: "))
#print(f"Number of digits in number: {cnt_of_num_digits(num)}")


### 203 ### 
def mul_of_number_digits(num: int) -> int:
    p: int = 1
    if num // 10 == 0:
        return num
    else:
        while num > 0:
            if num // 10 == 0:
                p *= num 
                break
            else:
                p *= num % 10
                num //= 10
    return p


#num = int(input("Enter a number: "))
#print(f"Number of digits in number: {mul_of_number_digits(num)}")

from typing import Sequence, Deque
from collections import deque
### 205 ###
def number_digits_left_to_right(num: int) -> Deque:
    dq = deque()
    if num // 10 == 0:
        dq.append(num)
    else:
        while num > 0:
            if num // 10 == 0:
                dq.append(num) 
                break
            else:
                dq.append(num % 10)
                num //= 10
    return dq

#num = int(input("Enter a number: "))
#digits = number_digits_left_to_right(num)
#while True:
 #   if digits:
 #       print(digits.pop(), end="  ")
 #   else:
 #       print("\n")
 #       break
#print(f"Digits in number from left to right: {[digits.pop() for _ in range(len(digits))]}")


### 206 ###
def number_digits_right_to_left(num: int) -> Deque:
    dq: Deque = deque()
    if num // 10 == 0:
        dq.append(num)
    else:
        while num > 0:
            if num // 10 == 0:
                dq.append(num) 
                break
            else:
                dq.append(num % 10)
                num //= 10
    
    res = 0
    for i in range(len(dq), 0, -1):
        res += 10**(i-1) * dq.popleft()

    return res

#num = int(input("Enter a number: "))
#print(number_digits_right_to_left(num))


### 207 ###
def digit_in_number(num: int) -> bool:
    t = False
    if num // 10 == 0 :
        if num == 2:
            t = True
            return t
    if num >= 10:
        while num > 0:
            if num % 10 == 2:
                t = True
                break
            else:
                num //= 10
                
    return t

#num = int(input("Enter a number: "))
#print(two_in_number(num))



### 209 ###
def odd_in_number(num: int) -> bool:
    t: bool = False
    if num // 10 == 0 :
        if num % 2 == 1:
            t = True
            return t
    if num >= 10:
        while num > 0:
            if (num % 10) % 2 == 1:
                t = True
                break
            else:
                num //= 10
                
    return t


#num = int(input("Enter a number: "))
#print(odd_in_number(num))


### 210 ###
def odd_eq_even(num: int) -> bool:
    odd_sum: int = 0
    even_sum: int = 0
    ind: int = 0
    if num // 10 == 0:
        return False
    else:
        while num > 0:
            if num // 10 == 0:
                if ind % 2 == 0:
                    even_sum += num % 10
                    num //= 10
                else:
                    odd_sum += num % 10
                    num //= 10
            else:
                if ind % 2 == 0:
                    even_sum += num % 10
                    num //= 10
                    ind += 1
                else:
                    odd_sum += num % 10
                    num //= 10
                    ind += 1    
    return odd_sum == even_sum

#num = int(input("Enter a number: "))
#print(odd_eq_even(num))


### Arrays ###
### 211 ###
def mean(lst: list) -> float:
    _sum: float = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            _sum += lst[i]
    return _sum
    ### version 2
    #return sum(el for el in lst if el > 0)
    

#lst: list = [-51, 1, -23, 4, 87, 0]
#print(mean(lst))


### 213 ###
def mean_square(lst: list) -> float:
    return sum(el*el for el in lst if el < 0)/len(lst)

#lst: list = [-51, 1, -23, 4, 87, 0]
#print(mean_square(lst))


### 215 ###
def even_ind_sum(lst: list) -> float:
    sum_: float = 0
    for i in range(0, len(lst), 2):
        sum_ += lst[i]
    return sum_

# n: int = int(input("Enter a number of elements: "))
# tup: tuple = tuple(float(input(f"Enter a element [{i}]: ")) for i in range(n))
# print(even_ind_sum(tup))


### 217 ###
def odd_ind_sum(tup: tuple) -> float:
    p: float = 1
    for i in range(1, len(tup), 2):
        p *= tup[i]
    return p


#n: int = int(input("Enter a number of elements: "))
#tup: tuple = tuple(float(input(f"Enter a element [{i}]: ")) for i in range(n))
#print(odd_ind_sum(tup))


from array import array
### 219 ###
def cnt_of_k_ind(arr: array, k: int) -> int:
    return (len(arr) - 1) // k + 1


# k: int = int(input("Enter a number K: "))
# n: int = int(input("Enter a number of elements: "))
# arr: array = array('d', [float(input(f"Enter a element [{i}]: ")) for i in range(n)])
# print(f"Result: {cnt_of_k_ind(arr, k)}")


### 221 ###
def sum_of_interval_a_b(arr: array, a: float, b: float) -> float:
    return sum(el for el in arr if (el >= a) and (el <= b))


#a: int = int(input("Enter a number A: "))
#b: int = int(input("Enter a number B(B>=A): "))
#n: int = int(input("Enter a number of elements: "))
#arr: array = array('d', [float(input(f"Enter a element [{i}]: ")) for i in range(n)])
#print(f"Result: {sum_of_interval_a_b(arr, a, b)}")


### 225 ###
def mul_el(tup: tuple, t: float) -> float:
    p: float = 1
    for i in range(len(tup)):
        if abs(tup[i]) < t:
            p *= tup[i]
    return p


#t: float = float(input("Enter a number T: "))
#n: int = int(input("Enter a number of elements: "))
#tup: tuple = tuple(float(input(f"Enter a element [{i}]: ")) for i in range(n))
#print(mul_el(tup, t))


### 230 ###
def mean_square_k(tup: tuple, k: int) -> float:
    sum_: float = 0
    cnt: int = 0
    for i in range(len(tup)):
        if int(tup[i]) % k == 0:
            sum_ += tup[i]**2
            cnt += 1
    return sum_ / cnt


# k: int = int(input("Enter a number K: "))
# n: int = int(input("Enter a number of elements: "))
# tup: tuple = tuple(float(input(f"Enter a element [{i}]: ")) for i in range(n))
# print(f"Result: {mean_square_k(tup, k)}")


from typing import TypeVar
from functools import reduce
from operator import mul

T = TypeVar('T', list[int], tuple[int], array, range)
### 233 ###
def mul_sum_even_el_arr(seq: T) -> tuple[int, int]:
    sum_: int = 0
    p: int = 1
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            sum_ += seq[i]
            p *= seq[i]
    return (sum_, p)


# n: int = int(input("Enter a number of elements: "))
# tup: tuple = tuple(int(input(f"Enter a element [{i}]: ")) for i in range(n))
#print(f"Result: {mul_sum_even_el_arr(range(1, 11))}")


### 239 ###
def div_on_five(seq: T) -> float:
    sum_: int = 0
    cnt: int = 0
    for i in range(len(seq)):
        if seq[i] % 5 == 0:
            sum_ += seq[i] ** 2
            cnt += 1
    return sum_ / cnt

#n: int = int(input("Enter a number of elements: "))
#tup: tuple = tuple(int(input(f"Enter a element [{i}]: ")) for i in range(n))
#print(f"Result: {div_on_five(tup)}")

import math
### 246 ###
def mean_of_el_if_el_square_of_number(seq: T) -> float:
    sum_: int = 0
    cnt: int = 0
    for i in range(len(seq)):
        if math.sqrt(seq[i]) == int(math.sqrt(seq[i])):
            sum_ += seq[i]
            cnt += 1
    return sum_ / cnt



# n: int = int(input("Enter a number of elements: "))
# tup: tuple = tuple(int(input(f"Enter a element [{i}]: ")) for i in range(n))
# print(f"Result: {mean_of_el_if_el_square_of_number(tup)}")


### 250 ###
def mul_of_elem(seq: T) -> int:
    p: int =1
    for i in range(len(seq)):
        if (seq[i] * i) % 3 == 2:
            p *= seq[i] ** 2
    return p

# n: int = int(input("Enter a number of elements: "))
# tup: tuple = tuple(int(input(f"Enter a element [{i}]: ")) for i in range(n))
# print(f"Result: {mul_of_elem(tup)}")


### 253 ###
def sum_of_min_max(lst: list) -> float:
    min_: float = lst[0]
    max_: float = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_:
            min_ = lst[i]
        elif lst[i] > max_:
            max_ = lst[i]
    return min_ + max_


#lst = [1, 2, 4, 7, 8, 9, 5]
#print(sum_of_min_max(lst))


### 256 ###
def sum_of_min_ind(tup: tuple) -> float:
    min_: float = tup[0]
    ind: int = 0
    for i in range(1, len(tup)):
        if tup[i] < min_:
            min_ = tup[i]
            ind = i
    return min_ + ind


#n: int = int(input("Enter a number of elements: "))
#tup: tuple = tuple(int(input(f"Enter a element [{i}]: ")) for i in range(n))
#print(f"Result: {sum_of_min_ind(tup)}")


### 260 ###
def last_min(tup: tuple) -> float:
    max_: float = tup[0]
    ind: int = 0
    for i in range(1, len(tup)):
        if tup[i] > max_:
            max_ = tup[i]
            ind = i
    return ind


#n: int = int(input("Enter a number of elements: "))
#tup: tuple = tuple(int(input(f"Enter a element [{i}]: ")) for i in range(n))
#print(f"Result: {last_min(tup)}")


### 261 ###
def mul_of_mean_square_of_arrs(X: tuple, Y: tuple) -> float:
    return (sum(X) / len(X)) * (sum(Y) / len(Y))


# n: int = int(input("Enter a number of elements: "))
# X: tuple = tuple(int(input(f"Enter a element X[{i}]: ")) for i in range(n))
# Y: tuple = tuple(int(input(f"Enter a element Y[{i}]: ")) for i in range(n))
# print(f"Result: {mul_of_mean_square_of_arrs(X, Y)}")


### 263 ###
def num_of_pos_el(X: tuple, Y: tuple) -> int:
    cnt: int = 0
    for i in range(len(X)):
        if (X[i] > 0) and (Y[i] > 0):
            cnt += 2
        elif (X[i] > 0) or (Y[i] > 0):
            cnt += 1
    return cnt

# n: int = int(input("Enter a number of elements: "))
# X: tuple = tuple(int(input(f"Enter a element X[{i}]: ")) for i in range(n))
# Y: tuple = tuple(int(input(f"Enter a element Y[{i}]: ")) for i in range(n))
# print(f"Result: {num_of_pos_el(X, Y)}")


### 266 ###
def arr_odd_minus_even(X: tuple, Y: tuple) -> float:
    odd_sum: float = 0
    even_sum: float = 0
    for i in range(len(X)):
        if X[i] % 2 == 1:
            odd_sum += X[i]
        if Y[i] % 2 == 0:
            even_sum += Y[i]
    return odd_sum - even_sum

# n: int = int(input("Enter a number of elements: "))
# X: tuple = tuple(int(input(f"Enter a element X[{i}]: ")) for i in range(n))
# Y: tuple = tuple(int(input(f"Enter a element Y[{i}]: ")) for i in range(n))
# print(f"Result: {arr_odd_minus_even(X, Y)}")

        

### 269 ###
def even_ind_plus_odd_ind(X: tuple, Y: tuple) -> float:
    return sum(X[i] for i in range(0, len(X), 2)) + sum(Y[i] for i in range(1, len(Y), 2))


# n: int = int(input("Enter a number of elements: "))
# X: tuple = tuple(int(input(f"Enter a element X[{i}]: ")) for i in range(n))
# Y: tuple = tuple(int(input(f"Enter a element Y[{i}]: ")) for i in range(n))
# print(f"Result: {even_ind_plus_odd_ind(X, Y)}")


### 271 ###
def count_of_symbol(tup: tuple[str]) -> int:
    return tup.count("a")
    # version 2
    #cnt: int = 0
    #for el in tup:
    #    if el == "a":
    #        cnt += 1
    #return cnt



#n: int = int(input("Enter a number of elements: "))
#tup: tuple[str] = tuple(input(f"Enter a element(str) X[{i}]: ") for i in range(n))
#print(f"Count of 'a': {count_of_symbol(tup)}")


### 274 ###
def mean_of_ind(tup: tuple[str]) -> float:
    ind: int = 0
    cnt: int = 0
    for i in range(len(tup)):
        if tup[i] > "h":
            ind += i**2
            cnt += 1
    return ind / cnt

#n: int = int(input("Enter a number of elements: "))
#tup: tuple[str] = tuple(input(f"Enter a element(str) X[{i}]: ") for i in range(n))
#print(f"Result: {mean_of_ind(tup)}")


import ctypes
T = TypeVar("T", tuple[str], list[str], ctypes.Array[str])
### 277 ###
def without_symbol(seq: T) -> tuple[str]:
    return tuple(el for el in seq if el != "d")


#n: int = int(input("Enter a number of elements: "))
# seq: tuple[str] = tuple(input(f"Enter a element(str) X[{i}]: ") for i in range(n))
# print(f"Result: {without_symbol(seq)}")


### 280 ###
def add_after_symbol(seq: T) -> list[str]:
    lst: list = []
    for el in seq:
        if el == "f":
            lst.append(el)
            lst.append("f")
        else:
            lst.append(el)
    return lst


# n: int = int(input("Enter a number of elements: "))
# seq: tuple[str] = tuple(input(f"Enter a element(str) X[{i}]: ") for i in range(n))
# print(f"Result: {add_after_symbol(seq)}")


### 282 ###
def create_new_list_without_zero(X: list) -> list:
    Y: list = [el for el in X if el != 0]
    return Y


# n: int = int(input("Enter a number of elements: "))
# X: list = [float(input(f"Enter a element(str) X[{i}]: ")) for i in range(n)]
# Y: list = create_new_list_without_zero(X)
# print(f"Result: {Y}")


### 289 ###
def create_new_list_in_interval_c_d(X: list, c: float, d: float) -> list:
    Y: list = [el for el in X if d > el ** 2 > c]
    return Y

# c: int = int(input("Enter a number C: "))
# d: int = int(input("Enter a number D: "))
# n: int = int(input("Enter a number of elements: "))
# X: list = [float(input(f"Enter a element(str) X[{i}]: ")) for i in range(n)]
# Y: list = create_new_list_in_interval_c_d(X, c, d)
# print(f"Result: {Y}")


### 296 ###
def program_296(X: list[int], k: int) -> list[int]:
    Y: list = [el for el in X if el % k == 2]
    return Y


# n: int = int(input("Enter a number of elements: "))
# X: list = [float(input(f"Enter a element(str) X[{i}]: ")) for i in range(n)]
# Y: list = program_296(X, c, d)
# print(f"Result: {Y}")


### 300 ###
def program_300(X: list, k: float) -> list:
    Y: list = [el for el in X if el ** 2 < k]
    return Y


# n: int = int(input("Enter a number of elements: "))
# X: list = [float(input(f"Enter a element(str) X[{i}]: ")) for i in range(n)]
# Y: list = program_300(X, c, d)
# print(f"Result: {Y}")


### 302 ###
def program_302(k: int) -> list[int]:
    lst: list = []
    for num in range(100, 1000):
        if num % 5 == 2:
            lst.append(num)
    return lst

#k: int = int(input("Enter a number K: "))
#print(program_302(k))


### 304 ###
def program_304(n: int) -> list[int]:
    lst: list = []
    num: int = 1
    while num < n - 1:
        if n % num == 2:
            lst.append(num)
            num += 1
        else:
            num += 1
    return lst

# n: int = int(input("Enter a number N: "))
# print(program_304(n))


### 306 ###
def program_306() -> list[int]:
    lst: list[int] = []
    for num in range(10, 100):
        if num // 10 + num % 10 > 5:
            lst.append(num)
    return lst


# print(program_306())


### 310 ###
def program_310() -> list[int]:
    lst: list[int] = []
    for num in range(100, 1000):
        if num % 10 == (num % 100) // 10:
            lst.append(num)
    return lst

# print(program_310())


### 311 ###
def program_311(X: list[float]) -> list[float]:
    max_: float = X[0]
    for i in range(len(X)):
        for j in range(len(X)):
            if X[i] > max_:
                max_ = X[i]
    Y: list[float] = [el + max_ for el in X if el > 0]
    return Y

# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# Y: list[float] = program_311(X)
# print(Y)


### 312 ###
def program_312(X: list[float]) -> list[float]:
    Y: list[float] = [max(X[i], X[i + 1]) if i < (len(X) - 1) else X[i] for i in range(0, len(X), 2) ]
    return Y


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# Y: list[float] = program_312(X)
# print(Y)


### 314 ###
def program_314(X: list[float]) -> list[float]:
    Y: list[float] = []
    for i in range(len(X)):
        if X[i] > 0:
            Y.extend([X[i], 0])
        else:
            Y.append(X[i])
    return Y


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# Y: list[float] = program_314(X)
# print(Y)


### 317 ###
def program_317(X: list[float]) -> list[float]:
    max_: float = X[0]
    for i in range(2, len(X), 2):
        if X[i] > max_:
            max_ = X[i]
    Y: list[float] = [X[i] + max_ for i in range(1, len(X), 2)]
    return Y


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# Y: list[float] = program_317(X)
# print(Y)


### 320 ###
def program_320(X: list[float]) -> list[float]:
    for _ in range(2):
        max_: float = X[0]
        for el in X:
            if el > max_:
                max_ = el
        X.remove(max_)
    return X


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# Y: list[float] = program_320(X)
# print(Y)
            

### 321 ###
def program_321(X: list[float]) -> list[float]:
    i: int = 0
    max_: float = X[0]
    for ind,  el in enumerate(X):
        if el > max_:
            max_ = el
            i = ind
    return [X[i] + max_ for i in range(0, i, 2)]


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# Y: list[float] = program_321(X)
# print(Y)


### 326 ###
def program_326(X: list[float]) -> list[float]:
    ### inplace ###
    #for i in range(len(X) // 2):
    #    X[i], X[len(X) - 1 - i] = X[len(X) - 1 - i], X[i]
    #return X
    ### With creation new array ###
    Y: list[float] = []
    for i in range(len(X) - 1, -1, -1):
        Y.append(X[i])
    return Y


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# Y: list[float] = program_326(X)
# print(Y)


### 327 ###
def program_327(X: list[float]) -> list[float]:
    Y: list[float] = []
    for i in range(len(X)):
        min_: float = X[0]
        for j in range(len(X)):
            if X[j] < min_:
                min_ = X[j]
        X.remove(min_)
        Y.append(min_)
    return Y


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# Y: list[float] = program_327(X)
# print(Y)


### 328 ###
def program_328(X: list[float]) -> list[float]:
    Y: list[float] = []
    while X:
        el: float = X[0]
        tmp: list[int] = [0]
        for j in range(1, len(X)):
            if X[j] == el:
                tmp.append(j)
        if len(tmp) == 1:
            Y.append(el)
        for i in range(len(tmp)):
            X.pop(tmp[i] - i)
    return Y
        
#n: int = int(input("Enter a number N: "))
#X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
#Y: list[float] = program_328(X)
#print(Y)


### 331 ###
def program_331(X: list[int]) -> list[int]:
    Y: list[int] = []
    for i in range(len(X)):
        if X[i] == 1:
            Y.append(X[i])
        else:
            for j in range(1, X[i] // 2 + 1):
                if j ** 2 == X[i]:
                    Y.append(X[i])
                    break
    return Y


#n: int = int(input("Enter a number N: "))
#X: list[int] = [int(input(f"Enter a X[{i}]: ")) for i in range(n)]
#Y: list[int] = program_331(X)
#print(Y)


### 335 ###
def program_335(X: list[float]) -> tuple[int, float]:
    max_: float = X[0] + X[2]
    el: float = X[1]
    ind: int = 1
    for i in range(2, len(X) - 1):
        if X[i - 1] + X[i + 1] > max_:
            max_ = X[i - 1] + X[i + 1]
            ind = i
            el = X[i]
    return (ind, el)


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# print(program_335(X))


### 337 ###
def program_337(X: list[float]) -> float:
    t: bool = True
    for i in range(0, len(X), 2):
        if X[i] < 0:
            t = False
            break
    if t:
        sum_: float = 0
        for i in range(1, len(X), 2):
            sum_ += X[i]
        return sum_
    else:
        return "s=1"
    
#n: int = int(input("Enter a number N: "))
#X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
#print(program_337(X))


### 341 ###
def program_341(X: list[float]) -> int:
    return len(program_328(X))


#n: int = int(input("Enter a number N: "))
#X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
#print(program_341(X))


### 350 ###
def program_350(X: list[float]) -> float:
    lst: list[int] = []
    for i in range(len(X) - 1, -1, -1):
        if X[i] > 0:
            if len(lst) == 5:
                break
            else:
                lst.append(i)
    sum_: int = 0
    for el in lst:
        sum_ += el ** 2
    return sum_ / len(lst)


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# print(program_350(X))


### 352 ###
def program_352(X: list[float]) -> float:
    for i in range(len(X)):
        if X[i] < 0:
            ind:int = i
            break
    else:
        return 0
    sum_: float = 0
    p = 1
    for j in range(ind):
        p *= X[j]        
        sum_ += p
    return sum_


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# print(program_352(X))


### 356 ###
def program_356(X: list[float]) -> int:
    cnt: int = 0
    for i in range(len(X)):
        if 2 ** i < X[i] < 2 ** (i + 1):
            cnt += 1
    return cnt


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# print(program_356(X))


### 358 ### 
def program_358(X: list[float]) -> float:  
    min_: float = 1
    ind: int = 0
    for i in range(0, len(X)):
        if min(abs(int(X[i]) - X[i]), int(X[i] + 1) - X[i]) < min_:
            min_ = min(abs(int(X[i]) - X[i]), int(X[i] + 1) - X[i])
            ind = i
    return ind


#X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(5)]
#print(program_358(X))


### 359 ###
def program_359(x: float, Y: tuple[float]) -> int:
    for i in range(1, 100):
        if Y[i - 1] < x < Y[i]:
            return i
    return "NO"


# Y: tuple[float] = tuple(1 + i * 0.25 for i in range(100))
# x: float = float(input("Enter a number X: "))
# print(program_359(x, Y))


### 363 ###
def program_363(n: int) -> list[int]:
    lst: list[int] = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            lst.append(i)
    return lst


#n: int = int(input("Enter a number N: "))
#print(program_363(n))


### 364 ###
def program_364(A: tuple[float]) -> str:
    for i in range(0, len(A) - 1):
        if (i + 2) * A[i] >  (i + 3) * A[i + 1]:
            return "NO"
    return "YES"

# n: int = int(input("Enter a number N: "))
# A: tuple[float] = tuple(1 + i * 0.25 for i in range(n))
# print(program_364(A))


### 366 ###
def program_366(A: tuple[float]) -> list[float]:
    lst: list[float] = []
    for i in range(len(A)):
        if i - 1 <=  A[i] <= i:
            lst.append(A[i])
    return lst


# n: int = int(input("Enter a number N: "))
# A: tuple[float] = tuple(1 + i * 0.25 for i in range(n))
# print(program_366(A))

from typing import Union
### 368 ###
def max_distatce_between_coords(coords: list[tuple[float, float]]) -> tuple[int, int]:
    max_: float = 0
    tup: tuple[Union(None, int), Union(None, int)] = (None, None)
    for i in range(len(coords) - 1):
        for j in range(i, len(coords)):
            if math.sqrt((coords[j][0] - coords[i][0]) ** 2 + (coords[j][1] - coords[i][1]) ** 2) > max_:
                max_ = math.sqrt((coords[j][0] - coords[i][0]) ** 2 + (coords[j][1] - coords[i][1]) ** 2)
                tup = (i, j)
    return tup


# n: int = int(input("Enter a number N: "))
# A: list[tuple[float, float]] = [(float(input(f"Enter a A[{i}] x coord: ")), float(input(f"Enter a A[{i}] y coord: "))) for i in range(n)]
# print(max_distatce_between_coords(A))


### 369 ###
def program_369(V1: list[float], V2: list) -> float:
    s1: set = set(V1)
    s2: set = set(V2)
    v1_without_v2:tuple = tuple(s1.difference(s2))
    min_: float = v1_without_v2[0]
    for i in range(1, len(v1_without_v2)):
        if v1_without_v2[i] < min_:
            min_ = v1_without_v2[i]
    return min_

from random import randint
# v1: list[float] = [randint(1, 100) for _ in range(30)]
# v2: list[float] = [randint(1, 100) for _ in range(30)]
# print(program_369(v1, v2))


### 370 ###
def sum_of_elements_at_least_two(A: list[float]) -> float:
    counter: dict = {}
    for i in range(len(A)):
        counter[A[i]] = counter.get(A[i], 0) + 1
    sum_: float = 0
    for key, value in counter.items():
        if value >= 2:
            sum_ += key
    return sum_


# lst: list[float] = [float(input(f"Enter a A[{i}]: ")) for i in range(5)]
# print(sum_of_elements_at_least_two(lst))


### 371 ###
def program_371(circle: list[tuple[float, float]]) -> float:
    min_: float = math.sqrt(circle[0][0] ** 2 + circle[0][1] ** 2)
    for i in range(1, len(circle)):
        if math.sqrt(circle[i][0] ** 2 + circle[i][1] ** 2) > min_:
            min_ = math.sqrt(circle[i][0] ** 2 + circle[i][1] ** 2)
    return round(min_, 2)


# n: int = int(input("Enter a number N: "))
# A: list[tuple[float, float]] = [(float(input(f"Enter a A[{i}] x coord: ")), float(input(f"Enter a A[{i}] y coord: "))) for i in range(n)]
# print(program_371(A))


### 372 ###
def program_372(A: list[float]) -> float:
    sum_: float = 0
    for i in range(len(A)):
        if A[i] ** 2 >= 4 * 1 * 5 / 9:
            sum_ += A[i]
    return sum_


# A: list[float] = [float(input(f"Enter a A[{i}]: ")) for i in range(90)]
# print(f"s = {program_372(A)}")


### 373 -> 370 difference between 373 only have two elements exactly ###

### 374 ###
def is_prime(num: int) -> bool:
    t: bool = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            t = False
            break
    return t

def program_374(arr: list[int]) -> tuple[int, int]:
    sum_: int = 0
    cnt: int = 0
    for el in arr:
        if is_prime(el):
            cnt += 1
            sum_ += el
    return (cnt, sum_)


# A: list[int] = [int(input(f"Enter a A[{i}]: ")) for i in range(5)]
# print(f"{program_374(A)}")


def program_375(arr: list[float]) -> bool:
    t: bool = False
    lst: list = []
    for i in range(len(arr)):
        if arr[i] == 0:
            if not lst:
                lst.append(i)
            elif lst[-1] == i - 1:
                lst.append(i)
            else:
                lst = []
            if len(lst) == 3:
                t = True
                break
    return t

# n: int = int(input("Enter a number N: "))
# A: list[int] = [int(input(f"Enter a A[{i}]: ")) for i in range(n)]
# print(f"{program_375(A)}")


def program_376() -> list[int]:
    cnt: int = 0
    num: int = 5
    lst: list[int] = []
    while True:
        lst.append(num**2 + (2 * num) ** 2)
        num += 5
        cnt += 1
        if cnt == 10:
            break
    return lst

#print(program_376())


### 377 ###
def program_377(arr: list[float]) -> float:
    t: bool = False
    sum_: float = 0
    p: float = 1
    for i in range(0, len(arr) - 1):
        if arr[i] > 0:
            sum_ += arr[i]
        elif arr[i] < 0:
            p *= arr[i]
        if i == len(arr) - 2:
            if arr[i + 1] > 0:
                sum_ += arr[i]
            elif arr[i + 1] < 0:
                p *= arr[i + 1]
             
        if arr[i] ** 2 >= arr[i+1] ** 2:
            t = True
    if t:
        return sum_
    else:
        return p
    

# n: int = int(input("Enter a number N: "))
# A: list[int] = [int(input(f"Enter a A[{i}]: ")) for i in range(n)]
# print(f"{program_377(A)}")


def sign(number: float) -> int:
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

### 378 ###
def program_378(arr: list[float]) -> float:
    t: bool = True
    sum_: float = 0
    p: float = 1
    if arr[0] >= 0:
        sign_ = 1
    elif arr[0] < 0:
        sign_ = -1
    for i in range(len(arr) - 1):
        if i % 2 == 0:
            sum_ += arr[i]
        else:
            p *= arr[i]
        if i == len(arr) - 2:
            if (i + 1) % 2 == 0:
                sum_ += arr[i + 1]
            else:
                p *= arr[i + 1]
        if sign(arr[i]) != -1 * sign(arr[i + 1]):
            t = False
    if t:
        return sum_
    else:
        return p
    

# n: int = int(input("Enter a number N: "))
# A: list[int] = [int(input(f"Enter a A[{i}]: ")) for i in range(n)]
# print(f"{program_378(A)}")


### 380 ###
def program_380(X: list[float], Y: list[float]) -> float:
    min_X: float = X[0]
    max_X: float = X[0]
    min_Y: float = Y[0]
    max_Y: float = Y[0]
    t: bool = True
    for i in range(len(X)):
        if X[i] > max_X:
            max_X = X[i]
        elif X[i] < min_X:
            min_X = X[i]
        if Y[i] > max_Y:
            max_Y = Y[i]
        elif Y[i] < min_Y:
            min_Y = Y[i]
        if X[i] not in Y:
            t = False
    if t:
        return (max_X + max_Y) / 2
    else:
        return (min_X + min_Y) / 2
    

# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# Y: list[float] = [float(input(f"Enter a Y[{i}]: ")) for i in range(n)]
# print(f"{program_380(X, Y)}")



### 382 ###
def program_382(X: list[float], Y: list[float]) -> list[float]:
    Z: list[float] = []
    for i in range(len(X)):
        if X[i] not in Y:
            Z.append(X[i])
    return Z


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# Y: list[float] = [float(input(f"Enter a Y[{i}]: ")) for i in range(n)]
# print(f"{program_382(X, Y)}")


### 384 ###
def program_384(X: list[float], Y: list[float]) -> list[float]:
    Z: list[float] = []
    for i in range(len(X)):
        if Y.count(X[i]) == 1:
            Z.append(X[i])
    return Z


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# Y: list[float] = [float(input(f"Enter a Y[{i}]: ")) for i in range(n)]
# print(f"{program_384(X, Y)}")


def program_386(X: list[float], Y: list[float]) -> list[float]:
    Z: list[float] = []
    Y_mean = reduce(lambda a, b: a + b, Y) / len(X)
    for i in range(len(X)):
        if X[i] > Y_mean:
            Z.append(X[i])
    return Z


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# Y: list[float] = [float(input(f"Enter a Y[{i}]: ")) for i in range(n)]
# print(f"{program_386(X, Y)}")


### 390 ###
def program_390(X: list[float], Y: list[float]) -> list[float]:
    Z: list[float] = []
    sum_: float = 0
    cnt: int = 0
    for el in Y:
        if el % 2 == 0:
            sum_ += el * el
            cnt += 1
    for x in X:
        if x < sum_ / cnt:
            Z.append(x)
    return Z


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# Y: list[float] = [float(input(f"Enter a Y[{i}]: ")) for i in range(n)]
# print(f"{program_386(X, Y)}")


### 392 ###
def program_392(lst: list[float]) -> list[float]:
    for i in range(len(lst) // 2):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst


# n: int = int(input("Enter a number N: "))
# X: list[float] = [float(input(f"Enter a X[{i}]: ")) for i in range(n)]
# print(f"{program_392(X)}")


### 393 ###
def program_393(arr: list[float]) -> int:
    max_: int = 0
    cnt: int = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            cnt += 1
            if cnt > max_:
                max_ = cnt
        else:
            if cnt > max_:
                max_ = cnt
            cnt = 0
    return max_

# n: int = int(input("Enter a number N: "))
# arr: list[float] = [float(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_393(arr)}")



### 394 ###
def program_394(arr: list[int]) -> list[int]:
    """DocString"""
    arr1: list[int] = []
    arr2: list[int] = []
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])
    return arr1 + arr2


# n: int = int(input("Enter a number N: "))
# arr: list[float] = [int(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_394(arr)}")


### 395 ###
def program_395(arr: list[float]) -> list[float]:
    for i in range(len(arr)):
        if arr[i] > 0:
            arr.remove(arr[i])
            break
    return arr


# n: int = int(input("Enter a number N: "))
# arr: list[float] = [float(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_393(arr)}")


### 397 ###
def program_397(arr1: list[float], arr2: list[float]) -> list[float]:
    i = j = 0
    arr: list[float] = []
    while i < len(arr1):
        while j < len(arr2):
            if arr1[i] > arr2[j]:
                arr.append(arr2[j])
                j += 1
                continue
            else:
                arr.append(arr1[i])
                i += 1
                break
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
    return arr


# n: int = int(input("Enter a number N: "))
# arr1: list[float] = [float(input(f"Enter a Arr1[{i}]: ")) for i in range(n)]
# arr2: list[float] = [float(input(f"Enter a Arr2[{i}]: ")) for i in range(n)]
# print(f"{program_397(arr1, arr2)}")


### 398 ###
def program_398(M: list[list[float]]) -> Union[set[float], str]:
    s = set(M[0])
    for i in range(1, len(M)):
        s = s.intersection(set(M[i]))
    if s:
        return s
    else:
        return "NO"
    

# n: int = int(input("Enter a number N: "))
# m: int = int(input("Enter a number M: "))
# M: list[float] = [[float(input(f"Enter a M[{i}][{j}]: ")) for i in range(n)]for j in range(m)]
# print(f"{program_398(M)}")


### 399 ###
def program_399(arr: list[float]) -> list[float]:
    ind: list[float] = []
    for i in range(1, len(arr) - 1):
        if (arr[i] == arr[i - 1]) and (arr[i] != arr[i + 1]):
            ind.append(i-1)
            ind.append(i)           
        elif (arr[i] == arr[i - 1]) and (arr[i] == arr[i + 1]):
            ind.append(i - 1)
    arr2:list[float] = []
    for i in range(len(arr)):
        if i not in ind:
            arr2.append(arr[i])
    return arr2

# n: int = int(input("Enter a number N: "))
# arr: list[float] = [float(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_399(arr)}")


from collections import namedtuple
### 400 ###
def program_400(arr: list[float]) -> tuple[float, int]:
    tup = namedtuple('tup', ['value', 'count'])
    value: list[float] = []
    cnt: int = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            value.append(arr[i])
            cnt +=1
    return tup(value, cnt)


# n: int = int(input("Enter a number N: "))
# arr: list[float] = [float(input(f"Enter a Arr[{i}]: ")) for i in range(n)]
# print(f"{program_400(arr)}")


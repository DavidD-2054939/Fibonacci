first = int(input())
second = int(input())
num = int(input())
result = []
list = []


def fibo(first, second, num):
    if num == first:
        return True
    while num >= second:
        if num == second:
            return True
        next_fib = first + second
        first = second
        second = next_fib


def numbers(num):
    while num != 0:
        list.append(num)
        if fibo(first, second, num):
            result.append(num)
            num = int(input())
        else:
            num = int(input())
    if num == 0:
        if result == [] and list != []:
            print("No valid values")
        elif result == []:
            print("No values given")
        else:
            print(len(result), "valid values:", str(result)[1:-1])

numbers(num)
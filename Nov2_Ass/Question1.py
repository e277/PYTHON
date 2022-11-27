# 1. Write a python program using a constructor to find Fibonacci numbers. (10 marks)
class Fib:
    def __init__(self):
        start, next = 0, 1
        print()
        for i in range(0, 10):
            print(start)
            start, next = next, start + next
            

fib = Fib()
fib
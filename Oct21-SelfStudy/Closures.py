# A closure is a function and an extended scope that contains free variables


# def say():
#     greet = "Hello"
#     print(hex(id(greet)))

#     # Closure
#     def display():
#         print(hex(id(greet)))
#         print(greet)

#     # display()
#     return display()

# say()
# fn = say()
# fn



def multiplier(x):
    def multiply(y):
        return x * y
    return multiply

# m1 = multiplier(1)
# m2 = multiplier(2)
# m3 = multiplier(3)

# print(m1(10))
# print(m2(10))
# print(m3(10))



# Creating all three at once
multipliers = []
for x in range(1,4):
    multipliers.append(multiplier(x))

m1, m2, m3 = multipliers

print(m1(10))
print(m2(10))
print(m3(10))
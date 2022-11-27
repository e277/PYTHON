# def netPrice(price, tax):
#     return price * (1 + tax)

# def currency(fn):
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         return f'${result}'
#     return wrapper

# netPrice = currency(netPrice) #Declaring netPrice as a Decrator
# print(netPrice(100, 0.05))

# ANOTHER WAY
from functools import wraps


def currency(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'${result}'
    return wrapper

@currency
def netPrice(price, tax):
    return price * (1 + tax)

netPrice = currency(netPrice) #Declaring netPrice as a Decrator
print(netPrice(100, 0.05))

help(netPrice)

print(netPrice.__name__)
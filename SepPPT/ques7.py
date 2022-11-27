# 1. Calculate CGST and SGST for a product and print the total price to pay {CGST = SGST = 9%}
def cal_cost():
    CGST = SGST = 0.09
    # products = []
    input_cost = float(input("Enter the items: "))
    if(input_cost):
        discount = input_cost * (CGST + SGST)
    print("Discount:", discount)
    print("Calculating cost for product...")
    cost = input_cost - discount
    return cost

if __name__ == "__main__":
    print("Cost of products:", cal_cost())

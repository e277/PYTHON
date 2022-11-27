# class FindSum:
#     def sum1(num1, num2):
#         return num1 + num2

#     def sum1(num1, num2, num3=0):
#         return num1 + num2 + num3

# obj1 = FindSum
# print(obj1.sum1(3, 7))
# print(obj1.sum1(3, 4, 7))
    

class FindArea:
    def polygon_area(self, a, b=None, c=None, d=None):
        
        #when a and c are passed as arguments
        if a != None and b != None and a != b and a != c:
            print("Area of the triangle =", (0.5 * a * b))
            
         #when a,b,c and d are passed as arguments   
        elif(b != None and c != None and d != None and a == b and a == c):
             print("Area of the square =", (a * c))
                
        elif(b == None and c == None and d == None):
            print("Enter more numbers ")
        else: 
            if(a == c):
                print("Area of the rectangle =", (a * b))
            else:
                print("Area of the rectangle =", (a * c))
        
obj = FindArea()
obj.polygon_area(19,8,77) # 76.0
obj.polygon_area(18,18,18,18) # 324
obj.polygon_area(72,38,72,38) # 2736
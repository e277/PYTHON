# single underscore “_”
# self._num1 = 2
# underscore “__”
# def __init__(self):
# Base.__init__(self)

# Access specifier

# Polymorphism
# Encapsulation
# Later ::: Data Abstraction



# Program to illustrate public access modifier in a class
class Person:
     # constructor
     def __init__(self, name, age):
           # public data members
           self.name = name
           self.age = age
 
     # public member function     
     def display_age(self):
           # accessing public data member
           print("Age: ", self.age)
 
# creating object of the class
person1 = Person("Ezra", 20)
 
# accessing public data member
print("Name: ", person1.name)
 
# calling public member function of the class
person1.display_age()


print("*" * 50)




# Program to illustrate protected access modifier in a class
# super class
class Student:
	# protected data members
	_name = None
	_roll = None
	_branch = None
	
	# constructor
	def __init__(self, name, roll, branch):
		self._name = name
		self._roll = roll
		self._branch = branch
	
	# protected member function
	def _displayRollAndBranch(self):

		# accessing protected data members
		print("Roll: ", self._roll)
		print("Branch: ", self._branch)

# derived class
class RegisteredStudent(Student):

	# constructor
	def __init__(self, name, roll, branch):
		Student.__init__(self, name, roll, branch)
		
	# public member function
	def displayDetails(self):
            # accessing protected data members of super class
            print("Name: ", self._name)
            
            # accessing protected member functions of super class
            self._displayRollAndBranch()

# creating objects of the derived class	
obj = RegisteredStudent("Ezra", 2345, "Python Developer")

# calling public member functions of the class
obj.displayDetails()


print("*" * 50)




# Program to illustrate private access modifier in a class
class Person3:
	# private members
	__name = None
	__roll = None
	__branch = None

	# constructor
	def __init__(self, name, roll, branch):
		self.__name = name
		self.__roll = roll
		self.__branch = branch

	# private member function
	def __displayDetails(self):
		# accessing private data members
		print("Name: ", self.__name)
		print("Roll: ", self.__roll)
		print("Branch: ", self.__branch)
	
	# public member function
	def accessPrivateFunction(self):
		# accessing private member function
		self.__displayDetails()

# creating object
obj = Person3("Vanessa", 3456, "Data Analyst")

# calling public member function of the class
obj.accessPrivateFunction()



print("*" * 50)



# Program to illustrate access modifiers of a class

# super class
class Super:
	# public data member
	var1 = None
	# protected data member
	_var2 = None
	# private data member
	__var3 = None
	
	# constructor
	def __init__(self, var1, var2, var3):
		self.var1 = var1
		self._var2 = var2
		self.__var3 = var3
	
	# public member function
	def displayPublicMembers(self):
		# accessing public data members
		print("Public Data Member: ", self.var1)
		
	# protected member function
	def _displayProtectedMembers(self):
		# accessing protected data members
		print("Protected Data Member: ", self._var2)
	
	# private member function
	def __displayPrivateMembers(self):
		# accessing private data members
		print("Private Data Member: ", self.__var3)

	# public member function
	def accessPrivateMembers(self):	
		# accessing private member function
		self.__displayPrivateMembers()

# derived class
class Sub(Super):

	# constructor
	def __init__(self, var1, var2, var3):
		Super.__init__(self, var1, var2, var3)
		
	# public member function
	def accessProtectedMembers(self):
            # accessing protected member functions of super class
            self._displayProtectedMembers()

# creating objects of the derived class	
obj = Sub("Hello", 1, "Ezra !")

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

# Object can access protected member
print("Object is accessing protected member:", obj._var2)

# object can not access private member, so it will generate Attribute error
# print(obj.__var3)

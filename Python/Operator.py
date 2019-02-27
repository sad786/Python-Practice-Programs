class Employee:
	def __init__(self,salary,name,city):
		self.salary = salary
		self.name = name
		self.city = city
		
	def __add__(self,other):
		self.salary = self.salary+other.salary
	def __lt__(self,other):
		return self.salary<other.salary
	def __gt__(self,other):
		return self.salary>other.salary
	def __ge__(self,other):
		return self.salary<=other.salary
	def __le__(self,other):
		return self.salary>=other.salary
	def __eq__(self,other):
		return self.salary==other.salary
	def displayInfo(self):
		print("Employee Name is ",self.name)
		print("Employee Salary is ",self.salary)
		print("Employee city is ",self.city)
		
		
emp1 = Employee(20000.00,"Saddam","Meerut")
emp2 = Employee(25000.00,'Rohit',"Mumbai")
emp1+emp2
print("*"*20)
emp1.displayInfo()
print("*"*20)
emp2.displayInfo()

if emp1<emp2:
	print("{} has less salary than {}".format(emp1.name,emp2.name))
elif emp2<emp1:
	print("{} has less salary than {}".format(emp2.name,emp1.name))
else:
	print("{} and {} has equal salary".format(emp1.name,emp2.name))

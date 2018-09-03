# Every method in a class automatically takes the instance as the first argument (eg: self)

# Employee class
class Employee:

	# Class variables
	raise_amount = 1.04
	num_of_employees = 0
	
	# This is the initialise constructor. Self refers to the instance of the class
	def __init__(self, first, last, pay):
		# Setting instance variables to passed in variables
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@company.com"
		
		# Incrementing the number of employees class variable each time an employee is added
		Employee.num_of_employees += 1
	
	# Returning fullname
	def fullname(self):
		return self.first + " " + self.last
		#return "{} {}".format(self.first, self.last)
	
	# Applying raise
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		
		
	# This is a class method
	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount
		
	# This class method can be used as an alternatice constructor, eg if employee info is given as an expected string
	@classmethod
	def from_string(cls, emp_string):
		first, last, pay = emp_string.split("-")
		return cls(first, last, pay)
		
		
	# Static methods do not automatically pass a class or instance
	@staticmethod
	def is_workday(day):
		# Python weekdays - 0 = Monday
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		
		return True


# Developer  is a subclass of employee and inherits all its variables and methods. It also has its own variables and methods that the main class does not
class Developer(Employee):
	raise_amount = 1.10

	# Init method for developer
	def __init__(self, first, last, pay, lang):
		super().__init__(first, last, pay) # This calls the main class
		self.lang = lang
		
# Subclass for manager. Passing a list of employees instead of language		
class Manager(Employee):
	raise_amount = 1.15
	
	# Init method for manager
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay) # This calls the main class
		if employees is None:
			self.employees = []
		else:
			self.employees = employees
	
	# Add employee to list
	def add_employee(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)
	# Remove employee from list
	def remove_employee(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
	# Printing employees
	def print_employees(self):
		for emp in self.employees:
			print("-->" + emp.fullname())
		
# Importing datetime		
import datetime
my_date = datetime.date(2018,8,30) # Making a python date. Year, month, day

# Employee instances	
emp1 = Employee("Lukas","vanVuuren",55000)
emp2 = Employee("Leana","Ludik",60000)


# Developers instances	
dev1 = Developer("Piet","vanVuuren",55000,"Java")
dev2 = Developer("Pompies","Ludik",60000,"Python")

manager1 = Manager("Sue","Smith",90000,[dev1,dev2])
manager1.print_employees()
manager1.add_employee(emp1)
print("")
manager1.print_employees()
manager1.remove_employee(dev1)
print("")
manager1.print_employees()


print(isinstance(manager1,Manager))
print(issubclass(Developer,Employee))
print(Employee.num_of_employees)

#print(dev1.lang)

#print(help(Developer))
#print(dev1.email)

#emp_string_1 = "John-Doe-70000"
#emp_string_2 = "Jane-Fondue-80000"
#emp_string_3 = "Piet-Pompies-90000"

#new_emp1 = Employee.from_string(emp_string_1)
#print(new_emp1.email)
#print(Employee.is_workday(my_date))
#print(emp1.pay)
#emp1.apply_raise()
#print(emp1.pay)
#emp1.raise_amount = 1.05;
#print(emp1.raise_amount)
#print(emp2.raise_amount)
#print(emp1.__dict__)
#print(Employee.__dict__)
#print(Employee.num_of_employees)
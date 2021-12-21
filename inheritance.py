#creates main class of student for a university
class Student:
    name= 'Mallory'
    email= ''
    password= ''

#creates a child class that has specific information for grad students
class grad(Student):
    degree= 'Art History'
    undergrad_college= 'UGA'

#creates a child class with specific information for undergrad students
class undergrad(Student):
    degree= 'Education'
    high_school= 'Lambert'
    grad_date= 2016

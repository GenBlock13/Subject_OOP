from Class_Uni_member import *

student1 = UniMember('Ivan', 'Petrov')
student2 = UniMember('Alex', 'Popov')

ast1 = Assistant('Petr', 'Volkov', 15500, 'geometry')
ast2 = Assistant('Maya', 'Lomova', 12500, 'economy')

student3 = Student('Vin', 'Diesel', 2500)
student4 = Student('Niki', 'Lauda', 7500)
student5 = Student('Jack', 'White', 9500)

proff_1 = Professor('Nick', 'Wayse', 25700)

print(student5.email)
student5.last_name = 'Black'
student5.change_email
print(student5.email)

stud_1 = UniMember('Ivan', 'Ivanov')

print(stud_1.full_name())

proff_1.add_assistant(student1)
proff_1.add_assistant(ast1)
proff_1.print_assist()
print(proff_1.assist_quantaty())


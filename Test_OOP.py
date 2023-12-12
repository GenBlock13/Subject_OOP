from Class_Uni_member import *

student1 = Uni_member('Ivan', 'Petrov')
student2 = Uni_member('Alex', 'Popov')


ast1 = Assistant('Petr', 'Volkov', 15500, 'geometry')
ast2 = Assistant('Maya', 'Lomova', 12500, 'economy')

student3 = Student('Vin', 'Diesel',2500)
student4 = Student('Niki', 'Lauda', 7500)
student5 = Student('Jack', 'White', 9500)

proff_1 = Professor('Nick', 'Wayse', 25700)

print(student5.email)
student5.last_name = 'Black'
student5.change_email
print(student5.email)
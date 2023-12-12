class UniMember:
    num_of_members = 0
    SEMESTER_BONUS = 1.15

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + '.' + last_name + '@uni.edu'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Assistant(UniMember):
    def __init__(self, first_name, last_name, salary, courses):
        super().__init__(first_name, last_name)
        self.salary = salary
        self.courses = courses

    def __str__(self):
        return f'Hello! My name is {self.first_name} {self.last_name}, give my {self.salary} dollars, please!'

    def __repr__(self):
        return f"Assistant('{self.first_name}', '{self.last_name}', {self.salary}, '{self.courses}')"


class Student(UniMember):
    def __init__(self, first_name, last_name, scolarship):
        super().__init__(first_name, last_name)
        self.scolarship = scolarship

    @property
    def change_email(self):
        self.email = self.first_name + '.' + self.last_name + '@uni.edu'

    def __str__(self):
        return f'Hello! My name is {self.first_name} {self.last_name}, give my {self.scolarship} dollars, please!'


class Professor(UniMember):
    def __init__(self, first_name, last_name, salary, assistants=None):
        super().__init__(first_name, last_name)
        self.salary = salary
        if assistants is None:
            self.assistants = []
        else:
            self.assistants = assistants

    def __str__(self):
        return f'Hello! My name is {self.first_name} {self.last_name}, give my {self.salary} dollars, please!'

    def add_assistant(self, assist):
        if assist not in self.assistants:
            self.assistants.append(assist)

    def delete_assistant(self, assist):
        if assist in self.assistants:
            self.assistants.remove(assist)

    def print_assist(self):
        for assist in self.assistants:
            print('My assistant is ->', assist.full_name())

    def assist_quantaty(self):
        return f'Quantaty of assistants is: {len(self.assistants)}'

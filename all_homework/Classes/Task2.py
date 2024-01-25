class Student:
    def __init__(self, name, average_ball, course=None):
        self.name=name
        self.average_ball=average_ball
        self.course=course
    def get_me_all(self):
        print (f'Имя: {self.name}\n' +
               f'Средний балл: {self.average_ball}\n' +
               f'Курс: {self.course}') #Как печально, что всё нужно вбивать рученьками :(
    def set_course(self,new_course):
        self.course = new_course
new_student = Student('Андрей', 4.4, 1)
new_student.get_me_all()
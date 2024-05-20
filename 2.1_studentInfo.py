#定义一个学生类
# 要求：
# 1.属性包括学生姓名、学号、以及语数英三科的成绩
# 2.能够设置学生某科目的成绩
# 3.能够打印出该学生的所有科目成绩

class Student:
    def __init__(self,name,stuId):
        self.name = name
        self.stuId = stuId
        self.grades = {"语文": 0,"数学": 0,"英语": 0}
    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade
    def print_grades(self):
        print(f"学生{self.name}(学号:{self.stuId})的成绩为:")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")


chen = Student("小陈","100618")
chen.set_grade("语文", 90)
chen.set_grade("数学", 95)
chen.print_grades()
# li = Student("小李","100622")
# print(chen.name)
# print(chen.stuId)
# print(chen.grades)
# print(li.name)
# print(li.stuId)


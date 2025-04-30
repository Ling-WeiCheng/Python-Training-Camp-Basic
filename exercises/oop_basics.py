"""
练习: 面向对象编程基础

描述：
在本练习中，您将学习如何定义类和创建对象，理解面向对象编程的基本概念。

请补全下面的Student类，实现相关方法。
"""

class Student:
    """学生类"""
    
    def __init__(self, name, age, grade):
        """初始化学生对象"""
        self.name = name
        self.age = age
        self.grade = grade
    
    def print_info(self):
        """打印学生信息"""
        print(f"姓名: {self.name}, 年龄: {self.age}, 成绩: {self.grade}")
    
    def is_passing(self):
        """判断学生是否通过考试"""
        return self.grade >= 60

def create_student_example():
    """创建一个Student类的实例并调用方法"""
    # 创建学生对象
    student = Student("张三", 18, 85)
    # 打印学生信息
    student.print_info()
    # 返回创建的对象
    return student
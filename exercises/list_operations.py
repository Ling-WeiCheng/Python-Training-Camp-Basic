"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 添加学生
    if operation == "add":
        if len(args) != 1:
            return "参数错误"
        student = args[0]
        if student in students:
            return "学生已存在"
        students.append(student)
        return students
    
    # 删除学生
    elif operation == "remove":
        if len(args) != 1:
            return "参数错误"
        student = args[0]
        if student not in students:
            return "学生不存在"
        students.remove(student)
        return students
    
    # 更新学生信息
    elif operation == "update":
        if len(args) != 2:
            return "参数错误"
        old_name, new_name = args
        if old_name not in students:
            return "学生不存在"
        if new_name in students:
            return "新名字已存在"
        index = students.index(old_name)
        students[index] = new_name
        return students
    
    else:
        return "操作类型错误"
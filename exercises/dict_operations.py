"""
练习: 字典操作

描述：
实现对学生成绩字典的添加、删除、修改和查询操作。

请补全下面的函数，对学生成绩字典进行各种操作。
"""

def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作
    
    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数
    
    返回:
    - 根据操作返回不同结果
    """
    # 请在下方编写代码
    # 添加学生成绩
    if operation == "add":
        if len(args) != 2:
            return "参数错误"
        name, score = args
        if name in students_dict:
            return "学生已存在"
        students_dict[name] = score
        return students_dict
    
    # 删除学生成绩
    elif operation == "remove":
        if len(args) != 1:
            return "参数错误"
        name = args[0]
        if name not in students_dict:
            return "学生不存在"
        del students_dict[name]
        return students_dict
    
    # 更新学生成绩
    elif operation == "update":
        if len(args) != 2:
            return "参数错误"
        name, new_score = args
        if name not in students_dict:
            return "学生不存在"
        students_dict[name] = new_score
        return students_dict
    
    # 查询学生成绩
    elif operation == "get":
        if len(args) != 1:
            return "参数错误"
        name = args[0]
        if name not in students_dict:
            return "学生不存在"
        return students_dict[name]
    
    else:
        return "操作类型错误"
        
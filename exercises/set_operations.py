"""
练习: 集合操作

描述：
实现两个学生集合的并集、交集和差集操作。

请补全下面的函数，对两个学生集合进行各种操作。
"""

"""
练习: 集合操作

描述：
实现两个学生集合的并集、交集和差集操作。
"""

def student_set_operations(set1, set2, operation):
    """
    对两个学生集合进行操作
    
    参数:
    - set1: 第一个学生集合
    - set2: 第二个学生集合
    - operation: 操作类型 ("union", "intersection", "difference")
    
    返回:
    - 集合操作的结果
    """
    # 检查输入是否为集合类型
    if not isinstance(set1, set) or not isinstance(set2, set):
        return "输入必须是集合类型"

    # 执行相应的集合操作
    if operation == "union":
        return set1 | set2
    elif operation == "intersection":
        return set1 & set2
    elif operation == "difference":
        return set1 - set2
    else:
        return "操作类型错误"
"""
练习: while循环

描述：
使用while循环查找列表中的第一个偶数。
"""

def find_first_even(numbers):
    """
    查找列表中的第一个偶数
    
    参数:
    - numbers: 整数列表
    
    返回:
    - 第一个偶数，如果没有找到则返回None
    """
    if not numbers:  # 处理空列表情况
        return None
        
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 == 0:  # 检查当前数字是否为偶数
            return numbers[index]
        index += 1
    
    return None  # 如果没有找到偶数
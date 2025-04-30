"""
练习: 正则表达式匹配

在本练习中，你将练习使用Python的正则表达式来处理文本匹配和提取。
"""
import re

def find_emails(text):
    """
    从文本中提取所有的电子邮件地址。
    
    参数:
        text (str): 要搜索的文本
        
    返回:
        list: 文本中找到的所有电子邮件地址的列表
    """
    # 实现你的代码: 使用正则表达式查找所有邮箱地址
    # 邮箱格式通常为: username@domain.com
    pass


import re

def find_emails(text):
    """
    从文本中提取所有的电子邮件地址。
    
    参数:
        text (str): 要搜索的文本
        
    返回:
        list: 文本中找到的所有电子邮件地址的列表
    """
    if not isinstance(text, str):
        return []
    # 邮箱正则表达式模式
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def is_valid_phone_number(phone):
    """
    验证字符串是否为有效的中国手机号码。
    """
    if not isinstance(phone, (str, int)):
        return False
    # 转换为字符串并检查格式
    phone_str = str(phone)
    pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(pattern, phone_str))

def extract_urls(text):
    """
    从文本中提取所有的URL链接。
    """
    if not isinstance(text, str):
        return []
    # URL正则表达式模式
    pattern = r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.findall(pattern, text)
"""
练习: HTTP请求

描述：
本练习帮助您学习如何使用requests库发送HTTP请求并处理响应。
注意：运行此练习前，请确保已安装requests库（pip install requests）。

请补全下面的函数，实现发送HTTP请求并处理响应的功能。
"""

import requests

def get_website_content(url):
    """
    发送GET请求获取网页内容
    
    参数:
    - url: 目标网站URL
    
    返回:
    - 包含响应信息的字典
    """
    try:
        # 发送GET请求
        response = requests.get(url)
        
        # 返回包含状态码、内容和头部信息的字典
        return {
            'status_code': response.status_code,
            'content': response.text,
            'headers': dict(response.headers)
        }
    except requests.RequestException as e:
        # 发生错误时返回错误信息
        return {
            'status_code': 0,
            'content': f"请求出错: {str(e)}",
            'headers': {}
        }

def post_data(url, data):
    """
    发送POST请求提交数据
    
    参数:
    - url: 目标网站URL
    - data: 要提交的数据字典
    
    返回:
    - 包含响应信息的字典
    """
    try:
        # 发送POST请求
        response = requests.post(url, json=data)
        
        # 尝试解析JSON响应
        try:
            response_json = response.json()
        except ValueError:
            response_json = None
        
        # 返回包含状态码、JSON响应和成功标志的字典
        return {
            'status_code': response.status_code,
            'response_json': response_json,
            'success': 200 <= response.status_code < 300
        }
    except requests.RequestException as e:
        # 发生错误时返回错误信息
        return {
            'status_code': 0,
            'response_json': None,
            'success': False
        }
import re
import os
import glob
from datetime import datetime

def wrap_math_expressions_with_div(content):
    # 处理$$...$$格式的数学表达式
    def wrap_with_div(match):
        # 获取匹配到的整个数学表达式
        math_expr = match.group(0)
        # 去除数学表达式中的空行
        math_expr = re.sub(r'\n\s*\n', '\n', math_expr)
        # 将整个数学表达式包装在<div>标签中
        return f'<div>{math_expr}</div>'
    
    # 使用正则表达式匹配$$...$$格式的数学表达式，并调用wrap_with_div函数处理
    content = re.sub(r'(\$\$.*?\$\$)', wrap_with_div, content, flags=re.DOTALL)
    
    return content

def escape_special_characters_in_inline_math(content):
    # 处理$...$格式的数学表达式，在^、_和*前面加上\
    def escape_special_characters(match):
        # 获取匹配到的整个数学表达式
        math_expr = match.group(0)
        # 在^、_和*前面加上\
        math_expr = re.sub(r'(?<!\\)([\^_\*])', r'\\\1', math_expr)
        return math_expr
    
    # 使用正则表达式匹配$...$格式的数学表达式，并调用escape_special_characters函数处理
    content = re.sub(r'(\$.*?\$)', escape_special_characters, content, flags=re.DOTALL)
    
    return content

def process_math_expressions(md_file_path):
    title = os.path.splitext(os.path.basename(md_file_path))[0]
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")
    metadata = f"""+++
title = "{title}"
date = "{current_time}+08:00"
draft = false
subtitle = ""
tags = ["笔记", "笔记1"]
categories = ["方向"]
license = '<a rel="license external nofollow noopener noreferrer" href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank">CC BY-NC 4.0</a>'
+++
"""

    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    if content.startswith('+++'):
        print(f"警告：文件 {md_file_path} 似乎已经包含元数据。跳过以避免二次添加。")
        return
    
    # 在文件内容前添加元数据
    content = metadata + content
    
    # 将$$...$$格式的数学表达式包装在<div>标签中
    content = wrap_math_expressions_with_div(content)
    
    # 在$...$格式的数学表达式中，在^、_和*前面加上\
    content = escape_special_characters_in_inline_math(content)
    
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"处理完成：文件 {md_file_path} 已更新。")

def process_all_md_files():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    md_files = glob.glob(os.path.join(script_directory, '*.md'))
    
    for md_file_path in md_files:
        process_math_expressions(md_file_path)

if __name__ == "__main__":
    process_all_md_files()

import re
import os
import glob
from datetime import datetime

def process_math_expressions(md_file_path):
    # 使用文件名（不含扩展名）作为文章标题
    title = os.path.splitext(os.path.basename(md_file_path))[0]
    # 获取当前时间，格式化为ISO 8601格式
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")
    
    # 构建要添加的元数据字符串
    metadata = f"""+++
title = "{title}"
date = "{current_time}+8:00"
draft = false
subtitle = ""
tags = ["笔记", "笔记1"]
categories = ["方向"]
license = '<a rel="license external nofollow noopener noreferrer" href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank">CC BY-NC 4.0</a>'
+++
"""
    
    # 读取 Markdown 文件
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 检查是否已经处理过
    if content.startswith('+++'):
        print(f"警告：文件 {md_file_path} 似乎已经包含元数据。跳过以避免二次添加。")
        return
    
    # 在文件内容前添加元数据
    content = metadata + content
    
    # 删除$$...$$中的空行
    def remove_empty_lines(match):
        return re.sub(r'\n\s*\n', '\n', match.group(0))
    
    content = re.sub(r'(\$\$(.*?)\$\$)', remove_empty_lines, content, flags=re.DOTALL)
    
    # 将$$ ... $$格式更改为<div>$$ ... $$</div>
    content = re.sub(r'(\$\$.*?\$\$)', r'<div>\1</div>', content, flags=re.DOTALL)
    
    # 转义$...$格式中的_, *, 和^
    def escape_characters(match):
        escaped_content = re.sub(r'(?<!\\)_', r'\_', match.group(0))
        escaped_content = re.sub(r'(?<!\\)\*', r'\*', escaped_content)
        escaped_content = re.sub(r'(?<!\\)\^', r'\^', escaped_content)
        return escaped_content
    
    content = re.sub(r'(\$.*?\$)', escape_characters, content, flags=re.DOTALL)
    
    # 保存更改
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"处理完成：文件 {md_file_path} 已更新。")

def process_all_md_files():
    # 获取脚本文件所在的目录
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # 查找目录下的所有.md文件
    md_files = glob.glob(os.path.join(script_directory, '*.md'))
    
    for md_file_path in md_files:
        process_math_expressions(md_file_path)

if __name__ == "__main__":
    process_all_md_files()

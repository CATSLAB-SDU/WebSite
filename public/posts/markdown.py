import re
import os

def process_math_expressions(md_file_name):
    # 获取脚本文件所在的目录
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # 构建 Markdown 文件的完整路径
    md_file_path = os.path.join(script_directory, md_file_name)
    
    # 读取 Markdown 文件
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 检查是否已经处理过
    if '<div>$$' in content or '/_' in content:
        print(f"警告：文件 {md_file_path} 似乎已经被处理过。跳过以避免二次转换。")
        return
    
    # 删除$$...$$中的空行
    def remove_empty_lines(match):
        return re.sub(r'\n\s*\n', '\n', match.group(0))
    
    content = re.sub(r'(\$\$(.*?)\$\$)', remove_empty_lines, content, flags=re.DOTALL)
    
    # 将$$ ... $$格式更改为<div>$$ ... $$</div>
    content = re.sub(r'(\$\$.*?\$\$)', r'<div>\1</div>', content, flags=re.DOTALL)
    
    # 转义$...$格式中的_, *, 和^
    def escape_characters(match):
        # Only escape _, *, and ^ that are not already escaped
        escaped_content = re.sub(r'(?<!\\)_', r'\_', match.group(0))
        escaped_content = re.sub(r'(?<!\\)\*', r'\*', escaped_content)
        escaped_content = re.sub(r'(?<!\\)\^', r'\^', escaped_content)
        return escaped_content
    
    content = re.sub(r'(\$.*?\$)', escape_characters, content, flags=re.DOTALL)
    
    # 保存更改
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"处理完成：文件 {md_file_path} 已更新。")

# 示例用法，文件名直接提供，无需路径
md_file_name = 'Hugo+Github搭建个人主页.md' # 你的 Markdown 文件名称
process_math_expressions(md_file_name)

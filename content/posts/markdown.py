import re

def process_math_expressions(md_file_path):
    # 读取 Markdown 文件
    with open(md_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 删除$$...$$中的空行
    def remove_empty_lines(match):
        return re.sub(r'\n\s*\n', '\n', match.group(0))
    
    content = re.sub(r'(\$\$(.*?)\$\$)', remove_empty_lines, content, flags=re.DOTALL)
    
    # 将$$ ... $$格式更改为<div>$$ ... $$</div>
    content = re.sub(r'(\$\$.*?\$\$)', r'<div>\1</div>', content, flags=re.DOTALL)
    
    # 转义$...$格式中的_
    def escape_underscores(match):
        # Only escape underscores that are not already escaped
        return re.sub(r'(?<!\\)_', r'\_', match.group(0))
    
    content = re.sub(r'(\$.*?\$)', escape_underscores, content, flags=re.DOTALL)
    
    # 保存更改
    with open(md_file_path, 'w', encoding='utf-8') as file:
        file.write(content)


# 示例用法
md_file_path = 'C:/Users/xkyin/Desktop/NTT.md' # 更改为你的 Markdown 文件路径
process_math_expressions(md_file_path)

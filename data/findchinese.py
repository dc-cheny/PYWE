import re

# only keep chinese
def find_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese

with open("wiki_jian.txt") as old_file, open("wiki_jian_ch.txt","w") as new_file:
    for line in old_file:
        cleaned_line = find_chinese(line)
        new_file.write(cleaned_line)
        new_file.write('\r\n')
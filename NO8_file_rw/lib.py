def read_file(file_path):
    lines = open(file_path, 'r', encoding='utf-8').readlines()
    return '\n'.join(lines)
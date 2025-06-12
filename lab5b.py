#!/usr/bin/env python3
# Author ID: 176512234

def read_file_string(file_name):
    try:
        f = open(file_name, 'r')
        content = f.read()
        f.close()
        return content
    except Exception:
        return ''

def read_file_list(file_name):
    try:
        f = open(file_name, 'r')
        lines = f.readlines()
        f.close()
        stripped_lines = [line.strip('\n') for line in lines]
        return stripped_lines
    except Exception:
        return []

def append_file_string(file_name, string_of_lines):
    try:
        f = open(file_name, 'a')
        f.write(string_of_lines)
        f.close()
    except Exception:
        pass

def write_file_list(file_name, list_of_lines):
    try:
        f = open(file_name, 'w')
        for line in list_of_lines:
            f.write(line + '\n')
        f.close()
    except Exception:
        pass

def copy_file_add_line_numbers(file_name_read, file_name_write):
    try:
        f_read = open(file_name_read, 'r')
        lines = f_read.readlines()
        f_read.close()

        f_write = open(file_name_write, 'w')
        for index, line in enumerate(lines, start=1):
            f_write.write(f"{index}:{line}")
        f_write.close()
    except Exception:
        pass

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))

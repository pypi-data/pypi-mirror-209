import os
import pickle as pkl
from pathlib import Path
import json


def read_text(path: str| Path) -> str:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        text = ''.join(lines)
        return text


def read_lines(path: str| Path) -> list[str]:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')
            lines[i] = lines[i].replace('\r', '')
        return lines


def write_text(path: str| Path, content: str) -> None:
    content = str(content)
    create_dir_if_not_exist(os.path.dirname(path))
    with open(path, 'w', encoding='utf-8', errors='ignore') as f:
        f.write(content)


def write_lines(path: str| Path, content: list) -> None:
    if not isinstance(content, list):
        raise TypeError('content is not list')
    create_dir_if_not_exist(os.path.dirname(path))
    text = '\n'.join(content)
    with open(path, 'w', encoding='utf-8', errors='ignore') as f:
        f.write(text)


def append_text(path: str| Path, content: str, newline=True) -> None:
    if not os.path.exists(path):
        write_text(path, '')
    content = str(content)
    if newline:
        content += '\n'
    with open(path, 'a', encoding='utf-8', errors='ignore') as f:
        f.write(content)


def append_lines(path: str| Path, content: list) -> None:
    if not isinstance(content, list):
        raise TypeError('content is not list')
    if not os.path.exists(path):
        write_text(path, '')
    with open(path, 'a', encoding='utf-8', errors='ignore') as f:
        text = '\n'.join(content)
        f.write(text)


def create_dir_if_not_exist(path: str| Path) -> None:
    if path == '':
        return
    if not os.path.exists(path):
        os.makedirs(path)


def read_csv(path: str| Path) -> list[list[str]]:
    lines = read_lines(path)
    rows:list[list[str]] = []
    for line in lines:
        rows.append(line.split(','))
    return rows


def write_csv(path: str| Path, rows: list) -> None:
    lines = []
    for row in rows:
        for i in range(len(row)):
            row[i] = str(row[i])
        line = ','.join(row)
        lines.append(line)
    write_lines(path, lines)


def write_pkl(path: str| Path, content) -> None:
    create_dir_if_not_exist(os.path.dirname(path))
    with open(path, 'wb') as f:
        pkl.dump(content, f)


def read_pkl(path: str| Path):
    with open(path, 'rb') as f:
        result = pkl.load(f)
    return result


def write_json(path: str| Path, content, indent=4) -> None:
    write_text(path, json.dumps(content, indent=indent, ensure_ascii=False, default=lambda x: x.__dict__))


def read_json(path: str| Path):
    return json.loads(read_text(path))


def main():
    s = 'hello'
    write_text('1.txt', s)
    # hello in 1.txt
    append_text('1.txt', 'world')
    # helloworld in 1.txt
    s = read_text('1.txt')
    print(s)  # helloworld

    s = ['hello', 'world']
    write_lines('1.txt', s)
    # hello\nworld in 1.txt
    append_lines('1.txt', ['\npython'])
    # hello\nworld\npython in 1.txt
    s = read_lines('1.txt')
    print(s)  # ['hello', 'world', 'python']

    os.remove('1.txt')


if __name__ == '__main__':
    main()

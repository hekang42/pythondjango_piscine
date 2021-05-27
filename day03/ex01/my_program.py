#!/usr/bin/env python3

from path import Path

def do():
    dir_path = Path('.')
    print(dir_path)
    new_path = dir_path / "text"
    print(new_path)
    if not new_path.isdir():
        new_path.mkdir()
    new_file = new_path/'file.txt'
    if not new_file.isfile():
        new_file.touch()
    new_file.write_lines(["Happy Piscine", "is Hell", "We are in Hell"])
    new_file.write_text("Where is Heaven?", append=True)
    for line in new_file.lines():
        print(line.replace('\n', ''))
if __name__ == '__main__':
    do()
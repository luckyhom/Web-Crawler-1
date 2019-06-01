import json


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def main(lists):
    for list in lists:
        print(list)
        write_to_file(list)


lists = ['a', 'b', 'c']
main(lists)

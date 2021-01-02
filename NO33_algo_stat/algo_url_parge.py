#coding=utf-8

def parse_url():
    file = 'problems.md'
    output_file = 'problems.json'
    with open(file, encoding='utf-8') as f:
        lines = f.readlines()
    lines = lines[2:]
    urls = []
    for line in lines:
        parts = line.split('|')
        urls.append([
            parts[2],
            parts[3]
            ]
        )
    print("长度是{}个".format(len(lines)))
    import json
    with open(output_file, 'w+') as f:
        f.write(json.dumps(urls))
    return urls


if __name__ == '__main__':
    ret = parse_url()
    print(ret)
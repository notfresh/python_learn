import yaml
with open('test.yml') as f:
    content = yaml.load(f)

a = [1,2,3]
print(content)
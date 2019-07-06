inv = input()

print(list(filter(lambda x: ord(x) in range(128), inv)))


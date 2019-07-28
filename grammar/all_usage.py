print(all([1, 2, 3]))
print(all([1, None, 3]))
print(all([1, [], 3]))
try:
    print(all(1, 2, 3)) #
except Exception as e:
    print(e)
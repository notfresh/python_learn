import os
from os.path import dirname


print(os.path.abspath(__file__))
print(os.path.dirname(__file__))

print(__file__)
print(type(__file__))

print(dirname(dirname(__file__)))
print(os.getcwd())
# https://www.pythontutorial.net/python-basics/python-directory/#:~:text=To%20create%20a%20new%20directory,before%20creating%20a%20new%20directory.

import os

dir = os.path.join("C:\\", "Desktop")
print(os.path.expanduser('~'))
print(dir)

if os.path.exists(dir) or os.path.isdir(dir):
    print(f'The {dir} is a directory')
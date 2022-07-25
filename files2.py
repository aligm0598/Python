from pathlib import Path
cwd = Path.cwd()

parent = cwd.parent

print('\nIs this a directory? ' + str(parent.is_dir()))

print('\nIs this a file? ' + str(parent.is_file()))

print('\n-----directory contents-----')
for child in parent.iterdir():
    if child.is_dir():
        print(child)
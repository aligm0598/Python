from pathlib import Path

cwd = Path.cwd()
print('\nCurrent Working directory:\n' + str(cwd))

new_file = Path.joinpath(cwd, 'new file.txt')
print('\nFull path\n' + str(new_file))

print('\nDoes that file exist? ' + str(new_file.exists()) + '\n')

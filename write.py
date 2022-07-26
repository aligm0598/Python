stream = open('output.txt', 'wt')

print('\nCan I write to this file? ' + str(stream.writable()) + '\n')

stream.write('H')
stream.writelines(['ello',' ','world'])
stream.write('\n')
names = ['John', 'Micheal']
stream.writelines(names)
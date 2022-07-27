try:
    stream = open('output.txt', 'wt')
    stream.write('Lorem ipsum dolar')
finally:
    stream.close

with open('output.txt', 'wt') as stream:
    stream.write('Lorem ipsum dolar')

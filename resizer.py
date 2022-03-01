from PIL import Image
import sys

try:
    fullImageFileName = sys.argv[1]

    operation = sys.argv[2]

    argument = sys.argv[3]

    if operation == '-f':

        r = fullImageFileName.split('.')

        imageFileName = r[0]

        im = Image.open(fullImageFileName)

        converted = im.convert('RGB')

        converted.save(f'{imageFileName}.{argument}')

    elif operation == '-r':
        im = Image.open(fullImageFileName)
        r = argument.split('x')
        r_tuple = (int(r[0]), int(r[1]))
        out = im.resize(r_tuple)
        out.save(f'output_{fullImageFileName}')

except:
    print('Usage:')
    print('python resizer.py [input file name] [operation] [argument]')
    print()
    print('Operations:')
    print('-f : Format image(png to jpg and vice versa)')
    print('Example 1: python resizer.py image.jpeg -f png ')
    print('Example 2: python resizer.py image.png -f jpeg ')
    print()
    print('-r : Resize image')
    print('Example 1: python resizer.py image.jpeg -r 200x200 ')
    print('Example 2: python resizer.py image.png -r 250x200 ')

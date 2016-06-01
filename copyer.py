import sys

def copy(source, destination):
    with open(source, 'rb') as f1:
        with open(destination, 'wb') as f2:
            f2.write(f1.read())

copy(sys.argv[1], sys.argv[2])

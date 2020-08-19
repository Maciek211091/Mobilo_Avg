import os

with open(r'/home/maciej/Desktop/file.txt', 'w+') as f:
    f.write('Pada deszcz i jest paskudnie')


def word_counter(source):

    with open(source, 'r') as file:
        content = file.read()
        word_count = len(content.split())
        return word_count


path = r'/home/maciej/Desktop/file.txt'

if os.path.isfile(path):

    print(word_counter(path))

else:

    raise FileNotFoundError

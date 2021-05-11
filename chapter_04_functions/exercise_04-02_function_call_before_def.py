# calling a function before it's defined to show the error it produces

repeat_lyrics()


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


# Code: http://www.py4e.com/code3/lyrics.py

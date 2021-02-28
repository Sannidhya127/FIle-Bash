from colored import fg, bg, attr


def printer(text):
    print(text)


if __name__ == '__main__':
    printer(f"{fg('46')}My name is valla{attr('reset')}")

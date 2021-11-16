def run():
    squares = [ i for i in range(1, 100000) if i % 36 == 0]
    print(squares)


if __name__ == '__main__':
    run()
def run():
    dictionary_com = [{i: i ** 2} for i in range(1, 101)]
    print(dictionary_com)

    dictionary_com = {i: i ** 2 for i in range(1, 101)}
    print(dictionary_com)


if __name__ == '__main__':
    run()

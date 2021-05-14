def read():
    numbers = []
    with open("./archivos/numbers.txt", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Facundo", "Gregorio", "Marta", "Susana", "Jose"]
    with open("./archivos/names.txt", "a") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    write()
    read()


if __name__ == '__main__':
    run()
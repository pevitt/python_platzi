import pdb

def divisors(num):
    divisors = []
    # pdb.set_trace()
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = int(input('Ingresa un número: '))
    print(divisors(num))
    another_way = [i for i in range(1, num + 1) if num % i == 0]
    print(another_way)
    print("Terminó mi programa")


if __name__ == '__main__':
    run()

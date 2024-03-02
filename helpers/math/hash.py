from random import randint

from helpers.math.prime import prime_generator

MOD_PRIME = 23


def get_hash_functions(num_rows, no_of_hash_functions=200):
    generator = prime_generator()
    cur_prime = next(generator)
    while cur_prime < num_rows:
        cur_prime = next(generator)
    hashes = []

    # all functions are same here. check this
    for i in range(no_of_hash_functions):
        coeff_1 = randint(1, 5 * cur_prime)
        constant = randint(1, 5 * cur_prime)

        def hash(x, b=coeff_1, c=constant):
            return (b * x + c) % cur_prime

        hashes.append(hash)

    return hashes


def get_hash_functions_coefficients(num_rows, no_of_hash_functions=200):
    generator = prime_generator()
    cur_prime = next(generator)
    while cur_prime < num_rows:
        cur_prime = next(generator)
    hashes = []

    # write prime first
    hashes.append([cur_prime, num_rows])

    # all functions are same here. check this
    for i in range(no_of_hash_functions):
        coeff_1 = randint(1, 5 * cur_prime)
        constant = randint(1, 5 * cur_prime)
        hashes.append([coeff_1, constant])

    return hashes


def load_hash_functions_from_coefficients(hash_coefficients):
    # all functions are same here. check this
    hashes = []
    index = 0
    for hash_coefficient in hash_coefficients:
        if index == 0:
            cur_prime = hash_coefficient[0]
            index = index + 1
        coeff_1 = hash_coefficient[0]
        constant = hash_coefficient[1]

        def hash(x, b=coeff_1, c=constant):
            return (b * x + c) % cur_prime

        hashes.append(hash)
    return hashes


if __name__ == "__main__":
    for i in range(20):
        print(i, " : ", get_hash_functions(200)[7](5))

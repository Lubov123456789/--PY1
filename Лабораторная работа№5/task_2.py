from random import sample


def get_unique_list_numbers(min: int = -10, max: int = 10,
                            length: int = 15) -> list[int]:

    rand_list = [i for i in range(min, max, 1)]

    return sample(rand_list, length)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

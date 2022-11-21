def get_unique_list_numbers() -> list[int]:
    from random import randint
    return [randint(-10,10) for _ in range(15)]
list_unique_numbers = get_unique_list_numbers()
list_ = []
for item in list_unique_numbers:
    if item not in list_:
        list_.append(item)
print(list_)

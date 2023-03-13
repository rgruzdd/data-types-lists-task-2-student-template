from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    # TODO: Add your code here
    new_list = []
    for n in range(1, n+1):
        new_n = n
        if n % 3 == 0:
            new_n = 'Fizz'
        if n % 5 == 0:
            new_n = 'Buzz'
        if n % 3 == 0 and n % 5 == 0:
            new_n = 'FizzBuzz'
        new_list.append(new_n)
    return new_list

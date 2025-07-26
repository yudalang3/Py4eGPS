from itertools import islice

def head(iterable, n):
    return islice(iterable, n)



if __name__ == '__main__':
    my_strings = "abcdefg"
    my_strings = [1,2,3,"fe","g"]
    print(head(my_strings, 3))
    for _ in head(my_strings, 5):
        print(_)
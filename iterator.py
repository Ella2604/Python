names = ("paul", "petre", "petrica")

def parcurgere_lista():
    for n in  names:
        print(n)

def iterate_iterator():
    print("iterator iteration")
    nyit = iter(names)
    print(next(nyit))
    print(next(nyit))
    print(next(nyit))


if __name__ == "__main__":
    parcurgere_lista()
    iterate_iterator()
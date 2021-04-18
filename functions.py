def sum_function(first, *rest):
    s = first + sum(rest)
    print(s)

def keywords_args(name, **kwargs):
    print(name)
    for arg in kwargs.items():
        print(arg)
        key, value = arg
        print(key + " " + value)

def multiple_values():
    return "Mihai", "Chifa", 26


#one line function

def sum_of_2(a, b):
    return a + b

#lambda

on_line_sum = lambda x, y: x+y

if __name__ == "__main__":
    sum_function(1, 2, 3, 4, 5)
    sum_function(1, 2, 3, 4, 5, 6)
    sum_function(1, 2, 3, 4, 5, 6, 7 , 8)
    sum_function(1, 2, 3, 4, 5)
    keywords_args("Mihai", prenume="ada", varsta="20")

for v in multiple_values():
    print("From for " + str(v))

    var1, var2, var3 = multiple_values()
    print(var1)

    print(on_line_sum(6,5))
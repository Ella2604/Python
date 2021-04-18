personal_info = {
    "nume": "Marius",
    "varsta": "23",
    "nota": "10"
}


def print_map():
    print("Map ")
    print(personal_info)
    print(" ")


def access_values():
    print("#4 accessing values")
    print(personal_info.values())
    print(" ")


def print_value():
    print("#2 print a value")
    print("Age: " + personal_info["varsta"])


def access_key():
    print("#3 accessing keys")
    print(personal_info.keys())

def add_values():
    print("#5 adding values")
    print("normal entry")
    print(personal_info)
    print("adding value ")
    personal_info["tara"]= "Ro"
    print(personal_info.values())

def remove_value():
    print("# remove values")
    print(personal_info)
    personal_info.pop("varsta")
    print(personal_info)

if __name__ == "__main__":
    print_map()
    print_value()
    access_key()
    access_values()
    add_values()
    remove_value()
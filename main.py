from array_list import ArrayList


def main():

    lst = ArrayList()


    print(f"expected 0 : {lst.size()}")


    lst.add("a")
    lst.add("b")
    lst.add("c")

    print(f"expected 3: {lst.size()}")
    print(f"expected 1: {lst.getIndex('b')}")


    removed = lst.remove(1)
    print(f" expected b: {removed}")
    print(f"expected 2 : {lst.size()}")
    print(f" expected c: {lst.get(1)}")
    print(f"expected -1: {lst.getIndex('b')}")


    lst.set(0, "z")
    print(f"expected z: {lst.get(0)}")


    try:

        lst.get(2)
    except IndexError:
        print("IndexError")

    try:
        lst.remove(-1)
    except IndexError:
        print("IndexError")



    full_list = ArrayList()
    for i in range(100):
        full_list.add(f"item_{i}")

    print(f"expected 100 : {full_list.size()}")

    try:

        full_list.add("Overflow")
    except OverflowError:
        print("OverflowError")



if __name__ == "__main__":
    main()
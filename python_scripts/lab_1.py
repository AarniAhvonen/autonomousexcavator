
def importing():
    global np
    global my_list

    my_list = [[1, 2, 3],[4,5,6]]

    return True


def test(i):

    global my_list

    return my_list[i]




if __name__ == '__main__':
    importing()
    test(1)



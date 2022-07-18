def c2f(tc):
    tf = (tc*9/5) + 32
    print(tf)
    return tf



def f2c(tf):
    tc = (tf-32)*(5/9)
    return tc





if __name__ == '__main__':
    c2f(37)
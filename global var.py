def my_fun(x):
    global k
    k = 11
    return c * x

def main():
    global c
    c = 5
    s = my_fun(9)
    print(s*k)
    
    

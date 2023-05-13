def addthis(x,y):
    print(f"This is x {x} and ex-type {type(x)}")
    print(f"This is y {y} and y-type {type(y)}")


    try:
        result = x + y
        return result
    except TypeError:
        print(f"The wrong type passed")
        result = int(x) + int(y)

    print(f"This is the result {result}")
    return result

print(addthis(1,"2"))
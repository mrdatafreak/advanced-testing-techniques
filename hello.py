def addthis(x,y):
    # import pdb;pdb.git staset_trace()
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

print(addthis('3',1))
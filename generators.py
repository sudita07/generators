# def cub():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#
#
# values=cub()
# print(values.__next__())
# print(values.__next__())


# a simple generator function program
def mygen():
    n=1
    print("this is printed first")
# generator function contains yield statements
    yield n

    n+=1
    print("this is printed second")
    yield n

    n+=1
    print("this is printed at last")
    yield n

for item in mygen():
    print(item)
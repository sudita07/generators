# a program to create top 10 perfect squares
def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
values=topten()
for i in values:
    print(i)
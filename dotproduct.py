#Dot product

def dot_product(vector_a: list, vector_b: list) -> list:
    empty = list()
    count = 0
    if vector_a.__len__() == vector_b.__len__():
        while count < len(vector_a):
            empty.append(vector_a[count]*vector_b[count])
            count += 1
        return empty
    else:
        raise ValueError(vector_a,' and ', vector_b,' are different sizes!') 

a = [1,2,3]
b = [2,3,5]

c = dot_product(a,b)
print(c)
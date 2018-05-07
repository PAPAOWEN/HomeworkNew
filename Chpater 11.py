#exercise1-4

#1. [10, 8, 6, 4, 2]
#2.Does this fragment create one or two turtle instances? Does setting the color of alex also change the color of tess? Explain in detail?
#It creates two turtle instances and chaging the color of alex does change the color of tess too.
#3. The snapshot beofre should look like a -->[1, 2, 3] b-->[1,2,3] After the a should look the same whereas b is changed to [5,2,3]
#4. The first one is false because even though they have the same value they are not the same object, and after "that" is assigned with the list of "this" they become the same object which allows the statement to be true.
#6. Write a function scalar_mult(s, v) that takes a number, s, and a list, v and returns the scalar multiple of v by s. :


def scalar_mult(a_list):
    new_list=[]
    for value in a_list:
        new_elem= 5 * value
        new_list.append(new_elem)

    return new_list
scalar_mult(5, [1, 2])
scalar_mult(3, [1, 0, -1])
scalar_mult(7, [3, 0, 5, 11, 2])

test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14]
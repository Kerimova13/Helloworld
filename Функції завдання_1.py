# примеры работы с функциями
# найти максимальное значение в передаваемом в функцию списке и верните его,
# если оно больше 0, в ином случае верните сообщение о том, что число меньше 0

#def function_maximum (list[]):
def function_of_maximum (x):
    max_element = x[0]
    for element in x:
        if element > max_element:
            max_element = element
    return max_element if max_element>0 else "Value <0"


a=[12,6,43,78]
max_a=function_of_maximum(a)
print(max_a)

b=[-1,-12,0,-24,-60]
max_b=function_of_maximum(b)
print(max_b)


'''This is the file where i will be learning the concepts that i don't know'''
from ipywidgets import interact
import numpy as np
w_range = np.array([0, 400])
# print(w_range)
# print(*w_range)
# w_array = np.arange(*w_range, 5)
# print(w_array)


# @interact(w=(*w_range, 10), continuous_update=False)
# def func(w=150):
#     pass

# print(type(w_range))
# print(*w_range)

# w=(*w_range,10)
# print(w)

x_train=np.array([1.0,2.0])+0
y_train=np.array([300,500])

w=150

b=100

f_wb=np.dot(w,x_train)+b
print(f_wb)
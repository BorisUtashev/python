from math import sqrt, acos, degrees
#import random

x_a = float(input())

y_a = float(input())

x_b = float(input())

y_b = float(input())

x_c = float(input())

y_c = float(input())

def compute_len(x_0,y_0,x_1,y_1):
    
    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    
    return len_line

def compute_area(a_1, a_2, a_3):
    
    p = (a_1 + a_2 + a_3) / 2
    
    area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
    
    return area

def compute_angle(a_1, a_2, a_3):
    
    angle_rad = acos((a_1 ** 2 + a_2 ** 2 - a_3 ** 2)/
                     (2 * a_1 * a_2))
    
    return degrees(angle_rad)

c = compute_len(x_a, y_a, x_b, y_b)

a = compute_len(x_b, y_b, x_c, y_c)

b = compute_len(x_a, y_a, x_c, y_c)

p = a + b + c

s = compute_area(a, b, c)    

angle_A = compute_angle(c, b, a)
    
angle_B = compute_angle(c, a, b)
    
angle_C = compute_angle(a, b, c)
    
def compute_Rinscribed(a_1, a_2, a_3):

    p = a + b + c
    
    R = sqrt( (p/2 - a_1) * (p/2 - a_2) * (p/2 - a_3) / (p/2))

    return R

def compute_Rdescribed(a_1, a_2, a_3):

    R = a_1 * a_2 * a_3 / (4 * s)
    
    return R

def compute_median(a_1, a_2, a_3):

    M = 0.5 * sqrt(2 * (pow(a_3,2) + pow(a_2,2)) - pow(a_1,2))
    
    return M

if a + b <= c or b + c <= a or a +c <= b:
    
    print("error")
    
else:     

   M_sum = compute_median(a, b, c) + compute_median(b, c, a) + compute_median(c, a, b)
   
   R_ins = compute_Rinscribed(a, b, c)
   
   R_des = compute_Rdescribed(a, b, c)
   
   print(round(R_ins,4), round(R_des,4), round(M_sum,4))
   
   #print("Стороны : ", round(a, 3), round(b, 3), round(c, 3))

   #print("Площадь : ", round(s,3))

   #print("Периметр : ", round(p,3))

   #print("Углы : ", round(angle_A, 3), round(angle_B, 3), round(angle_C, 3))
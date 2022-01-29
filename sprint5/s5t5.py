import cmath

def solve_quadric_equation(a, b, c):
    try:
        dis = (b ** 2) - (4 * a * c)  
        x1 = (-b-cmath.sqrt(dis))/(2*a)  
        x2 = (-b+cmath.sqrt(dis))/(2*a) 
        return f'The solution are x1={x1} and x2={x2}'    
    except ZeroDivisionError:
        return f'Zero Division Error'
    except TypeError:
        return f'Could not convert string to float'

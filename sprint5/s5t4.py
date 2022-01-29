def divide(numerator, denominator):
    try:
        return f'Result is {numerator / denominator}'
    except TypeError:
        return 'Value Error! You did not enter a number!'
    except ZeroDivisionError:
        return f'Oops, {numerator}/{denominator}, division by zero is error!!!'
        

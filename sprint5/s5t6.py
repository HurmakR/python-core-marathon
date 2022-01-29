class MyError(Exception):

    def __init__(self, num): 
        self.num = float(num)
    
    def __str__(self):
        return f'You input negative number: {self.num}. Try again.' 
    
def check_positive(number): 
    try:
        if float(number) > 0:
            return f'You input positive number: {float(number)}'
        else: 
            raise MyError(number)
    except ValueError:
        return "Error type: ValueError!"

    except MyError as e:
        return e

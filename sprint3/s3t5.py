def logger(func):
    
    def wrapper(*args, **kwargs):
        e=func(*args, **kwargs)
        listy=[]
        if args:
            for i in args:
                listy.append(str(i))
        if kwargs:    
            for key, val in kwargs.items():
                listy.append(str(val))

            
        #if func.__name__ != 'print_arg':
        print(f"Executing of function {func.__name__} with arguments {', '.join(listy)}...")    
        return e
    
    return wrapper

@logger
def concat(*args, **kwargs):
    conc=''
    if args:
        for i in args:
            conc+=str(i)
    if kwargs:    
        for key, val in kwargs.items():
            conc+=str(val)
    return conc
    

@logger
def sum(a,b):
    return a+b
    
@logger
def print_arg(arg):
    print(arg)
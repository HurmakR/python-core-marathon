def randomWord(lst):
    
    import random
    l1=list(lst)
    l2=list(lst)
    while l1:
        t=l1.pop(random.randint(0,len(l1)-1))
                   
        yield t
    
    while l2:
        r=l2.pop(random.randint(0,len(l2)-1))
           
        yield r
        
        
    while True:
        yield None
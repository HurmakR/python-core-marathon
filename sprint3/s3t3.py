def create_account(user_name, password, secret_words):
    import re
    
    pattern=r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!_%*?&])([a-zA-Z0-9@$!%*?&_]{6,})$'
    if not re.match(pattern, password):
         raise ValueError
            
            
    def check(passin, secretin):
        if passin == password and len(secretin) == len(secret_words):
            counter=0
            secret=sorted(secret_words)
            for i in secretin:
                if i in secret:
                    secret.pop(secret.index(i))
                    
                else:
                    counter += 1
            if counter <= 1:
                return True
            else:
                return False
        else:
            return False
        
    return check
    
tom = create_account("Tom", "Qwerty1_", ["1", "word"])  
check1 = tom("Qwerty1_",  ["1", "word"]) 
check2 = tom("Qwerty1_",  ["word"]) 
check3 = tom("Qwerty1_",  ["word", "2"]) 
check4 = tom("Qwerty1!",  ["word", "12"]) 
def toPostFixExpression(e):
    operators = ['+', '-', '/', '*', '(', ')']
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    temp = []
    post_string = []
    for i in e:
        if i not in operators:
            post_string.append(i)
        elif i == '(':
            temp.append(i)
        elif i == ')':
            while temp and temp[-1] != '(':
                post_string.append (temp.pop())
            temp.pop()
        else:
            while temp and temp[-1] != '(' and priority[i] <= priority[temp[-1]]:
                   post_string.append(temp.pop())
            temp.append(i)
    while temp:
        post_string.append(temp.pop())   
    
    return post_string
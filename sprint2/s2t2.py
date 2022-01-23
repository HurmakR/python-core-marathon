def morse_number(code):
    
    def dig_to_morse(char):
        if char == '0': return "----- "
        if char == '1': return ".---- "
        if char == '2': return "..--- "
        if char == '3': return "...-- "
        if char == '4': return "....- "
        if char == '5': return "..... "
        if char == '6': return "-.... "
        if char == '7': return "--... "
        if char == '8': return "---.. "
        if char == '9': return "----. "
        
    morse=''
    for i in code:
        morse += dig_to_morse(i)
    return morse
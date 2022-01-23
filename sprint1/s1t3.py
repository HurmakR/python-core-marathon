def isPalindrome(str):
    odd_char = 0
    chars_in_str = set(str)
    for i in chars_in_str:
        if str.count(i) % 2 != 0:
             odd_char += 1
        
    return False if odd_char > 1 else True
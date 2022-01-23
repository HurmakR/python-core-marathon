import re

def pretty_message(data):
   
   return re.sub(r'(\D+?)\1+', r'\1',data)
    
import re

def Regex(Text,regexType):
    matched = 1
    found = False
    match = re.search(regexType,Text)
    if(match!=None):
         print(Text)
         return matched
    else:
        return -1





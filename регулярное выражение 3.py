import re

def isTime(text:str):
    pattern = r'^([01]?\d|2[0-3])[:.-]([0-5]?\d)[:.-]([0-5]?\d)$'
    result = re.findall(pattern,text)
    return len(result) != 0

print(isTime("1.1.1"))
print(isTime("1:1:1"))
print(isTime("1-1-1"))
print(isTime("23.59.59"))
print(isTime("23.0.60"))

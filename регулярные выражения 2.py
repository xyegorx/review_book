import re
def isDate(text:str):
    pattern = r'^(0?[1-9]|[12]\d|3[01])[\.\\/-](0?[1-9]|1[012])[\.\\/-]\d+$'
    result = re.findall(pattern,text)
    return len(result) != 0


print(isDate('25.10.2023'))
print(isDate('AA.10.2023'))
print(isDate('11.02.2023'))
print(isDate('21.02.2023'))
print(isDate('17.02.2023'))
print(isDate('31.02.2023'))
print(isDate('1.02.2023'))
print(isDate('30.02.2023'))
print(isDate('2.02.2023'))
print(isDate('01.02.2023'))
print(isDate('32.02.2023'))
print()
print(isDate('1.00.2000'))
print(isDate('1.1.2000'))
print(isDate('1.01.2000'))
print(isDate('1.09.2000'))
print(isDate('1.10.2000'))
print(isDate('1.12.2000'))
print(isDate('1.13.2000'))
print(isDate('1.20.2000'))
print()
print(isDate('11/11/1111'))
print(isDate('11\\11\\1111'))
print(isDate('11-11-1111'))
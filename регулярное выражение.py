import re #регулярные выражения
pattern = r'\w+@\w+\.\w+' #r - регулярное выражение
text = 'test@test.test test2@test2.test2'
result = re.findall(pattern,text)
print(result)




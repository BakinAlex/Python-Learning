import re

with open('email_address.txt','r',encoding = 'utf-8') as file:
    content = file.read()
    print(content)
    rez = re.findall(r"\w+[@]\w+\w[.]\w+", content)
    print(rez)

frase = 'curso em video python'
frase2 = '      aprenda python       '

print(len(frase))
print(frase.count('o', 0, 13+1))
print(frase.find('deo'))
print(frase.find('android'))
print('curso' in frase)
print(frase[::2])

print(frase.replace('python', 'android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase2.strip())
print(frase2.lstrip())
print(frase2.rstrip())

frase3 = (frase.split())
print(frase3)

print('-'.join(frase3))

print('''
            Lorem Ipsum is simply dummy 
            text of the printing and 
            typesetting industry. 
            Lorem Ipsum has been 
            the industry's 
            standard dummy 
            text ever since 
            the 1500s.
      ''')

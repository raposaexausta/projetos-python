#Contador de letras utilizando estrutura while

frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum'

#Um método: print(frase.count('Python'))

i = 0
maior_aparição = 0
letra_maior_aparição = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    palavras_aparecidas = frase.count(letra_atual)


    if maior_aparição < palavras_aparecidas:
        maior_aparição = palavras_aparecidas
        letra_maior_aparição = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_maior_aparição}" que apareceu '
    f'{maior_aparição}x')
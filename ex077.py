palavras = ('banana', 'maca', 'pera', 'melao', 'melancia', 'coco')
for word in palavras:
    print('A palavra \33[35m{}\33[m possui as vogais:'.format(word.upper()), end = "")
    for letras in word:
        if letras in 'aeiou':
            print('\33[33:1m ', letras.upper(), end = "")
    print('.\33[m')

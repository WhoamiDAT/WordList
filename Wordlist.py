import random, time

menu = 0

while menu !=4:
    print('==' *18)
    print('𝑇𝐼𝑂 𝐷𝐴 𝐸𝑅𝑉𝐴 𝑦 𝑊𝐻𝑂𝐴𝑀𝐼')
    print('Seja Bem Vindo a Wordlist Generator.')
    print('[ 1 ] Apenas Textos')
    print('[ 2 ] Apenas Números')
    print('[ 3 ] Números e Textos')
    print('[ 4 ] Sair do Programa')
    print('==' *18)
    
    menu = int(input('Escolha um Número: '))

    if menu == 1:
        quant = input('Quantidade de senhas: ')
        max = int(input('Tamanho da senha(Em numero): '))
        for c in range(int(quant)):
            upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            all = upper
            lenght = max
            wordlist = "".join(random.sample(all, lenght))
            file = open('Wordlisttxt.txt', 'a')
            file.write(str(wordlist) + '\n')
            file.close()

        time.sleep(3)
        print('\n Worlist Criada...\n')

    if menu == 2:
        quant = input('Quantidade de senhas: ')
        max = int(input('Tamanho da senha(Em numero): '))
        for c in range(int(quant)):
            numbers = '0123456789'
            all = numbers
            lenght = max
            wordlist = "".join(random.sample(all, lenght))
            file = open('Wordlistnum.txt', 'a')
            file.write(str(wordlist) + '\n')
            file.close()

        time.sleep(3)
        print('\n Worlist Criada...\n')

    if menu == 3:
        quant = input('Quantidade de senhas: ')
        max = int(input('Tamanho da senha(Em numero): '))
        for c in range(int(quant)):
            upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            numbers = '0123456789'
            all = upper + numbers
            lenght = max
            wordlist = "".join(random.sample(all, lenght))
            file = open('Wordlist.txt', 'a')
            file.write(str(wordlist) + '\n')
            file.close()
            
        time.sleep(3)
        print('\n Worlist Criada...\n')

    if menu == 4:
        print('Finalizando...')
        

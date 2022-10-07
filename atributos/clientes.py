 
import random
nome = ['Miranda', 'Arthur', 'Ally', 'Heitor', 'Gabrielle', 'Dario', 'Bernardo', 'Gabriel', 'Locvan', 'Zé', 'Mayara', 'Cynara']
sobrenomes = ['Silva', 'Pereira', 'Oliveira', 'Batista', 'Bola', 'Schnapp', 'Soares', 'Monroe', 'Goth', 'Cacciari', 'Fernandes']
ruas = ['Rua Palmeiras', 'Rua Flamengo', 'Rua Brasil', 'Rua João Pinheiro', 'Rua Andorinhas']
numeroendereco = [180, 1441, 202, 567, 700, 800]
cpf = [12345, 54321, 65789, 59845, 12950, 90732, 93027, 15555]
numerostelefone1 = [99654, 99203, 99789, 99123, 99321, 99002,]
numerostelefone2 =  [3413, 1234, 4321, 7654, 9987, 4000, 3894]
anonascimento = [1994, 1997, 1978, 1987, 1965, 2002, 1984]
mesnascimento = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dianascimento =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
 
servidores = [
  'gmail.com', 'yahoo.com.br', 'amazon.com.br', 'protonmail.com', 'uol.com.br'
]
 
for i in range(40):
    nomex = random.choice(nome)
    sobrenomex = random.choice(sobrenomes)
    numeroenderecox = random.choice(numeroendereco)
    ruax = random.choice(ruas)
    cpfx = random.choice(cpf)
    numerostelefone1x = random.choice(numerostelefone1)
    numerostelefone2x = random.choice(numerostelefone2)
    anonascimentox = random.choice(anonascimento)
    dianascimentox = random.choice(dianascimento)
    mesnascimentox = random.choice(mesnascimento)
    idades = 2022 - anonascimentox
   
 
    print('insert into cliente (nome, endereço, cpf, telefone, data_nascimento, idade, email)')
    print(f'values (\'{nomex} {sobrenomex}\',\'{ruax}, {numeroenderecox}\', {cpfx}{cpfx}, {numerostelefone1x}{numerostelefone2x}, \'{anonascimentox}/{mesnascimentox}/{dianascimentox}\', {idades}, \'{nomex.lower()}{sobrenomex.lower()}@{random.choice(servidores)}\');')
 
 
 
 
 

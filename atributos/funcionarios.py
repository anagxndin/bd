# python C:\Users\15550649659\Documents\bd\atributos/funcionarios.py


import random

nomesf =['Ariel', 'Thamara', 'Helena', 'Mariana', 'Vic',  'Rafaela', 'Silvia',  'Clara', 'Patrícia', 'Mayara']

nomesm = ['Michelangelo', 'Ariel', 'Bruno', 'Ciro', 'Jair', 'Jarcy', 'Roberto', 'Carlos']

nomet = ['Ariel', 'Thamara', 'Helena', 'Mariana', 'Vic',  'Rafaela', 'Silvia',  'Clara', 'Patrícia', 'Mayara', 'Michelangelo', 'Ariel', 'Bruno', 'Ciro', 'Jair', 'Jarcy', 'Roberto', 'Carlos']

sobrenomes = ['Damares', 'Silvério', 'Theodoro', 'Circense', 'Carvalho', 'Almeida', 'Fischer', 'Corbucci', 'Vieira', 'Parreira', 'Britto']

cargos = ['Diretor Executivo (CEO)', 'Diretor de Operações (COO)', 'Diretor Financeiro (CFO)', 'Diretor de marketing (CMO)', 'Diretor de TI (CIO)', 'Diretor de Receita (CRO)', 'Gestor de marketing', 'Gerente de vendas', 'Supervisor de vendas', 'Coordenador de vendas', 'Consultor de vendas', 'Executivo de vendas ou analista de vendas', 'Suporte a vendas', 'Auxiliar de vendas ou assistente de vendas', 'Auxiliar administrativo de vendas']

departamento = [1, 2, 3, 4, 5]

mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dia =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
ano = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]


genero = ['Feminino', 'Masculino', 'Indefinido']

numerostelefone1 = [99654, 99203, 99789, 99123, 99321, 99002,]
numerostelefone2 =  [3413, 1234, 4321, 7654, 9987, 4000, 3894]



for i in range(15):
  nomex = random.choice(nomesm)
  nomestx = random.choice(nomet)
  sobrenomex = random.choice(sobrenomes)
  numerostelefone1x = random.choice(numerostelefone1)
  numerostelefone2x = random.choice(numerostelefone2)
  departamentox = random.choice(departamento)
  cargox = random.choice(cargos)
  diax = random.choice(dia)
  mesx = random.choice(mes)
  anox = random.choice(ano)
  print('insert into funcionários (matrícula, nome, sexo, telefone, dependentes, data_de_admissão, cargo, departamento)')
  print(f'values (\'##{i}D\',\'{nomex} {sobrenomex}\', \'Masculino\', \'{numerostelefone1x}{numerostelefone2x}\', \'{nomestx} {sobrenomex}\', \'{anox}/{mesx}/{diax}\', \'{cargox}\', \'{departamentox}\');')


for i in range(15):
  nomex = random.choice(nomesf)
  sobrenomex = random.choice(sobrenomes)
  numerostelefone1x = random.choice(numerostelefone1)
  numerostelefone2x = random.choice(numerostelefone2)
  departamentox = random.choice(departamento)
  cargox = random.choice(cargos)

  print('insert into funcionários (matrícula, nome, sexo, telefone, dependentes, data_de_admissão, cargo, departamento)')
  print(f'values (\'##{i}A\', \'{nomex} {sobrenomex}\', \'Feminino\', \'{numerostelefone1x}{numerostelefone2x}\', \'{nomestx} {sobrenomex}\', \'{anox}/{mesx}/{diax}\', \'{cargox}\', \'{departamentox}\');')


for i in range(15):
  nomex = random.choice(nomesf)
  sobrenomex = random.choice(sobrenomes)
  numerostelefone1x = random.choice(numerostelefone1)
  numerostelefone2x = random.choice(numerostelefone2)
  departamentox = random.choice(departamento)
  cargox = random.choice(cargos)

  print('insert into funcionários (matrícula, nome, sexo, telefone, dependentes, data_de_admissão, cargo, departamento)')
  print(f'values (\'##{i}{i}B\', \'{nomex} {sobrenomex}\', \'Feminino\', \'{numerostelefone1x}{numerostelefone2x}\', \'{nomestx} {sobrenomex}, {random.choice(nomet)} {sobrenomex}\', \'{anox}/{mesx}/{diax}\', \'{cargox}\', \'{departamentox}\');')


for i in range(10):
  nomestx = random.choice(nomet)
  sobrenomex = random.choice(sobrenomes)
  numerostelefone1x = random.choice(numerostelefone1)
  numerostelefone2x = random.choice(numerostelefone2)
  departamentox = random.choice(departamento)
  cargox = random.choice(cargos)
  print('insert into funcionários (matrícula, nome, sexo, telefone, dependentes, data_de_admissão, cargo, departamento)')
  print(f'values (\'##{i}{i}{i}C\',\'{nomestx} {sobrenomex}\', \'{random.choice(genero)}\', \'{numerostelefone1x}{numerostelefone2x}\', \'Sem dependentes.\', \'{anox}/{mesx}/{diax}\', \'{cargox}\', \'{departamentox}\');')


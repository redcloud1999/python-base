import sys
import logging





RESERVAS_FILE = 'reservas_1.txt'
QUARTOS_FILE = 'quartos.txt'

# ACESSO AO BANCO DE DADOS
ocupados = {}  # acumulador
try:
    for line in open(RESERVAS_FILE):
        nome_cliente, num_quarto, dias = line.strip().split(',')
        ocupados[int(num_quarto)] = {
            'nome_cliente': nome_cliente,
            'dias': int(dias)
        }

except FileNotFoundError:
    logging.error('arquivo %s não existe', RESERVAS_FILE)
    sys.exit(1)


# TODO: Usar função para ler os arquivos
quartos = {}  # acumulador
try:
    for line in open(QUARTOS_FILE):
        num_quarto, nome_quarto, preco = line.strip().split(',')
        quartos[int(num_quarto)] = {
            'nome_quarto': nome_quarto,
            'preco': float(preco), # TODO: Usar Decimal
            'disponivel': False if int(num_quarto) in ocupados else True
        }

except FileNotFoundError:
    logging.error('arquivo %s não existe', QUARTOS_FILE)
    sys.exit(1)


# PROGRAMA PRINCIPAL
print('Reserva no Hotel Pythonico LinuxTips')
print('_' * 40)

if len(quartos) == len(ocupados):
    print('Hotel está Lotado, volte depois.')
    sys.exit(0)

nome_cliente = input('Qual é o seu nome?: ').strip()
print()
print('Lista de Quartos')
print()
head = ['Número',  'Nome do Quarto', 'Preço', 'Disponivel']
print(f'{head[0]:<6} - {head[1]:<14} - R$ {head[2]:<9} - {head[3]:<10}')
for num_quarto, dados_quarto in quartos.items():
    nome_quarto = dados_quarto['nome_quarto']
    preco = dados_quarto['preco']
    disponivel = disponivel ='⛔' if not dados_quarto['disponivel'] else '👍'
    print(f'{num_quarto:<6} - {nome_quarto:<14} -  R$ {preco:<9.2f} - {disponivel}')

print('_' * 52)
# RESERVA

try:
    num_quarto = int(input('Qual o quarto desejado?: ').strip())
    if not quartos[num_quarto]['disponivel']:
        print(f'O quarto {num_quarto} está ocupado, escolha outro.')
        sys.exit(0)
except KeyError:
    logging.error(f'O Quarto {num_quarto} não existe!')
    sys.exit(0)
except ValueError:
    logging.error(f'Insira somente Números')
    sys.exit(0)

try:
    dias = int(input('Deseja ficar quantos dias?: ').strip())

except ValueError:
    logging.error(f'Insira somente Números')
    sys.exit(0)

nome_quarto = quartos[num_quarto]['nome_quarto']
preco_diaria = quartos[num_quarto]['preco']
total = dias * preco_diaria

print(
    f'Olá {nome_cliente}, você escolheu o {nome_quarto}'
    f' o valor total estimado será R$ {total:.2f}'
)

if input('Confirma? (digita y)').strip().lower() in ('y', 'yes', 'sim', 's'):
    with open(RESERVAS_FILE, 'a') as reserva_file:
        reserva_file.write(f'{nome_cliente},{num_quarto},{dias}\n')








































        


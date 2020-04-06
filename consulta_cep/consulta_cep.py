import requests

def main(): 
    print('####################')
    print('### Consulta CEP ###')
    print('####################')
    print()

    cep_input = input('Digite seu CEP: ')

    if len(cep_input) != 8:
        print('Quantidades de digitos invalida')
        exit()

    print('Resultado:')

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print('--- CEP encontrado ---')

        print('CEP: {}'.format(address_data['cep']))
        print('Logradouro: {}'.format(address_data['logradouro']))
        print('Bairro: {}'.format(address_data['bairro']))
        print('Cidade: {}'.format(address_data['localidade']))
        print('Estado: {}'.format(address_data['uf']))
        print('Cod. IBGE: {}'.format(address_data['ibge']))
    else: 
        print('{}: CEP inválido'.format(cep_input))

    print('-------------------------------------------------')
    option = int(input('Deseja realizar uma nova consulta?\n 1.Sim\n 2.Não\n'))

    if option == 1:
        main()
    else:
        print('Saindo...')

if __name__ == "__main__":
    main()
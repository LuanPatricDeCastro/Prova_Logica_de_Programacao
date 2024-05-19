print ('Bem vindo a copiadora do Luan Patric de Castro');

def escolha_servico():
    print('Nossos serviços são:');
    print('Serviço de digitalização = DIG');
    print('Serviço de impressão colorida = ICO');
    print('Serviço de impressão preto e branco = IPB');
    print('Serviço de Fotocópia = FOT');
    servico = input(('Escolha um dos serviços (DIG / ICO / IPB / FOT):'));
    if servico not in['DIG', 'ICO','IPB','FOT']:
        print('Escolha o serviço novamente: ');
        servico = input(('Escolha um dos serviços (DIG / ICO / IPB / FOT):'));
    if servico == 'DIG':
        valorservico = 1.10;
    elif servico == 'ICO':
        valorservico = 1.00;
    elif servico == 'IPB':
        valorservico = 0.40;
    else :
        valorservico = 0.20;
    print(f'o serviço escolhido custa R$ {valorservico} por página');
    return valorservico;


def num_pagina(valorservico):
    quantidadepaginas = int(input('Informe a quantidade de páginas: '));
    if(quantidadepaginas > 20000):
        print('Não aceitamos pedidos maiores que 20000 páginas');
        quantidadepaginas = int(input('Informe a quantidade de páginas: '));
    if quantidadepaginas < 20:
        valorimpressao = ((valorservico * quantidadepaginas) * 1);
    elif quantidadepaginas >= 20 and quantidadepaginas < 200:
        valorimpressao = ((valorservico * quantidadepaginas) * 0.85);
    elif quantidadepaginas >= 200 and quantidadepaginas < 2000:
        valorimpressao = ((valorservico * quantidadepaginas) * 0.80);
    elif quantidadepaginas >= 2000:
        valorimpressao = ((valorservico * quantidadepaginas) * 0.75);
    return valorimpressao;

def servico_extra():
    print('Serviços Adicionais:');
    print('0 = Impressão Normal');
    print('1 = Encadernação Simples');
    print('2 = Encadernação Capa Dura');
    servicoextra = int(input('Escolha uma opção (EC = 1 / ECP = 2 / IN = 0): '));
    if servicoextra not in [ 0 , 1 , 2 ]:
        print('Serviço indispónivel. Escolha um serviço: ');
        servicoextra = int(input('Escolha uma opção (EC = 1 / ECP = 2 / IN = 0): '));
    if(servicoextra == 1):
        valoradicional = 15;
    elif(servicoextra == 2):
        valoradicional = 40;
    elif(servicoextra == 0):
        valoradicional = 0;
    return valoradicional;


valorservico = escolha_servico();

valorimpressao = num_pagina(valorservico);

valoradicional = servico_extra();
print(f'O serviço escolhido custa R$ {valorservico} por pagína e o custo da impressão é: R$ {valorimpressao}');
valortotal = valorservico + valorimpressao + valoradicional;
print(f'O valor do serviço é R$ {valortotal}');
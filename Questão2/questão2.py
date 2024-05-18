print('Bem vindo a Loja de Gelados do Luan Patric de Castro');
print('-' * 15, 'Cardápio', '-' * 15 );
print('-' * 40);
print('-' * 3, 'Tamanho', '|', 'Cupuaçu (CP)', '|', 'Açai (AC)', '-' * 3);
print('-' * 9, 'P', '|','-' * 2, 'R$ 9,00', '-' * 2, '|', 'R$ 11,00');
print('-' * 9, 'M', '|','-' * 2, 'R$ 14,00','-' * 2, '|', 'R$ 16,00');
print('-' * 9, 'G', '|','-' * 2, 'R$ 18,00', '-' * 2,'|',  'R$ 20,00');

total_pedido = 0
quantidadeitens = 0;
while True:
    sabor = input("Digite o sabor (CP para Cupuaçu ou AC para Açaí): ")
    
    if sabor not in ["CP", "AC"]:
        print("Sabor inválido. Tente novamente.")
        quantidadeitens = quantidadeitens + 1;
        continue
    
    tamanho = input("Digite o tamanho (P para Pequeno, M para Médio ou G para Grande): ")
    
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente.")
        continue
    
    if sabor == "CP":
        if tamanho == "P":
            valor = 9
        elif tamanho == "M":
            valor = 14
        else:
            valor = 18
    else:
        if tamanho == "P":
            valor = 11
        elif tamanho == "M":
            valor = 16
        else:
            valor = 20
    total_pedido += valor

    print(f'O seu pedido é {sabor} no tamamnho {tamanho}');
    print(f'Você pediu {quantidadeitens} item(s)');
    print(f'O valor atual do seu pedido é: R$ {total_pedido}');
    
    mais_pedidos = input("Deseja pedir mais alguma coisa? (S/N): ")
    if mais_pedidos.upper() != "S":
        break

print(f"Total do pedido: R$ {total_pedido:.2f}")
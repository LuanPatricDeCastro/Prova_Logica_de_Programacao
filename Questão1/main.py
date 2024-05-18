print('Bem-vindo a loja do Luan Patric de Castro');

valorunitario = float (input('Informe o valor do produto: '));
quantidade = float(input('Informe a quantidade comprada: '));

valorcompra = quantidade * valorunitario;
print('O valor da compra sem desconto é: R$ ', valorcompra);
if(valorcompra < 2500):
    valorcomdesconto = valorcompra;
    print('O valor da compra com desconto é: R$ ', valorcomdesconto);
elif (valorcompra >= 2500 and valorcompra < 6000):
    valorcomdesconto = round(valorcompra * 0.96, 2);
    print('O valor da compra com desconto é: R$ ', valorcomdesconto);
elif (valorcompra >= 6000 and valorcompra < 10000):
    valorcomdesconto = round(valorcompra * 0.93, 2);
    print('O valor da compra com desconto é: R$ ', valorcomdesconto);
else:
    valorcomdesconto = round(valorcompra * 0.89, 2);
    print('O valor da compra com desconto é: R$ ', valorcomdesconto);
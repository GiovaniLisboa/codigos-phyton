saldo = 1000
print ("SELECIONE A OPERAÇÃO DESEJADA")
print ("1. Sacar")
print ("2. Depositar")
print ("3. Ver saldo")
print ("4. Encerrar")
int(input(seleção))
if (seleção == 1)
{
    repeat
    teste = false
    print("Qual valor deseja sacar?")
    int(input(saque))
    if (saque <= saldo)
    {
    print ("Retire seu dinheiro")
    saldo = saldo - saque
    teste = true 
    }
    else print ("Valor inválido")
    until teste = true
}
else if (seleção == 2)
{
    repeat
    teste = false
    print("Qual valor deseja depositar?")
    int(input(deposito))
    if (deposito < 0)
    {
    print ("Transação concluída")
    saldo = saldo + deposito
    teste = true 
    }
    else print ("Valor inválido")
}
else if (seleção == 3)
{
    repeat
    teste = false
    print("Saldo -> R$",saldo)
}
else if (seleção == 4)
print ("Retire seu cartão")
else print ("Operação inválida")

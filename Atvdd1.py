numero = []
nomes = []
def cadastro(num, nome):
     def deletar(num):
         if num in numero:
                posição= numero.index(num)
                numero.pop(posição)
                nomes.pop(posição)
                return "A chapa de numero", num, "foi removida"
         else:
              return("Não existe uma chapa com esse número")
     numero.append(num)
     nomes.append(nome)
     return "A chapa foi cadastrada com sucesso"

def pesquisar():
    cont = 0
    while cont < len(nomes):
         print(numero[cont])
         print(nomes[cont])
         cont += 1

def atualizar(num):
    novonumero = int(input("Digite o novo número"))
    novonome = "Israel"
    if num in numero:
        posicao = numero.index(num)
        numero[posicao] = novonumero
        nomes[posicao] = novonome
        return "Chapa atualizada com sucesso"

op = 10
while op !=0:
        op = int(input("Digite sua opção:"+
                       
                     "\n 1 - Cadastrar uma chapa"+
                     "\n 2 - Pesquisar uma chapa"+
                     "\n 3 - Atualize uma chapa"+
                     "\n 4 - Delete uma chapa"+
                     "\n 0 - Feche o sistema"+
                     
                     "\n Escolha uma opção: ")) 
        if op == 1:
             num = int(input("Digite o número da sua chapa: "))
             nome = input("Digite o nome da chapa: ")
             print(cadastro(num, nome))
        elif op ==2:
             def pesquisar():
                  return 0
             if op==1:
                  cadastro


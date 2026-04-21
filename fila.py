from collections import deque

fila = deque()
contador = 0


def menu():
    print("\n--- Sistema de Atendimento ---")
    print("1 - Adicionar cliente")
    print("2 - Atender cliente")
    print("3 - Ver fila")
    print("4 - Nº pessoas fila")
    print("5 - Clientes Atendidos")
    print("6 - Sair")


def adicionar_cliente(fila):
    nome = input("Digite o nome do cliente: ").capitalize()
    fila.append(nome)
    print(f"{nome}, você foi adicionado à fila.")


def atender_cliente(fila, contador):
    if fila:
        cliente = fila.popleft()
        print(f"{cliente}, você foi chamado.")
        contador += 1
        return contador
    else:
        print("Fila vazia.")
        return contador


def ver_fila(fila):
    print(f"Fila atual: {list(fila)}")


def contador_fila(fila):
    print(f"Quantidade de pessoas na fila: {len(fila)}")


def total_atendidos(contador):
    print(f"Total atendidos: {contador}")


def main():
    contador = 0

    opcoes = {
        1: lambda: adicionar_cliente(fila),
        3: lambda: ver_fila(fila),
        4: lambda: contador_fila(fila),
        5: lambda: total_atendidos(contador),
    }

    while True:
        menu()

        try:
            opcao = int(input("Escolha uma opção acima: "))
        except ValueError:
            print("❌ Digite um número válido!")
            continue

        if opcao == 2:
            contador = atender_cliente(fila, contador)

        elif opcao in opcoes:
            opcoes[opcao]()

        elif opcao == 6:
            print("Saindo...")
            break

        else:
            print("Opção inválida!!!")


main()

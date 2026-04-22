from collections import deque


def menu() -> None:
    """Exibe o menu principal do sistema."""
    print("\n--- Sistema de Atendimento ---")
    print("1 - Adicionar cliente")
    print("2 - Atender cliente")
    print("3 - Ver fila")
    print("4 - Nº pessoas fila")
    print("5 - Clientes Atendidos")
    print("6 - Sair")


def adicionar_cliente(fila: deque[str]) -> None:
    """Solicita um nome válido e adiciona o cliente à fila."""
    nome = input("Digite o nome do cliente: ").strip()
    if not nome:
        print("Nome inválido. Digite um nome não vazio.")
        return

    nome_formatado = nome.title()
    fila.append(nome_formatado)
    print(f"{nome_formatado}, você foi adicionado à fila.")


def atender_cliente(fila: deque[str], contador: int) -> int:
    """Atende o próximo cliente da fila e atualiza o contador."""
    if not fila:
        print("Fila vazia.")
        return contador

    cliente = fila.popleft()
    print(f"{cliente}, você foi chamado.")
    return contador + 1


def ver_fila(fila: deque[str]) -> None:
    """Exibe os clientes atualmente na fila."""
    if not fila:
        print("Fila atual: vazia.")
        return

    print("Fila atual:")
    for posicao, cliente in enumerate(fila, start=1):
        print(f"{posicao}. {cliente}")


def mostrar_tamanho_fila(fila: deque[str]) -> None:
    """Mostra a quantidade de pessoas aguardando atendimento."""
    print(f"Quantidade de pessoas na fila: {len(fila)}")


def total_atendidos(contador: int) -> None:
    """Exibe o total de clientes já atendidos."""
    print(f"Total atendidos: {contador}")


def main() -> None:
    """Executa o loop principal do sistema de atendimento."""
    fila: deque[str] = deque()
    contador = 0

    while True:
        menu()

        try:
            opcao = int(input("Escolha uma opção acima: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if opcao == 1:
            adicionar_cliente(fila)
        elif opcao == 2:
            contador = atender_cliente(fila, contador)
        elif opcao == 3:
            ver_fila(fila)
        elif opcao == 4:
            mostrar_tamanho_fila(fila)
        elif opcao == 5:
            total_atendidos(contador)
        elif opcao == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

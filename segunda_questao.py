def fibonacci(num):
    """
    Calcula os números da sequência de Fibonacci.

    Args:
        num (int): O número de termos da sequência a calcular.

    Returns:
        list: Uma lista contendo os números da sequência de Fibonacci.
    """
    sequencia_fibonacci = [0, 1]
    if num <= 0:
        return [num]
    while len(sequencia_fibonacci) - 1 < num:
        sequencia_fibonacci.append(sequencia_fibonacci[-1] + sequencia_fibonacci[-2])
    return sequencia_fibonacci


def encontrar_num(sequencia_fibonacci, num):
    """
        Verifica se um número está presente na sequência de Fibonacci.

        Args:
            sequencia_fibonacci (list): A sequência de Fibonacci.
            num (int): O número a ser buscado.

        Returns:
            str: Uma mensagem indicando se o número foi encontrado.
    """
    if num in sequencia_fibonacci:
        return "está presente na sequência."
    return "não está presente na sequência."


num = 21
print(f"O número {num} {encontrar_num(fibonacci(num), num)}")

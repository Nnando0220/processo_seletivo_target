faturamento_estados_distribuidora = [
    {"estado": "SP", "valor": 67836.43},
    {"estado": "RJ", "valor": 36678.66},
    {"estado": "MG", "valor": 29229.88},
    {"estado": "ES", "valor": 27165.48},
    {"estado": "Outros", "valor": 19849.53}
]#lista de dados dos estados da distribuidora com seus respectivos valores


def calculo_porcentagem_estados(faturamento_estados):
    """Calcula o percentual de representação de cada estado no faturamento total.

        Args:
            faturamento_estados (list): Lista de dicionários contendo o estado e o valor de faturamento.

        Returns:
            list: Lista de dicionários com o estado e a porcentagem de faturamento correspondente.
    """
    total_faturamento = sum(faturamento_estado['valor'] for faturamento_estado in faturamento_estados)
    return [
        {
            "estado": faturamento_estado["estado"],
            "porcentagem": (faturamento_estado['valor'] / total_faturamento) * 100
        }
        for faturamento_estado in faturamento_estados
    ]


faturamento_estados = calculo_porcentagem_estados(faturamento_estados_distribuidora)
for faturamento in faturamento_estados:#Exibe o percentual de representação de cada estado no faturamento total
    print(f"O percentual de representação de {faturamento['estado']} é {faturamento['porcentagem']}%")

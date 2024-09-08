import json

with open('dados_terceira_questao.json', 'r', encoding='utf-8') as arquivo:#Busca o arquivo Json e faz seu carregamemnto em uma variavel
    dados_json = json.load(arquivo)

def buscar_valores_validos(dados_json):
    """"Filtra os valores de faturamento positivos do JSON.

        Args:
            dados_json: Lista de dicionários com os dados de faturamento.

        Returns:
            list: Lista de valores de faturamento positivos.
    """
    return [dado['valor'] for dado in dados_json if dado['valor'] > 0]

def buscar_menor_valor_dia(dados_json):
    """Encontra o dia com o menor valor de faturamento.

        Args:
            dados_json: Lista de dicionários com os dados de faturamento.

        Returns:
            tuple: Tupla com o dia e o menor valor de faturamento.
    """
    menor_valor = min(buscar_valores_validos(dados_json))
    dia_com_menor_valor = next(dado['dia'] for dado in dados_json if dado['valor'] == menor_valor)
    return dia_com_menor_valor, menor_valor


def buscar_maior_valor_dia(dados_json):
    """Encontra o dia com o maior valor de faturamento.

        Args:
            dados_json: Lista de dicionários com os dados de faturamento.

        Returns:
            tuple: Tupla com o dia e o maior valor de faturamento.
    """
    maior_valor = max(buscar_valores_validos(dados_json))
    dia_com_maior_valor = next(dado['dia'] for dado in dados_json if dado['valor'] == maior_valor)
    return dia_com_maior_valor, maior_valor


def num_dias_maior_med_faturamento(dados_json):
    """Calcula o número de dias com faturamento acima da média mensal.

        Args:
            dados_json: Lista de dicionários com os dados de faturamento.

        Returns:
            int: Número de dias com faturamento acima da média mensal.
    """
    soma_faturamento = sum(buscar_valores_validos(dados_json))
    dias_util_semana = len(buscar_valores_validos(dados_json))
    media_faturamento = (soma_faturamento/dias_util_semana)
    return len([dado['dia'] for dado in dados_json if dado['valor'] > media_faturamento])


dia_com_menor_valor, menor_valor = buscar_menor_valor_dia(dados_json)
dia_com_maior_valor, maior_valor = buscar_maior_valor_dia(dados_json)
dias_acima_da_media = num_dias_maior_med_faturamento(dados_json)

print(f"Menor valor de faturamento foi no dia {dia_com_menor_valor}: {menor_valor}")
print(f"Maior valor de faturamento foi no dia {dia_com_maior_valor}: {maior_valor}")
print(f"Número de dias com faturamento maior que a média mensal: {dias_acima_da_media}")
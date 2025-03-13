import json

def carregar_faturamento(arquivo):
    with open(arquivo, 'r') as file:
        return json.load(file)
def calcular_faturamento(dados):
    faturamento_valido = [dia["valor"] for dia in dados if dia["valor"] > 0]
    if not faturamento_valido:
        return "Nenhum dia útil com faturamento registrado."
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)
    dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_mensal)


    
    return {
        "Menor Faturamento": menor_faturamento,
        "Maior Faturamento": maior_faturamento,
        "Dias Acima da Média": dias_acima_da_media
    }
dados_faturamento = carregar_faturamento("dados.json")
resultado = calcular_faturamento(dados_faturamento)






print("Resultados do Faturamento:")
for chave, valor in resultado.items():
    print(f"{chave}: {valor}")

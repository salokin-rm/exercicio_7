"""
Nome: Progressão Geométrica
Autor: Nikolas
Data: 26/06/2023
Versão: 0.0.1
"""

### Atribuição de variáveis e entrada de dados

n = float(input(f"Digite o primeiro termo 'n' de uma progressão geométrica:"))
print(n)

r = float(input(f"\nDigite a razão da progressão geométrica:"))
print(r)

nesima = float(input(f"\nDigite a n-ésima posição na série do termo desejado:"))
print(nesima)


### Processamento de dados

# Equação de Termos da P.G. --> termo_desejado_a = (primeiro_termo_an)*(razão^(n-ésima_posição - 1))

termo = (n*(r**(nesima - 1)))

# Equação de Soma dos Termos da P.G. --> soma_pg = ((primeiro_termo_an)*(razão^(n-ésima_posição) - 1)/(razão - 1))

soma = (n*((r**nesima) - 1)/(r-1))

### Saída de dados

print("\nO",nesima,"º termo da progressão geométrica com termo inicial igual a",n," e razão igual a",r,"é:",termo,".\nA soma dos termos da P.G. até (incluso) o número",termo,"é igual a:",soma,".")

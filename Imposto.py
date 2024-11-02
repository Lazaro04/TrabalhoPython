def somaimposto(taxaimposto, custo):
    valor_com_imposto = custo + (custo*taxaimposto)/100
    return valor_com_imposto


print(somaimposto(0.5, 100))

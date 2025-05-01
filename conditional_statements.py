state = input("digite seu estado (CA, MN, or NY): ") # apenas em MAIÚSCULO 
purchase_amount = float(input("digite o valor da compra: "))  
if state == "CA":  
    tax_amount = 0.075
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Você é de {}, seu custo total é {:.2f}.".format(state, total_cost)

elif state == "MN":  
    tax_amount = 0.095
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Você é de {}, seu custo total é {:.2f}.".format(state, total_cost)

elif state == "NY":  
    tax_amount = 0.089
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Você é de {}, seu custo total é {:.2f}.".format(state, total_cost)

else:
    result = "Estado inválido. Digite CA, MN, or NY."

print(result)
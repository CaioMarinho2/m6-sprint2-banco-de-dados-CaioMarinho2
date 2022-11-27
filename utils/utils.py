
# converting the transaction type to get your name and be able to calculate the total balance
def convert_transactions(type,value):
    if int(type)==1:
        return {"type":"Débito","value":value}
    
    if int(type)==2:
        return {"type":"Boleto","value":-value}
    
    if int(type)==3:
        return {"type":"Financiamento","value":-value}
    
    if int(type)==4:
        return {"type":"Crédito","value":value}
    
    if int(type)==5:
        return {"type":"Recebimento Empréstimo","value":value}
    
    if int(type)==6:
        return {"type":"Vendas","value":value}
    
    if int(type)==7:
        return {"type":"Recebimento TED","value":value}
    
    if int(type)==8:
        return {"type":"Recebimento DOC","value":value}
    
    if int(type)==9:
        return {"type":"Aluguel","value":-value}
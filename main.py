def valorAerea(base, altura):
  area = base * altura
  return area 

  
ladoBase = int(input("Digite o valor do lado das bases: "))
ladoAltura = int(input("Digite o valor do lado das alturas: "))
area = valorAerea(ladoBase, ladoAltura)
print(f"O resultado da Área: {area}")
nota1 = float(input("Insira a nota 1 (0-20): "))
nota2 = float(input("Insira a nota 2 (0-20): "))
nota3 = float(input("Insira a nota 3 (0-20): "))

mediaPon = (nota1*0.25)+(nota2*0.35)+(nota3*0.40)

if mediaPon >= 9.5:
    print ("Voce foi aprovado")

else:
    print ("Voce foi reprovado")

print (f"Media ponderada = {mediaPon}")

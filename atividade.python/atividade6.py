nome = input ("digite seu nome")
idade = int (input("digite sua idade:"))

while idade > 120 or idade < 0:
    idade = int(input("idade(anos completos - ate 120 anos)"))
    dias_vida = idade * 365
    print(f"{nome}, você viveu {dias_vida}")
    
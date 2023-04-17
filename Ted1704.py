#1. Faça um programa que leia dois números inteiros e exiba o maior deles.

num1 = float(input("Qual primeiro número? "));
num2 = float(input("Qual segundo número? "));

if(num1>num2):
    print("o primeiro número é maior");
else:
    print("o segundo número é maior");

#2. Escreva um programa que receba a idade de uma pessoa e informe se ela é maior de idade ou não.

idade = int(input("Qual sua idade? "));

if(idade>=18):
    print("Maior de idade");
else:
    print("Menor de idade");

#3. Crie um programa que solicite o nome e a idade do usuário e informe se ele pode dirigir um veículo.

nome = input("Qual seu nome? ");
idade = int(input("Qual sua idade? "))

if(idade>=18):
    print(f"{nome} pode dirigir veículo por ter {idade} anos.");
else:
    print(f"{nome} não pode dirigir veículo por ter {idade} anos.");

#4. Faça um programa que calcule a média aritmética de 4 notas e informe se o aluno foi aprovado (média maior ou igual a 7) ou reprovado.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = nota1 + nota2 + nota3 + nota4 / 4;

if(media>=7):
    print("Aprovado");
else:
    print("Reprovado");

#5. Escreva um programa que receba um número inteiro e informe se ele é par ou ímpar.

num = int(input("Digite um número: "))

teste = num%2

if(teste == 0):
    print("Par")
else:
    print("Impar")

#6. Faça um programa que leia o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1500,00, o aumento é de 10%. Para salários inferiores ou iguais a R$1500,00, o aumento é de 15%.

salario = float(input("Digite seu salário: "))

if(salario>=1500):
    print(salario*1.1);
else:
    print(salario*1.15);

#7. Faça um programa que leia uma lista de números inteiros e informe qual o maior valor e qual o menor valor da lista.

listaNum = {2, 20, 15, 40}

print("o máximo é: ", max(listaNum))
print("o mínimo é: ", min(listaNum))

#8.  Escreva um programa que leia uma string e verifique se ela é um palíndromo. Um palíndromo é uma palavra que pode ser lida tanto da esquerda para a direita quanto da direita para a esquerda e possui o mesmo significado.

texto = input("Escreva sua palavra: ")

if(texto == texto[::-1]):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

#9. Faça um programa que gere a tabuada de um número informado pelo usuário.

num = int(input("Digite um valor maior que zero: "))

for i in range(11):
    print(num, " * ", i, " = ", num * i, "\n")

#10. Escreva um programa que leia uma lista de nomes e remova todos os nomes duplicados, deixando apenas um de cada nome na lista final.

lista = ["Alan", "Paula", "Pabllo", "Paula", "Paula"];

sett = set (lista);

print(sett)

import re


class CalcIMC:  # Cálculo do Índice de Massa Corporal

    def iniciar(self):  # Função iniciar, que chama de forma ordenada as demais funções;
        self.inicio = input("Deseja iniciar o calculo de IMC? \n Sim - 1 \n Não - 2 \n")
        if self.inicio == "1":
            print("\n Iniciando Avaliação! \n")
            self.extrair_altura()
            self.extrair_peso()
            self.calcular_imc()
            self.refazer_avaliacao()
        elif self.inicio == "2":
            print("Okay, até a próxima!")
        else:
            print("Não entendi, tente novamente! \n")
            self.iniciar()

    def extrair_altura(self):  # Função responsável por coletar o dado altura
        self.altura = input("Digite sua altura em metros: ")
        self.altura_ajustada = self.altura.replace(',', '.')  # Adequando caso o usuário tenha usado ','
        formato = re.compile(
            r'^[0-9]+\.[0-9]*$')  # Definindo o formato no qual a altura deve ser inserida
        padrao = re.match(formato, self.altura_ajustada)  # Validando se a altura cumpre os requisitos definidos
        if padrao:
            print("Altura Válida!")
        else:
            print("Digite uma altura valida!")
            self.extrair_altura()

    def extrair_peso(self):  # Função responśavel por coletar o dado peso;
        self.peso = input("Digite seu peso em Kg: ")
        self.peso_ajustado = self.peso.replace(',', '.')  # Adequando caso o usuário tenha usado ','
        padrao = self.peso_ajustado.replace('.', '', 1).isdigit()  # Validando se o peso é realmente numérico
        if padrao:
            print("Peso Válido!")
        else:
            print('Digite um peso valido!')
            self.extrair_peso()

    def calcular_imc(self):  # Função responsável por calcular o imc e buscar na tabela o valor correspondente
        mt = float(self.altura_ajustada)  # Converter a string altura em float
        kg = float(self.peso_ajustado)  # Converter a string peso em float
        imc = kg / mt ** 2
        print("Seu IMC é: %.2f" % imc)
        if imc < 16:
            print("Magreza grave\n")
        elif imc < 17:
            print("Magreza moderada\n")
        elif imc < 18.5:
            print("Magreza leve\n")
        elif imc < 25:
            print("Saudável\n")
        elif imc < 30:
            print("Sobrepeso\n")
        elif imc < 35:
            print("Obesidade Grau I\n")
        elif imc < 40:
            print("Obesidade Grau II (severa)\n")
        else:
            print("Obesidade Grau III (mórbida)\n")

    def refazer_avaliacao(self):  # Função reiniciar, caso o usuário queira refazer o processo
        self.refazer = input("Você deseja fazer outra avaliação? \n 1 - Sim \n 2 - Não \n")
        if self.refazer == "1":
            print("\n Reiniciando Avaliação!\n")
            self.extrair_altura()
            self.extrair_peso()
            self.calcular_imc()
            self.refazer_avaliacao()
        elif self.refazer == "2":
            print("Okay, até a próxima!")
        else:
            print("Não entendi, tente novamente! \n")
            self.refazer_avaliacao()


IMC = CalcIMC()
IMC.iniciar()

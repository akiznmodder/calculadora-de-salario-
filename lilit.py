# ===== ANOTAÇÃO =====
# Este arquivo contém um exercício de Python para calcular
# o salário horário de um funcionário durante o mês.
# O usuário deve fornecer o salário mensal e o número de horas
# trabalhadas no mês, e o programa calculará e exibirá o salário
# por hora.
# ====================

salario  = float(input("Digite o salário mensal: "))
horas = float(input("digite o numero de horas trabalhadas na semana: "))

soma_hora = horas * 4
salario_hora = salario / soma_hora
print(f"O salário por hora é: R$ {salario_hora:.2f}")
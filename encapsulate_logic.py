#variaveis numericas: calculation_to_hours,
#variaveis matemáticas: calculation_to_minutes, calculation_to_seconds
#funções: day_to_units
# parâmetros de função: num_of_days, unit
# variaveis de entrada: user_input
# variaveis de descompactação de entrada: days, unit
# argumentos de função: days, unit

# armazenar horas de um dia em uma variavel calculo de dias para horas
calculation_to_hours = 24

# armazenar minutos de um dia em uma variavel calculo de dias para minutos
calculation_to_minutes = 24 * 60

# armazenar segundos de um dia em uma variavel calculo de dias para segundos
calculation_to_seconds = 24 * 60 * 60

# criar função que converte dias para unidades com dois paremetros: numero de dias e unidades
def days_to_units(num_of_days, unit):
    # se a unidade for igual a horas retorna numero de dias são numero de dias vezes variavel de calculo correspondente com sua unidade um if e 2 elifs e um else
    if unit == "hours":
        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {unit}"
    elif unit == "minutes":
        return f"{num_of_days} days are {num_of_days * calculation_to_minutes} {unit}"
    elif unit == "seconds":
        return f"{num_of_days} days are {num_of_days * calculation_to_seconds} {unit}"
    #else retornando unidade não suportada
    else:
        return "Unsupported unit"

# inicio do loop while
while True:
    # entrada do usuário com texto de orientaçõs das unidades ou palavra para encerrar
    user_input = input("Enter number of days and conversion unit (hours/minutes/seconds) or 'exit' to quit: ")
    
    #condicional reduzindo entrada do usuario a minúsculas se for igual a 'exit' encerrar o loop
    if user_input.lower() == 'exit':
        break
    
    # inicira um tratamento de erro para dias e unidades se tiver erro desvia para o except
    try:
        #dividir a entrada do usuário em uma lista de sub strings com split e descompactar nas variaveis dias e unidades
        days, unit = user_input.split()
        # conveter unidade de dias para inteiro
        days = int(days)

        # iniciar variável e chamar função de retorno de mensagem com os parametros de entrada dias e  unidade como argumentos
        message = days_to_units(days, unit)
        # imprimir a mensagem retornada pela função
        print(message)
    #saída do tratamento de erro com ValueError - se a entrada do usuário não puder ser dividida em duas partes (dias e unidade) ou se a parte dos dias não puder ser convertida para um inteiro.
    except ValueError:
        # imprimir mensagem de invalid input pedir para colocar numero de dias e unidades separados por espaço   
        print("Invalid input. Please enter the number of days and the unit separated by a space.")


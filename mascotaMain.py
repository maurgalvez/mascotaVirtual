nombre = ""
hambre = 50
energia = 80
felicidad = 60
salud = 100
nivel = 1
experiencia = 0
dia = 1

def mostrar_estado():
    print(f"{nombre} | Nivel {nivel} | Día {dia}")
    print(f" Hambre {hambre}")
    print(f" Energía {energia}")
    print(f" Felicidad {felicidad}")
    print(f" Salud {salud}")
    print(f" EXP {experiencia}")

def subir_nivel():
    global nivel, experiencia, salud
    if experiencia >= nivel * 100:
        experiencia = experiencia - (nivel * 100)
        nivel += 1
        salud = salud + 20
        saludRecuperada = 20
        print(f"\n {nombre} subió al nivel {nivel}!")
        print(f" Recupero {saludRecuperada} de salud ")

def ganar_exp(cantidad):
    global experiencia
    experiencia += cantidad
    print(f" +{cantidad} EXP")
    subir_nivel()
nombre = "maurochupameelpico"
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

def alimentar():
    global hambre, felicidad, energia
    print("\n ¿Qué le daras de comer?")
    print("  1. Croquetas      (hambre -20, felicidad +5)")
    print("  2. Snack sabroso  (hambre -35, felicidad +15)")
    print("  3. Fruta fresca   (hambre -25, energia +10)")
    print("  0. Cancelar")

    opcion = input("Ingrese opción: ")

    if opcion == "1":
        hambre = hambre - 20
        felicidad = felicidad + 5
        print(f"\n {nombre} comió sus croquetas")
        ganar_exp(10)
    elif opcion == "2":
        hambre = hambre - 35
        felicidad = felicidad + 15
        print(f"\n {nombre} comió sus croquetas")
        ganar_exp(15)
    elif opcion == "3":
        hambre = hambre - 25
        felicidad = felicidad + 10
        print(f"\n {nombre} comió su fruta fresca")
        ganar_exp(12)
    else:
        print ("  Opción no válida.")

def entrenar():
    global energia, felicidad, hambre, salud
    
    if energia < 20:
        print(f"\n {nombre} está muy cansado para entrenar.")
        return
    
    print("\n ¿Qué entrenamiento hacer?")
    print("  1. Caminata suave   (energia -10, salud +5)")
    print("  2. Ejercicio fuerte (energia -25, salud +15, hambre +15)")
    print("  3. Yoga y descanso  (energia -5,  felicidad +10)")
    print("  0. Cancelar")

    opcion = input("Ingrese opción: ")

    if opcion == "1":
        energia = energia - 10
        salud = salud + 5
        print(f"\n {nombre} salió a caminar")
        ganar_exp(15)
    elif opcion == "2":
        energia = energia - 25
        salud = salud + 15
        hambre = hambre + 15
        print(f"\n {nombre} hizo ejercicio intenso")
        ganar_exp(30)
    elif opcion == "3":
        energia = energia - 5
        felicidad = felicidad + 10
        print(f"\n {nombre} hizo yoga y se relajó")
        ganar_exp(12)
    else:
        print ("  Opción no válida.")

def jugar():
    global energia

    
    if energia < 15:
        print(f"\n {nombre} no tiene energía para jugar.")
        return
    juegos = ["pelota", "nadar"; "tirar la cuerda"]
    juego = juegos[random.randint(0, len(juegos) - 1)]
    
    print(f"\n {nombre} juega a {juego}!")
    energia = energia - 15
    felicidad = felicidad + 20

def dormir():

    print(f"\n {nombre} se va a dormir...")

    horas = 0

    for h in range(8):
        energia = energia + 10
        salud = salud + 2
        hambre = hambre + 5
        horas += 1

    felicidad = felicidad + 5
    print(f" {nombre} durmió {horas} horas y se recuperó")
    ganar_exp(5)


    
    
 

name = input("¿Cuál es tu nombre? ")
first_name = input("¿Cuál es tu apellido? ")
print("Hellow", name.capitalize()+ " " + first_name.capitalize(), "¡Bienvenido a Python!")

adulto = str(input("¿Eres un adulto? (si/no) "))
r_major = "Tu eres un adulto, puedes acceder! "
r_menor = "Eres menor de edad, no puedes acceder! "
if adulto == "si":
 date = int(input("¿Que edad tienes? "))
 if date >= 18:
  print (r_major)
 else:
  print (r_menor)
elif adulto == "no":
  print (r_menor)
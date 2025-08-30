name = input("What are you name? ")
first_name = input("waht are your first name? ")
print("Hellow", name.capitalize()+ " " + first_name.capitalize(), "Welcome to the python curse of the honeycomb!")

adulto = str(input("are you an adult (yes/no) "))
r_major = "you are major, you can enter! "
r_menor = "you are minor, you can't enter! "
if adulto == "yes":
 date = int(input("What is date? "))
 if date >= 18:
  print (r_major)
 else :
  print (r_menor)
elif adulto == "no":
  print (r_menor)

score = date
if score >= 18 and score <= 24:
    print("Grade: A")
elif score >= 25:
    print("Grade: B")
elif score >= 35:
    print("Grade: C")
elif score >= 45:
    print("Grade: D") 
else: 
    print("Grade: X")

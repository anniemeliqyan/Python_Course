name = input("please enter your name")
z = "Hello, " + (((name != "Mubashir") * name) or ((name == "Mubashir") * "My Love")) + "!"
print(z)

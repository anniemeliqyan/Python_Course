user = input(" Enter the user`s name ,please   ")
x = "Hello ," + (((user != "Mubashir") * user) or ((user == "Mubashir") * "my Love")) + "!"
print(x)
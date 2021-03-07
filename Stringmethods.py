print(dir("hello"))
print(help("hello".format))
s = "hello, my name is {}".format("Bogdan")
print(s)
s = "This contract is between lawyer {} and client {} and you will pay me {}$".format("Carlos", "Bogdan", "and you will pay me $1000")
print(s)
print(s.count(" "))
print(s.lower())
print(s.split())
lawyer = input("Please give me the name of the lawyer")
client = "Beatriz Pisoni"
sum = "500"
s = f"Lawyer: {lawyer}, Client: {client}, value: {sum}$"
print(s)

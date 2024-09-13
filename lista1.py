nombres = ["JEREMIAS", "ANA", "IGNACIO", "PAUL", "VICTORIA "]
print ( len (nombres))
nombres.append("JUAN")
print (nombres)
nombres.remove("ANA")
print (nombres)
if "IGNACIO" in nombres:
    print (f"{IGNACIO}esta en la lista")
else:
    print (f"{CARLOS}no se encontro")

print(nombres.sort())
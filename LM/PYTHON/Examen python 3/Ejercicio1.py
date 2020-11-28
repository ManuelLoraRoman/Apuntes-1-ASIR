def EstaRebajado(art):
    if "Rebajas" in art:
        return True
    else:
        return False

def CalcularPrecio(art,precio,cant):
    if EstaRebajado(art) == True:
        total = "El precio del artículo " + art + " es igual a " + str((precio * 0.5)*cant) + "€."
        return total
    else:
        total = "El precio del artículo " + art + " es igual a " + str(precio*cant) + "€."
        return total

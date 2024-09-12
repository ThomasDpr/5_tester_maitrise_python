def square(number: int | float) -> None:
    """
    Calcule la puissance carrée d'un nombre.

    Args:
        number (int | float): le nombre où on veut calculer sa puissance carrée

    Returns:
        None
    """

    try:
        result = (number ** 2)
    except TypeError:
        print("Le paramètre doit être un nombre !")
        return None
    
    return result

print(square(5))


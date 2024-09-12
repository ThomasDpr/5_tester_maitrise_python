def calculate_average(numbers):
    """
    Calcule la moyenne d'un ensemble de nombres.

    Args:
        numbers (list): liste de nombres

    Returns:
        float: la moyenne des nombres
    """

    average = sum(numbers) / len(numbers)
    return average


# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)

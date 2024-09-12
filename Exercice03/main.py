words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

vowels_lower = [letter.lower() for letter in vowels]
vowels_upper = [letter.upper() for letter in vowels]

def count_vowels(word):
    # Somme de 1 pour chaque lettre voyelle dans le mot
    # Si aucune voyelle n'est trouvée, retourne 0

    return sum(1 for letter in word if letter in vowels_lower or letter in vowels_upper)
    

# On crée un tuple qui contient le mot et le nombre de voyelles
# pour chaque mot dans la liste "words"


result = [(word, count_vowels(word)) for word in words]

print(result)

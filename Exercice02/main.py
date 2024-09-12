# Source d'information :
# https://stackoverflow.com/questions/5202233/how-to-change-39-54484700000000-to-39-54-and-using-python


students = {
    'Alice': {
        'Mathematiques': 90,
        'Francais': 80,
        'Histoire': 95
    },
    'Bob': {
        'Mathematiques': 75,
        'Francais': 85,
        'Histoire': 70
    },
    'Charlie': {
        'Mathematiques': 88,
        'Francais': 92,
        'Histoire': 78
    }
}

while True:
    student_name = input("Entrez le nom du étudiant : ")

    if student_name in students:
        notes = students[student_name]
        print(f"Voici les notes de {student_name} :")

        for school_subject in notes:
            print(f"{school_subject} : {notes[school_subject]}")

        average = sum(notes.values()) / len(notes)
        print(f"Moyenne de {student_name} : {round(average, 2)}")
        # Il existe aussi cette syntaxe :   {average:.2f}
        # qui permet également de formater la valeur avec 2 décimales dans les
        # nouvelles versions de Python
        break
    else:
        print(f"L'étudiant {student_name} n'existe pas dans la liste, "
              "veuillez réessayer.")

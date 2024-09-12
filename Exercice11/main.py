# Écrivez votre code ici !

class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"{amount} € a été déposé sur le compte.")
        else:
            print("Le montant à déposer doit être supérieur à zéro.")

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Fonds insuffisants pour effectuer le retrait.")
        elif amount <= 0:
            print("Le montant à retirer doit être supérieur à zéro.")
        else:
            self.balance -= amount
            print(f"{amount} € a été retiré du compte.")

    def display_balance(self):
        print(f"Titulaire du compte : {self.account_holder}")
        print(f"Solde actuel : {round(self.balance, 2)} €")


# Nouveau compte bancaire d'escroquerie
crook_account = BankAccount("Bernard Madoff", 1000)

# Afficher le solde initial de l'escroc
crook_account.display_balance()

# Déposer de l'argent sur le compte de l'escroc
crook_account.deposit(500)

# Afficher le solde de l'escroc
crook_account.display_balance()

# Retirer de l'argent du compte de l'escroc
crook_account.withdraw(200)

# Afficher le solde de l'escroc
crook_account.display_balance()

# Essayer de retirer plus que le solde
print(f"Tentative de retrait de 2000 € alors que le solde est de {crook_account.balance} €.")
crook_account.withdraw(2000)

# Essayer de retirer de l'argent avec un montant négatif
print(f"Tentative de retrait de -200 € alors que le solde est de {crook_account.balance} €.")
crook_account.withdraw(-200)

# Afficher le solde de l'escroc
crook_account.display_balance()

menu = '''
   ---------- MENU ----------
   
   Selecione uma opção:
   
   1- Deposit
   2- Withdraw
   3- Extract
   4- Exit...
   
   --------------------------
   --> '''

balance = 0
limit = 500
extract = ""
number_of_withdraws = 0
withdraws_limit = 3

while True:
    
    option = str(input(menu))

    if option == "1":
        deposit_value = float(input("Inform the amount for deposit: "))
        if deposit_value > 0:
            balance += deposit_value
            extract += str(f"deposit: + R${deposit_value:.2f}\n")
            print("Deposit succesfull!")
        else:
            print("Failed, the amount is invalid!")
    
    elif option == "2":
        if number_of_withdraws < 3:
            withdraw_value = float(input("Inform the amount for withdraw: "))
            if withdraw_value <= balance:
                if withdraw_value <= limit:
                    balance -= withdraw_value
                    extract += str(f"withdraw: - R${withdraw_value:.2f}\n")
                    number_of_withdraws += 1
                    print("Withdraw succesfull!")
                else:
                    print("Withdraw failed, maximum value per operation exceeded!")
            else:
                print("Withdraw failed, not enough funds.")
        else:
            print("Sorry, you reached the limit of withdraws today...")
    
    elif option == "3":
        if not extract:
            print("\n-----------EXTRACT-----------")
            print(extract)
            print(f"\nBalance: R$ {balance:.2f}")
            print("\n-----------------------------")
        else:
            print("Não foram realizadas movimentações.")

    elif option == "4":
        break

    else:
        print("Invalid option, select an option from the menu.")


import random

def main():
    start = input("Do you wanna play BlackJack, y or n: ")
    if start == 'y' or start == 'yes':
        print(cards())
    else: print("Ok")

def cards():
    print("____________________________________________________")
    while True:
        player1 = []
        computer = []
        gerador_carta(computer)
        for i in range(2):
            carta1 = random.randint(2,11)
            player1.append(carta1)

            # Avisar e começar o while se quiser
        print(f"Your Cards: {player1}, current score: {calculador_de_pontos(player1)}")
        print(f"Computer's first card: {computer[0]}")
        print("___________________________________________")
            

        while calculador_de_pontos(player1) < 21 and calculador_de_pontos(computer) < 21:
            decision = input("Type 'y' to get another card, type 'n' to pass: ")
            if decision == 'n':
                gerador_carta(computer)
                print(f"Your Final Hands: {player1}, current score: {calculador_de_pontos(player1)}")
                print(f"Computer's card: {computer}, current score: {calculador_de_pontos(computer)}")
                if calculador_de_pontos(computer) > 21:
                    print("You won")
                    user_input = input("Do you wanna play BlackJack, y or n: ")
                    if user_input == 'y' or user_input == 'yes':
                        break
                    else: 
                        return "Thanks for playing"
                elif calculador_de_pontos(player1) <= 21 and calculador_de_pontos(player1) > calculador_de_pontos(computer):
                    print("You won")
                    user_input = input("Do you wanna play BlackJack, y or n: ")
                    if user_input == 'y' or user_input == 'yes':
                        break
                    else: 
                        return "Thanks for playing"
                elif calculador_de_pontos(player1) == calculador_de_pontos(computer):
                    print("Draw")
                    user_input = input("Do you wanna play BlackJack, y or n: ")
                    if user_input == 'y' or user_input == 'yes':
                        break
                    else: 
                        return "Thanks for playing"
                else:
                    print("You lost")
                    user_input = input("Do you wanna play BlackJack, y or n: ")
                    if user_input == 'y' or user_input == 'yes':
                        break
                    else: return "Thanks for playing"
                
            gerador_carta(player1)
            gerador_carta(computer)

            print(f"Your Cards: {player1}, current score: {calculador_de_pontos(player1)}")
            print(f"Computer's first card: {computer[0]}")
            print("___________________________________________")

            if 11 in player1:
                caso_11(player1)
                print("The Ace has changed his value, for player")
                print(f"{player1}, and the player values has changed {calculador_de_pontos(player1)}")
                print(f"Computer's first card: {computer[0]}")
                if calculador_de_pontos(player1) > calculador_de_pontos(computer) and calculador_de_pontos(player1) <= 21:
                    pass

            if 11 in computer:
                caso_11(computer)
                pass
            
            if calculador_de_pontos(player1) == 21 and calculador_de_pontos(computer) == 21:
                print("That's a draw")
                user_input = input("Do you wanna play BlackJack, y or n: ")
                if user_input == 'y' or user_input == 'yes':
                    break
                else: return "Thanks for playing"

            elif calculador_de_pontos(player1) > 21:
                print("You Lose 😢")
                user_input = input("Do you wanna play BlackJack, y or n: ")
                if user_input == 'y' or user_input == 'yes':
                    break
                else: return "Thanks for playing"

            elif calculador_de_pontos(player1) == 21:
                if 11 in player1:
                    caso_11(player1)
                    if calculador_de_pontos(player1) <= 21:
                        print("The Ace has changed his value")
                        print(f"{player1}, and the player values has changed {calculador_de_pontos(player1)}")
                        continue
                    else:
                        print("You Lose 😢")
                        user_input = input("Do you wanna play BlackJack, y or n: ")
                        if user_input == 'y' or user_input == 'yes':
                            break
                        else: 
                            return "Thanks for playing"
                print("You win ")
                user_input = input("Do you wanna play BlackJack, y or n: ")
                if user_input == 'y' or user_input == 'yes':
                    break
                else: return f"Thanks for playing"

            elif calculador_de_pontos(computer) > 21:
                print("You win 😀")
                user_input = input("Do you wanna play BlackJack, y or n: ")
                if user_input == 'y' or user_input == 'yes':
                    pass
                else: return f"Thanks for playing"
        
            


def gerador_carta(player:list):
    carta = random.randint(2,11)
    player.append(carta)
    return player

def calculador_de_pontos(player:list):
    contador = 0
    for numero in player:
        contador += numero
    return contador

def caso_11(player:list):
    while sum(player) > 21:
        for i in range(len(player)):
            if player[i] == 11:
                player[i] = 1
                break

        return player

        


if __name__ == '__main__':
    main()

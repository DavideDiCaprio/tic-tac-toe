def print_menu():
    print("\n=== Tic Tac Toe ===")
    print("1. Single Player (vs Random AI)")
    print("2. Two Players")
    print("3. vs Monte Carlo AI")
    print("4. Exit")
    print("==================")

def main():
    while True:
        print_menu()
        choice = input("Select game mode (1-4): ")
        
        if choice == "1":
            while True:
                print("\n" + "*_ "*10 + "NEW MATCH" + " _*"*10 + "\n")
                play_singleplayer()
                if input("\nPlay again? (y/n): ").lower() != 'y':
                    break
                
        elif choice == "2":
            while True:
                print("\n" + "*_ "*10 + "NEW MATCH" + " _*"*10 + "\n")
                play_multiplayer()
                if input("\nPlay again? (y/n): ").lower() != 'y':
                    break
                
        elif choice == "3":
            level = input("Select challenge level (Beginner/Intermediate/Advanced): ")
            while level not in ["Beginner", "Intermediate", "Advanced"]:
                print("Invalid level!")
                level = input("Select challenge level (Beginner/Intermediate/Advanced): ")
            
            while True:
                print("\n" + "*_ "*10 + "NEW MATCH" + " _*"*10 + "\n")
                play_montecarlo(user_selected_challenge_level=level)
                if input("\nPlay again? (y/n): ").lower() != 'y':
                    break
                
        elif choice == "4":
            print("Thanks for playing!")
            break
            
        else:
            print("Invalid choice! Please select 1-4")

if __name__ == "__main__":
    main()
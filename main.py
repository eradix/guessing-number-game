from functions import clean_screen, play_game

if __name__ == '__main__':
    # execute game
    run_game = True
    i = 1
    while run_game:
        game_counter_str = " again?" if i > 2 else "?"
        user_to_play = input(f"\nDo you want to play a number guessing game{game_counter_str} Type 'y' or 'n': ").lower()
        if user_to_play not in ['y','n']:
            print('Invalid input.')
        elif user_to_play == 'n':
            print("Game Terminated. Goodbye!")
            run_game = False
        else:
            clean_screen()
            play_game()
            i += 2
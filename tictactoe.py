# Initiales Spielfeld (9 Felder)
field = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

current_player = "X"
game_running = True

# Speilfeldanzeige
def print_field():
    print()
    print(field[0] + " | " + field[1] + " | " + field[2])
    print("--+---+--")
    print(field[3] + " | " + field[4] + " | " + field[5])
    print("--+---+--")
    print(field[6] + " | " + field[7] + " | " + field[8])
    print()

# Interaktion Spieler
def get_move():
   while True: 
        player_move = input("Wähle ein Feld (1–9): ") 

        if not player_move.isdigit():
            print("Bitte eine Zahl eingeben.")
            continue 

        player_move = int(player_move) - 1  # Python-Listen beginnen bei 0, das Spielfeld bei 1, deshalb muss (-1) gezählt werden.

        if player_move < 0 or player_move > 8:
            print("Zahl muss zwischen 1 und 9 liegen.")
            continue

        if field[player_move] in ["X", "Y"]: # Wenn das gewählte Feld bereits ein X oder ein Y enthält, dann …“
            print("Feld ist bereits belegt.")
            continue

        return player_move

# Gewinnermittlung
def check_win():
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Reihen
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Spalten
        (0, 4, 8), (2, 4, 6)              # Diagonalen
    ]
    # Prüft jede mögliche Gewinnreihe und gibt sofort den Gewinner zurück, wenn gefunden. Sonst None.“
    for a, b, c in win_combinations: # mehrere Elemente gleichzeitig durchgehen
        if field[a] == field[b] == field[c]:
            return field[a] # Gibt zurück, wer auf dieser Gewinnreihe steht, weil er gewonnen hat, und stoppt sofort die Prüfung anderer Reihen.“

    return None

# Auswertung des Unentschiedens
def check_draw():
    return all(cell in ["X", "Y"] for cell in field)
    # Prüft jede Zelle, ob sie besetzt ist, und gibt True zurück, wenn das gesamte Spielfeld voll ist.

# Spielerwechsel
def switch_player():
    global current_player
    current_player = "Y" if current_player == "X" else "X"


# Hauptspiel-Schleife
print("TicTacToe startet!")

while game_running:
    print_field()
    player_move = get_move()
    field[player_move] = current_player

    winner = check_win()
    if winner:
        print_field()
        print(f"Spieler {winner} gewinnt!")
        break

    if check_draw():
        print_field()
        print("Unentschieden!")
        break

    switch_player()

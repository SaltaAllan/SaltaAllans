# function to ask play again or not
def play_again():
  print("\nVill du spela igen? (y or n)")
  
  # convert the player's input to lower_case
  answer = input(">").lower()

  if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()

# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again()

# diamond room
def kladdig_källare():
  # some prompts
  print("\nDu är nu i ett stinkande och kladdigt badrum.")
  print("Och det finns en dörr där.")
  print("vad gör du då? (1 or 2)")
  print("1). Tar med lite av kladdet innan jag går ut genom dörren.")
  print("2). Går bara igenom dörren.")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead, call game_over() function with the "reason"
    game_over("Kladdet var salt och du avled strax efter att du passerat dörren.")
  elif answer == "2":
    # the player won the game
    print("\nFinemang, du lämnade utan kladdet. Du kan nu gå hem till din familj som undrar var du tog vägen.")
    # activate play_again() function
    play_again()
  else:
    # call game_over() with "reason"
    game_over("Lär dig att salta fläsket rätt.")

# monster room
def Tages_trädgård():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nNu möter du din granne Tage, face to face.")
  print("Men Tage är gammal och verkningslös.\nBakom Tage finns en annan, lockande dörr. Vad gör du härnäst? (1 or 2)")
  print("1). Finta Tage och passera dörren")
  print("2). Piska Tage med trädgårdsslangen och visa ditt mod!")

  # take input()
  answer = input(">")

  if answer == "1":
    # lead him to the diamond_room()
    kladdig_källare()
  elif answer == "2":
    # the player is dead, call game_over() with "reason"
    game_over("Tyvärr var Tage's glock snabbare än trädgårdslangens piskande")
  else:
    # game_over() with "reason"
    game_over("Lär dig att snärta klinten!")

# bear room
def Torstens_dungeon():
  # give some prompts
  # '\n' is to print the line in a new line
  print("\nDet är en Torsten här.")
  print("Bakom Torsten finns en garagedörr.")
  print("Torsten sitter på huk och äter kedjan till sin cykel")
  print("Vad gör du? (1 or 2)")
  print("1). Ta cykelkedjan ifrån Torsten.")
  print("2). Reta Torsten med en pinne.")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead!
    game_over("Torsten dödade dig med cykelkedjan.")
  elif answer == "2":
    # lead him to the diamond_room()
    print("\nDu har tur idag. Torsten vek sig undan.")
    kladdig_källare()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Kan du inte finta Torsten?")

def start():
  # give some prompts.
  print("\nDu står på din farstukvist. Tage frågar om det är din katt på hans tomt, och Torsten äter cykelkedjor.")
  print("Du kan gå till Tage och tala om katten eller möta Torsten. Vart går du? (l or r)")
  
  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    # if player typed "left" or "l" lead him to bear_room()
    Torstens_dungeon()
  elif "r" in answer:
    # else if player typed "right" or "r" lead him to monster_room()
    Tages_trädgård()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Är du feg? Kan du inte ta dig vidare?")


# start the game
start()
# Sai Nikhil Reddy Anumula

# Movie Highlights with Distinguishing Features:
# 13 GHOSTS (1960): A supernatural film renowned for its illusion-O process.
# A CHRISTMAS CAROL (1938): Classic film from the 1930s.
# AMERICAN PSYCHO (2000): A film inspired by a novel.
# BELOW (2002): Set on a sunken ship.
# CARNIVAL OF SOULS (1962): Revolves around a woman surviving a car accident.
# CITY STREETS (1931): A tale of lovers ensnared by gangsland connections.
# G-MEN (1935): Unfolds in the Midwest.
# GODFATHER (1990): Renowned gangster saga.
# GOODFELLAS (1990): Based on the life of an actual ex-mobster.
# HEAVEN CAN WAIT (1978): Incorporates football.
# HOLD THAT GHOST (1941): A comedic venture.
# INTERNAL AFFAIRS (1990): Explores the world of two undercover moles.
# MILLER'S CROSSING (1990): Involves an Irish mob leader-gangster.
# SUSPECT ZERO (2004): Features an ex-FBI agent obsessed with killing serial killers.
# THE BIGHOUSE (1930): One of the earliest prison films.
# THE GHOST SHIP (2002): Unfolds in the eerie setting of a sunken ship.
# THE LEGEND OF HELL HOUSE (1973): Researchers spend time in a haunted house.
# THE PLEDGE (2001): Focuses on a retired cop.
# THE RING (2002): A remake of Hideo Nakata's Japanese film.
# TOPPER (1937): Explores the aftermath of a couple's car accident.

print("Hey! Do you need Instructions?", end="")
if input() in ['yes','YES']:
    print("There are 20 movie names below from two subgenres - Crime and Supernatural")
    print("Choose a movie that interests you and keep it in your mind")
    print("Answer yes/no to the questions following in order to guess your choice")
else:
    print("Perfect! We are ready to play!")

print("Pick a movie from the list and keep it in your mind")
print("--------------------------------------------------------")
print("1. 13 GHOSTS           ||   11. HOLD THAT GHOST")
print("2. A CHRISTMAS CAROL   ||   12. INTERNAL AFFAIRS")
print("3. AMERICAN PSYCHO     ||   13. MILLER'S CROSSING")
print("4. BELOW               ||   14. SUSPECT ZERO")
print("5. CARNIVAL OF SOULS   ||   15. THE BIGHOUSE")
print("6. CITY STREETS        ||   16. THE GHOST SHIP")
print("7. G-MEN               ||   17. THE LEGEND OF HELL HOUSE")
print("8. GODFATHER III       ||   18. THE PLEDGE")
print("9. GOODFELLAS          ||   19. THE RING")
print("10. HEAVEN CAN WAIT    ||   20. TOPPER")
print("--------------------------------------------------------")
print("Pick one from two sub-genres: 'Supernaturals' and 'Crime and Gangster'")

print("Do you want to pick a film from supernaturals?", end="")
if input() in ['yes','YES']:
    print("Was this film between 1935 and 1945?", end="")
    if input() in ['yes', 'YES']:
        print("Is it about a couple who were involved in a car accident?", end="")
        if input() in ['yes', 'YES']:
            print("The film in your mind is 'TOPPER'!")
        else:
            print("Does it include comedy?", end="")
            if input() in ['yes','YES']:
                print("The film in your mind id 'HOLD THAT GHOST'!")
            else:
                print("The film in your mind is 'A CHRISTMAS CAROL'!")
    else:
        print("Was the film between 1960 and 1980?", end="")
        if input() in ['yes', 'YES']:
            print("Is it memorable for its illusion-o process?", end="")
            if input() in ['yes', 'YES']:
                print("The film in your mind is '13 GHOSTS'!")
            else:
                print("Was it a woman who survived car accident?", end="")
                if input() in ['yes', 'YES']:
                    print("The film in your mind is 'CARNIVAL OF SOULS'!")
                else:
                    print("Is it about four researchers who spent a week in a house inhabited by spirituals?", end="")
                    if input() in ['yes','YES']:
                        print("The film in your mind is 'THE LEGEND OF HELL HOUSE'!")
                    else:
                        print("The film in your mind is 'HEAVEN CAN WAIT'!")
        else:
            print("Was it a remake of Hideo Nakata's Japanese film?",  end="")
            if input() in ['yes', 'YES']:
                print("The film in your mind is 'THE RING'!")
            else:
                print("Does the film's name contain the letter 'G'?", end="")
                if input() in ['yes', 'YES']:
                    print("The film in your mind is 'THE GHOST SHIP'!")
                else:
                    print("The film in your mind is 'BELOW'!")

else:
    print("Was the film between 1930 and 1935?", end="")
    if input() in ['yes', 'YES']:
        print("Was it famed as one of the earliest prison?", end="")
        if input() in ['yes', 'YES']:
            print("The film in your mind is 'THE BIGHOUSE'!")
        else:
            print("Was it about two lovers trapped by gangland connections?", end="")
            if input() in ['yes', 'YES']:
                print("The film in your mind is 'CITY STREETS'!")
            else:
                print("The film in your mind is 'G-MEN'!")
    else:
        print("Was the film in the year 1990?",end="")
        if input() in ['yes', 'YES']:
            print("Was it based on the life of an actual ex-mobster?",end="")
            if input() in ['yes', 'YES']:
                print("The film in your mind is 'GOODFELLAS'!")
            else:
                print("Was it popular as gangster saga?", end="")
                if input() in ['yes', 'YES']:
                    print("The film in your mind is 'GODFATHER'!")
                else:
                    print("Does it involve irish mob leader-gangster?", end="")
                    if input() in ['yes', 'YES']:
                        print("The film in your mind is 'MILLER'S CROSSING'!")
                    else:
                        print("The film in your mind is 'Internal Affairs'!")
        else:
            print("Was the film inspired by a novel?", end="")
            if input() in ['yes', 'YES']:
                print("The film in your mind is 'AMERICAN PSYCHO'!")
            else:
                print("Was it about a retired cop?", end="")
                if input() in ['yes', 'YES']:
                    print("The film in your mind is 'THE PLEDGE'!")
                else:
                    print("The film in your mind is 'SUSPECT ZERO'!")


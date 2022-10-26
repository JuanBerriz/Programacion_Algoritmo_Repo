#Programacion orientada a objetos
from Valid import Valid
from Race import Race
from Horse import Horse

def main():
    print("Welcome to the Kentucky Derby")
    valids = int(input("Please enter how many valids will occur today: "))
    races = int(input("How many races per valid?: "))
    caballo1 = Horse("El rayo Veloz", 1)
    caballo2 = Horse("Superman", 2)
    caballo3 = Horse("Jose", 3)
    caballo4 = Horse("Blackjack", 4)
    caballo5 = Horse("Crack", 5)
    caballo6 = Horse("El rayo Lento", 6)
    
    for valid in range(valids):
        race_list = []
        horse_list = [caballo1, caballo2, caballo3 ,caballo4 ,caballo5, caballo6]
        for race in range(races):
            race_list.append(Race(race, horse_list))
        for race in race_list:
            race.start_race()
            race.winning_horse()

    return

main()
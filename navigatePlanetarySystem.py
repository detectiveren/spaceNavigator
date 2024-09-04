# Navigate Planetary System script for spaceNavigator
import planetary_system


# Imports handled above this comment


def searchForPlanetarySystem(planetarySystem, currentPlanet):
    """Searches for the planetary system entered by the user"""
    try:
        planetarySystemInfo = planetary_system.getPlanetarySystems(planetarySystem)
        numberOfPlanets = planetarySystemInfo[0]
        binarySystem = planetarySystemInfo[1]
        lightYears = planetarySystemInfo[2]
        habitablePlanets = planetarySystemInfo[3]
        numberOfHabitablePlanets = planetarySystemInfo[4]
        starName = planetarySystemInfo[5]
        planetarySystemName = planetarySystemInfo[6]
        potentiallyHabitablePlanets = planetarySystemInfo[7]

        print(f"Planetary System: {planetarySystemName}\n\n")
        print(f"Number of planets in the {planetarySystemName}: {numberOfPlanets}\n")
        if binarySystem:
            print(f"The {planetarySystemName} is a binary system\n")
        else:
            print(f"The {planetarySystemName} is not a binary system\n")
        if lightYears == 0:
            # Change this so that if the planet is within the planetary system dictionary it will print this
            # instead of saying it is 0 light years away
            print(f"{currentPlanet} is part of the {planetarySystemName}\n")
        else:
            print(f"The {planetarySystemName} is {lightYears} away from {currentPlanet}\n")

        print(f"Habitable Planets in the {planetarySystemName}:")
        for i in habitablePlanets:  # Prints out all the habitable planets within the habitablePlanets list
            print(i)
        print(f"\nNumber of Habitable Planets in the {planetarySystemName}: {numberOfHabitablePlanets}\n")
        print(f"The name of the star in the {planetarySystemName}: {starName}\n")
        print(f"\nPotentially Habitable Planets in the {planetarySystemName}:")
        for i in potentiallyHabitablePlanets:
            # Prints out all the habitable planets within the potentiallyHabitablePlanets list
            print(i)
    except:
        print(f"Planetary System \"{planetarySystem}\" not in Planetary System Dictionary, it may be added later")


def userSearch():
    planetarySystemName = input("Enter a planetary system (be precise): ")
    searchForPlanetarySystem(planetarySystemName, "Earth")

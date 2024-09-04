# Planetary System script for spaceNavigator

# Imports handled above this comment

class PlanetarySystem:
    """Planetary System class where information about a planetary system can be defined"""
    def __init__(self, numberOfPlanets, binarySystem, lightYears, habitablePlanets, numberOfHabitablePlanets,
                 starName, planetarySystemName, potentiallyHabitablePlanets):
        self.numberOfPlanets = numberOfPlanets
        self.binarySystem = binarySystem
        self.lightYears = lightYears
        self.habitablePlanets = habitablePlanets
        self.numbersOfHabitablePlanets = numberOfHabitablePlanets
        self.starName = starName
        self.planetarySystemName = planetarySystemName
        self.potentiallyHabitablePlanets = potentiallyHabitablePlanets


planetarySystems = {  # Dictionary containing planetary systems and the information about the planetary systems
    "Solar System": PlanetarySystem("8", False, 0, ["Earth"],
                                    1, "The Sun", "Solar System",
                                    ["Mars"])
}


def getPlanetarySystems(selection):
    """This grabs information from the planetarySystems dictionary"""
    getInfo = planetarySystems.get(selection)
    if isinstance(getInfo, list):
        return [list(vars(item).values()) for item in getInfo]
    elif getInfo is not None:
        return list(vars(getInfo).values())
    else:
        return getInfo

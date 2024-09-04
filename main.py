# Space Navigator main script to load other scripts
import navigatePlanetarySystem


# Imports handled above this comment

def welcomeMessage(datasetMode):
    """Prints out the necessary info about the application"""
    title = "spaceNavigator"
    version = "1.0"
    supported_planetary_systems = [  # The list of planetary systems supported
        'Solar System'
    ]
    if datasetMode:
        datasetInfo = "Dataset Mode enabled"  # Dataset Mode hasn't been made yet
    else:
        datasetInfo = "Dataset Mode not enabled"

    print(f"{title}\nVersion: {version}\n{datasetInfo}\n\nSupported Planetary Systems: ")

    for i in supported_planetary_systems:  # Prints all the supported planetary systems in the list
        print(i)


def main():
    """Where all the scripts are ran and configured"""
    datasetVersion = False  # If set to false then dataset mode won't be enabled
    stayInApplication = True  # To bring you back to the menu instead of ending the application
    welcomeMessage(datasetVersion)
    while stayInApplication:
        print("1. Planetary System Search")
        selection = int(input("Enter the number to enter the mode: "))

        if selection == 0:
            stayInApplication = 0  # This will end the application
        if selection == 1:
            navigatePlanetarySystem.userSearch()
            # This will bring you to the search function to search for info on a planetary system


if __name__ == '__main__':  # The program starts here
    main()

#  Application needs to be built to have details on planets within planetary systems along with their moons and the
#  details about those moons among other things

#  Application needs to be able to handle large amount of datasets about planets and planetary systems from NASA, ESA, etc

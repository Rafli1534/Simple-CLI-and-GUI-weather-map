def hello() -> None:
    print("Hello my dear user! If you want to see the weather,\n" \
    "would u so please to write ur APPID key from urs " \
    "OpenWeather account!\n\n" \
    "but if u don't have it, u can sign in, and then write " \
    "it here!\n" \
    "Don't worry, u don't have to search this site. Here it is!\n" \
    "After writing it, u can successfuly use this project!\n" \
    "https://home.openweathermap.org/users/sign_in \n" \
    "Enjoy your time!")

def appid() -> str:
    """Prompt for OpenWeather APPID and require exactly 32 
    characters.

    Keeps prompting until the user provides a 32-character key,
    then returns it.
    """
    while True:
        key = str(input("Write your OpenWeather APPID: ")).strip()
        if len(key) == 32:
            return key
        print(
            "APPID must be exactly 32 characters long. " \
            "Please try again."
            )
        
def save_appid(appid: str, filename: str = 'appid.txt') -> None:
    with open(filename, 'w') as f:
        f.write(appid)

def load_appid(filename: str = 'appid.txt') -> str:
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return ''
        
def get_city() -> str:
    """Prompt user for a city name, normalize and return it."""
    return str(input(
        "Write a name of city/town you need: "
        )).strip().lower()

def choose_units() -> str:
    """Prompt user to choose units and return OpenWeather 'units'
 value.

    Returns 'metric' for Celsium and 'imperial' for Fahrenheit.
    """
    while True:
        try:
            choice = int(input(
                "Choose type of degree:" \
                "\n1. Celsius" \
                "\n2. Fahrenheit" \
                "\n   - "))
        except ValueError:
            print("Please enter 1 or 2")
            continue
        if choice == 1:
            return 'metric'
        elif choice == 2:
            return 'imperial'
        else:
            print("Unknown choice, try again")

def choose_language() -> str:
    """Prompt user to choose language and return language code."""
    while True:
        try:
            choice = int(input("Choose the language:" \
            "\n1. Ukrainian" \
            "\n2. English" \
            "\n3. russian" \
            "\n  - "))
        except ValueError:
            print("Please enter 1, 2 or 3")
            continue
        if choice == 1:
            return 'ua'
        elif choice == 2:
            return 'en'
        elif choice == 3:
            return 'ru'
        else:
            print("Unknown choice, try again")

def choose_mode_cli() -> str:
    """Ask user whether they want current weather, forecast, or both."""
    while True:
        try:
            choice = int(input("Choose mode:" \
            "\n1. Current weather" \
            "\n2. 5-day forecast" \
            "\n3. Both\n  - "
            ))
        except ValueError:
            print("Please enter 1, 2 or 3")
            continue
        if choice == 1:
            return 'current'
        elif choice == 2:
            return 'forecast'
        elif choice == 3:
            return 'both'
        else:
            print("Unknown choice, try again")

def get_city_from_params(params):
    return params.get('q', '').title()

def get_unit_from_params(params):
    return params.get('units')

def get_lang_from_params(params):
    return params.get('lang')

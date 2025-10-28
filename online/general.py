from project.gui import run_gui
from project.utils import(
    hello,
    appid,
    get_city,
    choose_units,
    choose_language,
    choose_mode_cli,
    
)
from project.weather_api import (
    run_current,
    run_forecast,

)

def main_action():
    mode = input("Choose mode:\n1. CLI\n2. GUI\n- ").strip()
    if mode == "2":
        run_gui()
        return
    else:
        hello()
        ad = appid()
        city = get_city()
        units = choose_units()
        lang = choose_language()
        mode = choose_mode_cli()

        if mode == "current":
            run_current(ad, city, units, lang)
        elif mode == "forecast":
            run_forecast(ad, city, units, lang)
        elif mode == "both":
            run_current(ad, city, units, lang)
            run_forecast(ad, city, units, lang)
        else:
            print("Unknown mode.")

        if lang == 'en':
            input(
            "\nPress 'Enter' when u want to finish the program..."
            )
        elif lang == 'ua':
            input(
            "\nНатисніть Enter коли захочете закінчити программу..."
            )
        else:
            input(
            "\nНажмите Enter когда захотите закончить программу..."
            )

if __name__ == '__main__':
    main_action()

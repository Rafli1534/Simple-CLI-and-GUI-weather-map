from project.gui import run_gui
from project.utils import run_cli

def main_action():
    mode = input("Choose mode:\n1. CLI\n2. GUI\n- ").strip()
    if mode == "2":
        run_gui()
        return
    else:
        run_cli()
        return 

if __name__ == '__main__':
    main_action()

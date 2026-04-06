from project.starts import (
    run_cli, 
    run_gui
)

def main_action():
    mode = input("Choose mode:\n1. CLI\n2. GUI\nUr choice: ").strip()
    if mode == '1':
        run_cli()
        return 
    elif mode == '2':
        run_gui()
        return 
    else:
        print("No such variant")
        return 

if __name__ == '__main__':
    main_action()

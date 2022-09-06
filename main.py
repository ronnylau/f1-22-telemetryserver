from telemetry import collector, analyzer
import fastf1
import os

fastf1.Cache.enable_cache('cache')


def clear_console():
    if os.name == 'nt':
        os.system('cls')

    else:
        os.system('clear')


if __name__ == '__main__':
    print('F1 22 Telemetry')
    print('')
    print('Select action:')
    print('1. Record Session')
    print('2. Analyze Data')
    print('3. Exit')
    print('')
    selection: str = input('Enter number: ')

    try:
        int(selection)
        match int(selection):
            case 1:
                print('Starting Telemetry collection...')
                clear_console()
                collector.receive_data()

            case 2:
                clear_console()
                analyzer.analyze_data()

            case 3:
                print('Exit')

            case _:
                print('Invalid input, exiting program!')

    except ValueError:
        print('Invalid input, exiting program!')

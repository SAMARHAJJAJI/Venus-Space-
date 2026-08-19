def show_welcome():
    print("Welcome to Venus Space")
    print("Design a space that feels like you")


def choose_option(options, message):
    print()
    print(message)

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    while True:
        try:
            choice = int(input("Enter your choice: "))

            if 1 <= choice <= len(options):
                selected_option = options[choice - 1]
                break
            else:
                print(
                    "Invalid choice. "
                    "Please choose a number from the list."
                )

        except ValueError:
            print("Please enter a number.")

    return selected_option


def get_positive_number(message):
    while True:
        try:
            number = float(input(message))

            if number > 0:
                return number
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")
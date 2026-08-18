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
                print("Invalid choice. Please choose a number from the list.")

        except ValueError:
            print("Please enter a number.")

    return selected_option


show_welcome()

room_name = input("What room are you designing? ")

styles = ["Minimal", "Cozy", "Modern", "Scandinavian"]
room_style = choose_option(styles, "Choose your interior style:")

colors = ["Beige", "White", "Sage Green", "Dusty Pink", "Brown"]
main_color = choose_option(colors, "Choose your main color:")

materials = ["Wood", "Metal", "Glass", "Stone", "Fabric"]
favorite_material = choose_option(materials, "Choose your favorite material:")

room_width = float(input("Enter room width in meters: "))
room_length = float(input("Enter room length in meters: "))
room_area = room_width * room_length

if room_area < 10:
    room_size = "Compact"
    recommendation = (
        "Light colors and multifunctional furniture "
        "can help the room feel more open."
    )
elif room_area < 20:
    room_size = "Medium"
    recommendation = "You have enough space for a balanced layout."
else:
    room_size = "Spacious"
    recommendation = "You have a lot of space to work with!"

room_budget = float(input("Enter your budget in yen: "))

print()
print("Room Summary")
print("------------------------------")
print(f"Room: {room_name}")
print(f"Style: {room_style}")
print(f"Main Color: {main_color}")
print(f"Favorite Material: {favorite_material}")
print(f"Area: {room_area:.2f} m²")
print(f"Room Size: {room_size}")
print(f"Budget: ¥{room_budget:.2f}")
print(f"Recommendation: {recommendation}")
print("------------------------------")

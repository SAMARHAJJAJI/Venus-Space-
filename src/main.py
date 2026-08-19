from helpers import show_welcome, choose_option, get_positive_number
from styles import styles, style_details
show_welcome()

room_types = [
    "Bedroom",
    "Living Room",
    "Home Office",
    "Dining Room"
]
room_name = choose_option( room_types, "What room are you designing?"
)

room_style = choose_option(styles, "Choose your interior style:")
selected_style = style_details[room_style]
colors = ["Beige", "White", "Sage Green", "Dusty Pink", "Brown", "Cream", "Warm Brown"]
print()
print(f"{room_style} Style Details")
print(f"Mood: {selected_style['mood']}")
print(f"Lighting: {selected_style['lighting']}")

print("Recommended Colors:")
for color in selected_style["colors"]:
    print(f"- {color}")
main_color = main_color = choose_option(
    selected_style["colors"],
    "Choose your main color:"
)


materials = ["Wood", "Metal", "Glass", "Stone", "Fabric"]
print("Recommended Materials:")
for material in selected_style["materials"]:
    print(f"- {material}")
favorite_material = choose_option(
    selected_style["materials"],
    "Choose your favorite material:"
)

room_width = get_positive_numbers("Enter room width in meters: ")
room_length = get_positive_numbers("Enter room length in meters: ")
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

room_budget = get_positive_numbers("Enter your budget in yen: ")

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
# First dictionary experiment



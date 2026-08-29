from helpers import show_welcome, choose_option, get_positive_number
from styles import styles, style_details
from data import room_types , room_details

show_welcome()

     # ---------------- ROOM ----------------


room_name = choose_option( room_types, "What room are you designing?"
)
selected_room = room_details[room_name]
print()
print(f"{room_name} Design")
print(f"Purpose: {selected_room['purpose']}")
print(f"Design Focus: {selected_room['focus']}")

    # ---------------- STYLE ----------------


room_style = choose_option(styles, "Choose your interior style:")
selected_style = style_details[room_style]
#colors = ["Beige", "White", "Sage Green", "Dusty Pink", "Brown", "Cream", "Warm Brown"]
print()
print(f"{room_style} Style Details")
print(f"Mood: {selected_style['mood']}")
print(f"Lighting: {selected_style['lighting']}")


    # ---------------- COLOR ----------------


print("Recommended Colors:")
for color in selected_style["colors"]:
    print(f"- {color}")
main_color = choose_option(
    selected_style["colors"],
    "Choose your main color:"
)

    # ---------------- MATERIAL ----------------


#materials = ["Wood", "Metal", "Glass", "Stone", "Fabric"]
print("Recommended Materials:")
for material in selected_style["materials"]:
    print(f"- {material}")
favorite_material = choose_option(
    selected_style["materials"],
    "Choose your favorite material:"
)

    # ---------------- DESIGN TIP ----------------


if room_name == "Bedroom" and room_style == "Cozy":
    design_tip = (
        "Use warm lighting, soft fabrics, and comfortable "
        "furniture to create a relaxing bedroom."
    )

elif room_name == "Home Office" and room_style == "Minimal":
    design_tip = (
        "Keep the workspace clean and organized with natural "
        "lighting and simple furniture."
    )

else:
    design_tip = (
        f"Use the {room_style} style while keeping the "
        f"{room_name} practical and comfortable."
    )


    # ---------------- ROOM DIMENSIONS ----------------


print()
print("Room Dimensions")
room_width = get_positive_number("Enter room width in meters: ")
room_length = get_positive_number("Enter room length in meters: ")
room_area = room_width * room_length


     # ---------------- ROOM SIZE ----------------


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


     # ---------------- BUDGET ----------------


room_budget = get_positive_number("Enter your budget in yuan: ")

     # ---------------- FINAL SUMMARY ----------------


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
print(f"Design Tip: {design_tip}")
print("------------------------------")
# First dictionary experiment



from helpers import show_welcome, choose_option, get_positive_number
from styles import styles, style_details
from data import room_types, room_details, design_recommendations , room_size_recommendations , budget_scope
from furniture import furniture_prices
from decorations import decoration_prices

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

    # ---------------- DESIGN RECOMMENDATION ----------------

design = design_recommendations[(room_name, room_style)]


    # ---------------- ROOM DIMENSIONS ----------------


print()
print("Room Dimensions")
room_width = get_positive_number("Enter room width in meters: ")
room_length = get_positive_number("Enter room length in meters: ")
room_area = room_width * room_length


     # ---------------- ROOM SIZE ----------------


if room_area < 10:
    room_size = "Compact"
elif room_area < 20:
    room_size = "Medium"
else:
    room_size = "Spacious"

size_advice = room_size_recommendations[room_size]


   # ---------------- BUDGET ----------------

room_budget = get_positive_number("Enter your budget in yuan: ")

budget_scope = choose_option(
    budget_scope,
    "How should we use your budget?"
)


# Calculate furniture cost
furniture_total = 0

for furniture in design["furniture"]:
    furniture_total += furniture_prices[furniture]


# Calculate decoration cost
decoration_total = 0

if budget_scope == "Furniture and decoration":
    for decoration in decoration_prices:
        decoration_total += decoration_prices[decoration]


# Calculate the final estimated cost
total_estimated_cost = furniture_total + decoration_total


# Compare the total cost with the budget
if total_estimated_cost <= room_budget:
    budget_status = "Within budget"
else:
    budget_status = "Over budget"

   

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

print("Room Size Advice:")
print(f"Layout: {size_advice['layout']}")
print(f"Furniture: {size_advice['furniture']}")
print(f"Color: {size_advice['color']}")

print(f"Design Tip: {design['tip']}")
print(f"Lighting: {design['lighting']}")
print(f"Atmosphere: {design['atmosphere']}")

print("Furniture Suggestions:")
for furniture in design["furniture"]:
    print(f"- {furniture}")

print(f"Budget Scope: {budget_scope}")
print(f"Estimated Furniture Cost: ¥{furniture_total:.2f}")

if budget_scope == "Furniture and decoration":
    print(f"Estimated Decoration Cost: ¥{decoration_total:.2f}")

print(f"Total Estimated Cost: ¥{total_estimated_cost:.2f}")
print(f"Budget Status: {budget_status}")
print("------------------------------")
# First dictionary experiment




from helpers import show_welcome, choose_option, get_positive_number
from styles import styles, style_details
from data import (
    room_types,
    room_details,
    design_recommendations,
    room_size_recommendations,
    budget_scopes
)
from furniture import furniture_prices
from decorations import decoration_prices
from Design_costs import lighting_prices, material_prices_per_m2

def calculate_room_size(room_area):
    if room_area < 10:
        return "Compact"
    elif room_area < 20:
        return "Medium"
    else:
        return "Spacious"

# ---------------- WELCOME ----------------

show_welcome()


# ---------------- ROOM ----------------

room_name = choose_option(
    room_types,
    "What room are you designing?"
)

selected_room = room_details[room_name]

print()
print(f"{room_name} Design")
print(f"Purpose: {selected_room['purpose']}")
print(f"Design Focus: {selected_room['focus']}")


# ---------------- STYLE ----------------

room_style = choose_option(
    styles,
    "Choose your interior style:"
)

selected_style = style_details[room_style]

print()
print(f"{room_style} Style Details")
print(f"Mood: {selected_style['mood']}")
print(f"Lighting: {selected_style['lighting']}")


# ---------------- COLOR ----------------

print()
print("Recommended Colors:")

for color in selected_style["colors"]:
    print(f"- {color}")

main_color = choose_option(
    selected_style["colors"],
    "Choose your main color:"
)


# ---------------- MATERIAL ----------------

print()
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

room_width = get_positive_number(
    "Enter room width in meters: "
)

room_length = get_positive_number(
    "Enter room length in meters: "
)

room_area = room_width * room_length


# ---------------- ROOM SIZE ----------------

room_size = calculate_room_size(room_area)

size_advice = room_size_recommendations[room_size]


# ---------------- BUDGET ----------------

print()
room_budget = get_positive_number(
    "Enter your budget in yuan: "
)

budget_scope = choose_option(
    budget_scopes,
    "How should we use your budget?"
)


# ---------------- FURNITURE COST ----------------

furniture_total = 0

for furniture in design["furniture"]:
    furniture_total += furniture_prices[furniture]


# ---------------- DECORATION COST ----------------

decoration_total = 0

if budget_scope in [
    "Furniture and decoration",
    "Complete room design"
]:
    for decoration in decoration_prices:
        decoration_total += decoration_prices[decoration]


# ---------------- LIGHTING AND MATERIAL COST ----------------

lighting_total = 0
material_total = 0

if budget_scope == "Complete room design":

    lighting_name = selected_style["lighting"]
    lighting_total = lighting_prices[lighting_name]

    material_price = material_prices_per_m2[favorite_material]
    material_total = room_area * material_price


# ---------------- TOTAL COST ----------------

total_estimated_cost = (
    furniture_total
    + decoration_total
    + lighting_total
    + material_total
)


# ---------------- BUDGET STATUS ----------------

if total_estimated_cost <= room_budget:
    budget_status = "Within budget"
else:
    budget_status = "Over budget"


# ---------------- FINAL SUMMARY ----------------

print()
print("Room Summary")
print("------------------------------")

# your other summary print statements go here

print(f"Total Estimated Cost: ¥{total_estimated_cost:.2f}")
print(f"Budget Status: {budget_status}")


# Add the new code here

if budget_status == "Over budget":
    print()

    client_action = choose_option(
        budget_actions,
        "How would you like to continue?"
    )

    print()
    print(f"You selected: {client_action}")

    if client_action == "Keep the current design":
        print(
            "Excellent choice. We will keep the selected design "
            "and preserve the quality of the recommended items."
        )

    elif client_action == "Find lower-cost alternatives":
        print(
            "We can look for more affordable furniture and materials "
            "while keeping the same overall atmosphere."
        )

    elif client_action == "Discuss a possible discount":
        print(
            "We can review the design together and discuss whether "
            "a discount or special package is available."
        )

else:
    print()
    print(
        "Your design fits within the budget. "
        "We can now focus on refining the final details."
    )

print("------------------------------")
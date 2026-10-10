from helpers import show_welcome, choose_option, get_positive_number
from styles import styles, style_details
from data import (
    room_types,
    room_details,
    design_recommendations,
    room_size_recommendations,
    budget_scopes,
    budget_actions
)
from furniture import furniture_prices
from decorations import decoration_prices
from design_costs import lighting_prices, material_prices_per_m2

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
    furniture_total += furniture_prices[room_name][furniture]


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

print(f"Room: {room_name}")
print(f"Style: {room_style}")
print(f"Main Color: {main_color}")
print(f"Favorite Material: {favorite_material}")
print(f"Room Area: {room_area:.1f} m²")
print(f"Room Size: {room_size}")
print()
print("Size Advice:")
print(f"- Layout: {size_advice['layout']}")
print(f"- Furniture: {size_advice['furniture']}")
print(f"- Color: {size_advice['color']}")
print()
print("Cost Breakdown:")
print(f"- Furniture: ¥{furniture_total:.2f}")
print(f"- Decoration: ¥{decoration_total:.2f}")
print(f"- Lighting: ¥{lighting_total:.2f}")
print(f"- Materials: ¥{material_total:.2f}")
print(f"- Total Estimated Cost: ¥{total_estimated_cost:.2f}")
print(f"- Your Budget: ¥{room_budget:.2f}")

budget_difference = abs(room_budget - total_estimated_cost)
print(f"Budget Status: {budget_status} (difference: ¥{budget_difference:.2f})")


# ---------------- OVER BUDGET / WITHIN BUDGET ----------------

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
        print()
        print("Budget-Friendly Suggestions:")

        cheapest_name = min(
            furniture_prices[room_name],
            key=furniture_prices[room_name].get
        )
        cheapest_price = furniture_prices[room_name][cheapest_name]

        new_furniture_total = 0

        for furniture in design["furniture"]:
            old_price = furniture_prices[room_name][furniture]
            new_furniture_total += cheapest_price
            print(
                f"- Swap '{furniture}' (¥{old_price}) "
                f"for '{cheapest_name}' (¥{cheapest_price})"
            )

        savings = furniture_total - new_furniture_total
        print(f"New furniture total: ¥{new_furniture_total:.2f}")
        print(f"You save: ¥{savings:.2f}")

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
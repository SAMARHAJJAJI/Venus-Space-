import tkinter as tk
from data import (
    room_types,
    room_details,
    design_recommendations,
    budget_scopes
)
from styles import styles, style_details
from furniture import furniture_prices
from decorations import decoration_prices
from design_costs import lighting_prices, material_prices_per_m2


def update_style_choices(*args):
    selected_style = style_var.get()
    details = style_details[selected_style]

    color_var.set(details["colors"][0])
    material_var.set(details["materials"][0])

    color_menu["menu"].delete(0, "end")
    for color in details["colors"]:
        color_menu["menu"].add_command(
            label=color, command=tk._setit(color_var, color)
        )

    material_menu["menu"].delete(0, "end")
    for material in details["materials"]:
        material_menu["menu"].add_command(
            label=material, command=tk._setit(material_var, material)
        )

    style_info_label.config(
        text=f"Mood: {details['mood']}   |   Lighting: {details['lighting']}"
    )


def estimate_cost():
    room = room_var.get()
    style = style_var.get()
    scope = scope_var.get()

    try:
        width = float(width_entry.get())
        length = float(length_entry.get())
        budget = float(budget_entry.get())
    except ValueError:
        result_label.config(
            text="Please enter valid numbers for width, length and budget."
        )
        return

    if width <= 0 or length <= 0 or budget <= 0:
        result_label.config(text="Numbers must be greater than 0.")
        return

    area = width * length

    design = design_recommendations[(room, style)]

    furniture_total = 0
    for item in design["furniture"]:
        furniture_total += furniture_prices[room][item]

    decoration_total = 0
    if scope in ["Furniture and decoration", "Complete room design"]:
        for price in decoration_prices.values():
            decoration_total += price

    lighting_total = 0
    material_total = 0
    if scope == "Complete room design":
        lighting_total = lighting_prices[style_details[style]["lighting"]]
        material_total = area * material_prices_per_m2[material_var.get()]

    total = (
        furniture_total
        + decoration_total
        + lighting_total
        + material_total
    )

    if total <= budget:
        status = f"Within budget (difference: ¥{budget - total:.2f})"
    else:
        status = f"Over budget (difference: ¥{total - budget:.2f})"

    result_label.config(
        text=(
            f"Room Area: {area:.1f} m²\n"
            f"Furniture: ¥{furniture_total:.2f}\n"
            f"Decoration: ¥{decoration_total:.2f}\n"
            f"Lighting: ¥{lighting_total:.2f}\n"
            f"Materials: ¥{material_total:.2f}\n"
            f"Total: ¥{total:.2f}\n"
            f"Budget: ¥{budget:.2f}\n"
            f"Status: {status}"
        )
    )


# ---------------- BUILD THE WINDOW ----------------

window = tk.Tk()
window.title("Venus Space")
window.geometry("420x600")

tk.Label(window, text="Venus Space", font=("Arial", 18)).pack(pady=10)

tk.Label(window, text="Room:").pack()
room_var = tk.StringVar(window)
room_var.set(room_types[0])
tk.OptionMenu(window, room_var, *room_types).pack()

tk.Label(window, text="Style:").pack()
style_var = tk.StringVar(window)
style_var.set(styles[0])
style_menu = tk.OptionMenu(
    window, style_var, *styles, command=update_style_choices
)
style_menu.pack()

style_info_label = tk.Label(window, text="")
style_info_label.pack(pady=4)

tk.Label(window, text="Main Color:").pack()
color_var = tk.StringVar(window)
color_menu = tk.OptionMenu(window, color_var, "")
color_menu.pack()

tk.Label(window, text="Favorite Material:").pack()
material_var = tk.StringVar(window)
material_menu = tk.OptionMenu(window, material_var, "")
material_menu.pack()

tk.Label(window, text="Width (m):").pack()
width_entry = tk.Entry(window)
width_entry.pack()

tk.Label(window, text="Length (m):").pack()
length_entry = tk.Entry(window)
length_entry.pack()

tk.Label(window, text="Budget (¥):").pack()
budget_entry = tk.Entry(window)
budget_entry.pack()

tk.Label(window, text="Budget scope:").pack()
scope_var = tk.StringVar(window)
scope_var.set(budget_scopes[0])
tk.OptionMenu(window, scope_var, *budget_scopes).pack()

tk.Button(window, text="Estimate Cost", command=estimate_cost).pack(pady=12)

result_label = tk.Label(window, text="", justify="left", anchor="w")
result_label.pack(pady=8)

update_style_choices()

window.mainloop()
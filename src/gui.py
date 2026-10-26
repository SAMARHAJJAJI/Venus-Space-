
import os
import tkinter as tk
import customtkinter as ctk
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
from reports import save_project_summary


# ---------------- THEME ----------------

BG      = "#F5F0E8"
CARD    = "#FFFFFF"
ACCENT  = "#A07850"
HOVER   = "#8B6543"
TEXT    = "#4A3F35"
MUTED   = "#9C8E7E"
LINE    = "#E3D9C8"
ENTRY   = "#FBF8F3"
ERROR   = "#B0524A"


# ---------------- LOGIC ----------------
last_result = None
def update_style_choices(choice=None):
    details = style_details[style_menu.get()]

    color_menu.configure(values=details["colors"])
    color_menu.set(details["colors"][0])

    material_menu.configure(values=details["materials"])
    material_menu.set(details["materials"][0])

    style_info.configure(
        text=f"{details['mood']}  ·  {details['lighting']}"
    )


def estimate_cost():
    room = room_menu.get()
    style = style_menu.get()
    scope = scope_menu.get()

    try:
        width = float(width_entry.get())
        length = float(length_entry.get())
        budget = float(budget_entry.get())
    except ValueError:
        result_label.configure(
            text="Please enter valid numbers for width, length and budget.",
            text_color=ERROR
        )
        return

    if width <= 0 or length <= 0 or budget <= 0:
        result_label.configure(
            text="Numbers must be greater than 0.",
            text_color=ERROR
        )
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
        material_total = area * material_prices_per_m2[material_menu.get()]

    total = (
        furniture_total
        + decoration_total
        + lighting_total
        + material_total
    )

    global last_result

    if area < 10:
        room_size = "Compact"
    elif area < 20:
        room_size = "Medium"
    else:
        room_size = "Spacious"

    last_result = {
        "room_name": room,
        "room_style": style,
        "main_color": color_menu.get(),
        "favorite_material": material_menu.get(),
        "room_area": area,
        "room_size": room_size,
        "room_budget": budget,
        "total_estimated_cost": total,
        "budget_status": "",
        "furniture_total": furniture_total,
        "total": total,
        "budget": budget,
    }

    if total <= budget:
        status = f"Within budget (difference: ¥{budget - total:.2f})"
        last_result["budget_status"] = "Within budget"
        options_frame.pack_forget()
    else:
        status = f"Over budget (difference: ¥{total - budget:.2f})"
        last_result["budget_status"] = "Over budget"
        options_frame.pack(pady=8)

    result_label.configure(
        text=(
            f"Room Area: {area:.1f} m²\n"
            f"Furniture: ¥{furniture_total:.2f}\n"
            f"Decoration: ¥{decoration_total:.2f}\n"
            f"Lighting: ¥{lighting_total:.2f}\n"
            f"Materials: ¥{material_total:.2f}\n"
            f"Total: ¥{total:.2f}\n"
            f"Budget: ¥{budget:.2f}\n"
            f"Status: {status}"
        ),
        text_color=TEXT
    )

def show_alternatives():
    if last_result is None:
        return

    room = last_result["room_name"]
    design = design_recommendations[(room, last_result["room_style"])]

    cheapest_name = min(furniture_prices[room], key=furniture_prices[room].get)
    cheapest_price = furniture_prices[room][cheapest_name]

    lines = ["Budget-Friendly Suggestions:"]

    new_furniture_total = 0
    for item in design["furniture"]:
        old_price = furniture_prices[room][item]
        new_furniture_total += cheapest_price
        lines.append(
            f"- Swap '{item}' (¥{old_price}) "
            f"for '{cheapest_name}' (¥{cheapest_price})"
        )

    savings = last_result["furniture_total"] - new_furniture_total
    lines.append(f"You save: ¥{savings:.2f}")

    result_label.configure(text="\n".join(lines), text_color=TEXT)


def apply_discount():
    if last_result is None:
        return

    try:
        percent = float(discount_entry.get())
    except ValueError:
        result_label.configure(
            text="Enter a valid discount number.", text_color=ERROR
        )
        return

    if percent <= 0 or percent > 100:
        result_label.configure(
            text="Discount must be between 1 and 100.", text_color=ERROR
        )
        return

    total = last_result["total"]
    budget = last_result["budget"]

    amount = total * percent / 100
    new_total = total - amount

    if new_total <= budget:
        end_text = "now fits your budget."
    else:
        end_text = f"still over budget by ¥{new_total - budget:.2f}"

    result_label.configure(
        text=(
            f"Discount: {percent:.0f}% = ¥{amount:.2f}\n"
            f"New total: ¥{new_total:.2f}\n"
            f"With this discount, the design {end_text}"
        ),
        text_color=TEXT
    )


def save_summary():
    if last_result is None:
        save_label.configure(
            text="Estimate a design first.", text_color=ERROR
        )
        return

    save_project_summary(
        "../design_summary.txt",
        [last_result],
        last_result["total"],
        last_result["budget"]
    )

    save_label.configure(
        text="Summary saved to design_summary.txt",
        text_color=ACCENT
    )
# ---------------- WINDOW ----------------

ctk.set_appearance_mode("light")

app = ctk.CTk()
app.geometry("440x700")
app.title("Venus Space")

ASSETS = os.path.join(os.path.dirname(__file__), "..", "assets")
app.iconbitmap(os.path.join(ASSETS, "logo.ico"))

logo_image = tk.PhotoImage(file=os.path.join(ASSETS, "logo.png"))
logo_image = logo_image.subsample(2, 2)

main = ctk.CTkScrollableFrame(app, fg_color=BG, corner_radius=0)
main.pack(fill="both", expand=True)

logo_label = tk.Label(main, image=logo_image, bg=BG)
logo_label.pack(pady=(16, 0))

ctk.CTkLabel(
    main, text="Venus Space",
    font=("Georgia", 26, "bold"), text_color=TEXT
).pack(pady=(6, 0))

ctk.CTkLabel(
    main, text="Design a space that feels like you",
    font=("Georgia", 13, "italic"), text_color=MUTED
).pack()

ctk.CTkFrame(main, fg_color=LINE, height=1, width=340).pack(pady=8)


def section_label(text):
    ctk.CTkLabel(
        main, text=text,
        font=("Segoe UI", 11, "bold"), text_color=MUTED
    ).pack(pady=(6, 2))


section_label("ROOM")
room_menu = ctk.CTkOptionMenu(
    main, values=room_types,
    fg_color=CARD, button_color=ACCENT, button_hover_color=HOVER,
    text_color=TEXT, dropdown_fg_color=CARD,
    dropdown_text_color=TEXT, dropdown_hover_color=ACCENT,
    corner_radius=10, font=("Segoe UI", 12)
)
room_menu.pack(pady=(0, 8))

section_label("STYLE")
style_menu = ctk.CTkOptionMenu(
    main, values=styles, command=update_style_choices,
    fg_color=CARD, button_color=ACCENT, button_hover_color=HOVER,
    text_color=TEXT, dropdown_fg_color=CARD,
    dropdown_text_color=TEXT, dropdown_hover_color=ACCENT,
    corner_radius=10, font=("Segoe UI", 12)
)
style_menu.pack(pady=(0, 2))

style_info = ctk.CTkLabel(
    main, text="", font=("Segoe UI", 12), text_color=ACCENT
)
style_info.pack(pady=(0, 8))

section_label("MAIN COLOR")
color_menu = ctk.CTkOptionMenu(
    main, values=["-"],
    fg_color=CARD, button_color=ACCENT, button_hover_color=HOVER,
    text_color=TEXT, dropdown_fg_color=CARD,
    dropdown_text_color=TEXT, dropdown_hover_color=ACCENT,
    corner_radius=10, font=("Segoe UI", 12)
)
color_menu.pack(pady=(0, 8))

section_label("FAVORITE MATERIAL")
material_menu = ctk.CTkOptionMenu(
    main, values=["-"],
    fg_color=CARD, button_color=ACCENT, button_hover_color=HOVER,
    text_color=TEXT, dropdown_fg_color=CARD,
    dropdown_text_color=TEXT, dropdown_hover_color=ACCENT,
    corner_radius=10, font=("Segoe UI", 12)
)
material_menu.pack(pady=(0, 8))

section_label("WIDTH (m)")
width_entry = ctk.CTkEntry(
    main, justify="center", width=180,
    fg_color=ENTRY, text_color=TEXT, border_color=LINE
)
width_entry.pack(pady=(0, 8))

section_label("LENGTH (m)")
length_entry = ctk.CTkEntry(
    main, justify="center", width=180,
    fg_color=ENTRY, text_color=TEXT, border_color=LINE
)
length_entry.pack(pady=(0, 8))

section_label("BUDGET (¥)")
budget_entry = ctk.CTkEntry(
    main, justify="center", width=180,
    fg_color=ENTRY, text_color=TEXT, border_color=LINE
)
budget_entry.pack(pady=(0, 8))

section_label("BUDGET SCOPE")
scope_menu = ctk.CTkOptionMenu(
    main, values=budget_scopes,
    fg_color=CARD, button_color=ACCENT, button_hover_color=HOVER,
    text_color=TEXT, dropdown_fg_color=CARD,
    dropdown_text_color=TEXT, dropdown_hover_color=ACCENT,
    corner_radius=10, font=("Segoe UI", 12)
)
scope_menu.pack(pady=(0, 16))

estimate_button = ctk.CTkButton(
    main, text="Estimate Cost", command=estimate_cost,
    fg_color=ACCENT, hover_color=HOVER, text_color="white",
    font=("Segoe UI", 13, "bold"),
    corner_radius=14, width=200, height=42
)
estimate_button.pack()

result_label = ctk.CTkLabel(
    main, text="", justify="left",
    font=("Segoe UI", 12), text_color=TEXT
)
result_label.pack(pady=8, padx=40, fill="x")
options_frame = ctk.CTkFrame(main, fg_color=BG)

ctk.CTkButton(
    options_frame, text="Find Cheaper Alternatives",
    command=show_alternatives,
    fg_color=CARD, hover_color=ENTRY, text_color=TEXT,
    border_color=ACCENT, border_width=1,
    corner_radius=12, font=("Segoe UI", 11)
).pack(pady=4)

discount_entry = ctk.CTkEntry(
    options_frame, justify="center", width=120,
    fg_color=ENTRY, text_color=TEXT, border_color=LINE,
    placeholder_text="Discount %"
)
discount_entry.pack(pady=4)

ctk.CTkButton(
    options_frame, text="Apply Discount",
    command=apply_discount,
    fg_color=ACCENT, hover_color=HOVER, text_color="white",
    corner_radius=12, font=("Segoe UI", 11)
).pack(pady=4)

ctk.CTkButton(
    main, text="Save Summary to File",
    command=save_summary,
    fg_color=CARD, hover_color=ENTRY, text_color=TEXT,
    border_color=ACCENT, border_width=1,
    corner_radius=12, font=("Segoe UI", 11)
).pack(pady=6)

save_label = ctk.CTkLabel(
    main, text="", font=("Segoe UI", 11), text_color=MUTED
)
save_label.pack()

update_style_choices()

app.mainloop()
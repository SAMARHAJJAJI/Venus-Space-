
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

    if total <= budget:
        status = f"Within budget (difference: ¥{budget - total:.2f})"
    else:
        status = f"Over budget (difference: ¥{total - budget:.2f})"

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


# ---------------- WINDOW ----------------

ctk.set_appearance_mode("light")

app = ctk.CTk()
app.geometry("440x760")
app.title("Venus Space")

ASSETS = os.path.join(os.path.dirname(__file__), "..", "assets")
app.iconbitmap(os.path.join(ASSETS, "logo.ico"))

logo_image = tk.PhotoImage(file=os.path.join(ASSETS, "logo.png"))

main = ctk.CTkFrame(app, fg_color=BG, corner_radius=0)
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

ctk.CTkFrame(main, fg_color=LINE, height=1, width=340).pack(pady=16)


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
result_label.pack(pady=16, padx=40, fill="x")

update_style_choices()

app.mainloop()
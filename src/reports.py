def save_design_summary(
    filename,
    room_name,
    room_style,
    main_color,
    favorite_material,
    room_area,
    room_size,
    furniture_total,
    decoration_total,
    lighting_total,
    material_total,
    total_estimated_cost,
    room_budget,
    budget_status
):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Venus Space - Design Summary\n")
        file.write("----------------------------\n")
        file.write(f"Room: {room_name}\n")
        file.write(f"Style: {room_style}\n")
        file.write(f"Main Color: {main_color}\n")
        file.write(f"Favorite Material: {favorite_material}\n")
        file.write(f"Room Area: {room_area:.1f} m2\n")
        file.write(f"Room Size: {room_size}\n")
        file.write("\n")
        file.write(f"Furniture: ¥{furniture_total:.2f}\n")
        file.write(f"Decoration: ¥{decoration_total:.2f}\n")
        file.write(f"Lighting: ¥{lighting_total:.2f}\n")
        file.write(f"Materials: ¥{material_total:.2f}\n")
        file.write(f"Total Estimated Cost: ¥{total_estimated_cost:.2f}\n")
        file.write(f"Budget: ¥{room_budget:.2f}\n")
        file.write(f"Budget Status: {budget_status}\n")
def save_project_summary(filename, project_rooms, project_total, project_budget):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Venus Space - Project Summary\n")
        file.write("=============================\n")

        for room in project_rooms:
            file.write(f"Room: {room['room_name']}\n")
            file.write(f"  Style: {room['room_style']}\n")
            file.write(f"  Main Color: {room['main_color']}\n")
            file.write(f"  Favorite Material: {room['favorite_material']}\n")
            file.write(f"  Room Area: {room['room_area']:.1f} m2\n")
            file.write(f"  Room Size: {room['room_size']}\n")
            file.write(f"  Estimated Cost: ¥{room['total_estimated_cost']:.2f}\n")
            file.write(f"  Budget: ¥{room['room_budget']:.2f}\n")
            file.write(f"  Budget Status: {room['budget_status']}\n")
            file.write("\n")

        file.write("-----------------------------\n")
        file.write(f"Total Project Cost: ¥{project_total:.2f}\n")
        file.write(f"Total Budget: ¥{project_budget:.2f}\n")

        difference = abs(project_budget - project_total)

        if project_total <= project_budget:
            file.write(f"Project is within budget (difference: ¥{difference:.2f})\n")
        else:
            file.write(f"Project is over budget (difference: ¥{difference:.2f})\n")
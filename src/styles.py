#MODULE: styles.py
#styles = [
 #   "Minimal",
  #  "Cozy",
   # "Modern",
    #"Scandinavian"
#]


style_details = {
    "Cozy": {
        "mood": "Warm and comfortable",
        "lighting": "Warm",
        "colors": ["Beige", "Cream", "Warm Brown"],
        "materials": ["Wood", "Fabric"]
    },

    "Minimal": {
        "mood": "Clean and calm",
        "lighting": "Natural",
        "colors": ["White", "Beige", "Light Gray"],
        "materials": ["Wood", "Glass"]
    },

    "Modern": {
        "mood": "Clean and sophisticated",
        "lighting": "Bright and balanced",
        "colors": ["White", "Black", "Gray"],
        "materials": ["Glass", "Metal", "Wood"]
    },

    "Scandinavian": {
        "mood": "Light, natural and comfortable",
        "lighting": "Natural and soft",
        "colors": ["White", "Beige", "Light Blue"],
        "materials": ["Light Wood", "Fabric"]
    }
}
print(style_details.keys())
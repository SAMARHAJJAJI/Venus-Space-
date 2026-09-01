#room types
#furniture categories
#lighting choices
#flooring choices
room_types = [
    "Bedroom",
    "Living Room",
    "Home Office",
    "Dining Room"
]
room_details = {
    "Bedroom": {
        "purpose": "Rest and relaxation",
        "focus": "Comfort, calm colors, and soft lighting"
    },

    "Living Room": {
        "purpose": "Relaxing and spending time with others",
        "focus": "Comfortable seating and an open layout"
    },

    "Home Office": {
        "purpose": "Work and study",
        "focus": "Good lighting, organization, and productivity"
    },

    "Dining Room": {
        "purpose": "Eating and gathering",
        "focus": "Comfortable seating and a welcoming atmosphere"
    }
}
design_recommendations = {
    ("Bedroom", "Cozy"): {
        "tip": "Use warm lighting, soft fabrics, and comfortable furniture to create a relaxing bedroom.",
        "furniture": ["Bed", "Nightstand", "Wardrobe"],
        "lighting": "Warm and soft",
        "atmosphere": "Relaxing and comfortable"
    },

    ("Bedroom", "Minimal"): {
        "tip": "Keep the bedroom simple with clean furniture, neutral colors, and natural lighting.",
        "furniture": ["Bed", "Nightstand", "Simple Wardrobe"],
        "lighting": "Natural and soft",
        "atmosphere": "Clean and calm"
    },

    ("Living Room", "Cozy"): {
        "tip": "Create a welcoming living room with comfortable seating, warm lighting, and soft materials.",
        "furniture": ["Sofa", "Coffee Table", "TV Cabinet"],
        "lighting": "Warm",
        "atmosphere": "Warm and welcoming"
    },

    ("Living Room", "Minimal"): {
        "tip": "Use simple furniture and an open layout to keep the living room clean and spacious.",
        "furniture": ["Sofa", "Coffee Table", "TV Cabinet"],
        "lighting": "Natural",
        "atmosphere": "Simple and spacious"
    },

    ("Home Office", "Cozy"): {
        "tip": "Use warm materials and comfortable furniture to make the workspace feel inviting.",
        "furniture": ["Desk", "Office Chair", "Bookshelf"],
        "lighting": "Warm and comfortable",
        "atmosphere": "Comfortable and creative"
    },

    ("Home Office", "Minimal"): {
        "tip": "Keep the workspace clean and organized with simple furniture and good natural lighting.",
        "furniture": ["Desk", "Office Chair", "Storage Cabinet"],
        "lighting": "Natural and bright",
        "atmosphere": "Focused and organized"
    },

    ("Dining Room", "Cozy"): {
        "tip": "Create a warm dining atmosphere with wooden furniture, soft lighting, and comfortable seating.",
        "furniture": ["Dining Table", "Dining Chairs", "Sideboard"],
        "lighting": "Warm",
        "atmosphere": "Warm and social"
    },

    ("Dining Room", "Minimal"): {
        "tip": "Choose a simple dining table and keep the space uncluttered and bright.",
        "furniture": ["Dining Table", "Dining Chairs", "Sideboard"],
        "lighting": "Natural and bright",
        "atmosphere": "Clean and elegant"
    }
}
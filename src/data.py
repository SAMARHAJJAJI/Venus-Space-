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
    },
    ("Bedroom", "Modern"): {
        "tip": "Combine a clean bed frame with bold accents and practical storage for a polished bedroom.",
        "furniture": ["Platform Bed", "Bedside Table", "Built-in Wardrobe"],
        "lighting": "Layered and adjustable",
        "atmosphere": "Stylish and confident"
    },

    ("Bedroom", "Scandinavian"): {
        "tip": "Use light wood, soft textiles, and pale colors to create a peaceful and airy bedroom.",
        "furniture": ["Light Wood Bed", "Bedside Table", "Open Clothing Rack"],
        "lighting": "Bright natural light with warm lamps",
        "atmosphere": "Peaceful and airy"
    },

    ("Living Room", "Modern"): {
        "tip": "Use strong shapes, a statement sofa, and selected accents for a contemporary living room.",
        "furniture": ["Sectional Sofa", "Glass Coffee Table", "Media Console"],
        "lighting": "Layered accent lighting",
        "atmosphere": "Elegant and energetic"
    },

    ("Living Room", "Scandinavian"): {
        "tip": "Mix light timber, comfortable seating, and simple decoration for a bright social space.",
        "furniture": ["Fabric Sofa", "Wooden Coffee Table", "Open Shelving"],
        "lighting": "Bright and warm",
        "atmosphere": "Light and inviting"
    },

    ("Home Office", "Modern"): {
        "tip": "Use a streamlined desk, ergonomic chair, and focused task lighting for productive work.",
        "furniture": ["Standing Desk", "Ergonomic Chair", "Drawer Unit"],
        "lighting": "Bright task lighting",
        "atmosphere": "Focused and professional"
    },

    ("Home Office", "Scandinavian"): {
        "tip": "Use light wood, plants, and soft textures to create a calm but productive workspace.",
        "furniture": ["Wooden Desk", "Comfortable Chair", "Storage Shelves"],
        "lighting": "Natural and gentle",
        "atmosphere": "Calm and productive"
    },

    ("Dining Room", "Modern"): {
        "tip": "Make the dining table the focal point and use statement lighting for a refined space.",
        "furniture": ["Extendable Dining Table", "Upholstered Chairs", "Modern Sideboard"],
        "lighting": "Statement pendant lighting",
        "atmosphere": "Refined and social"
    },

    ("Dining Room", "Scandinavian"): {
        "tip": "Use natural wood, simple chairs, and soft colors for relaxed and welcoming meals.",
        "furniture": ["Light Wood Dining Table", "Wooden Chairs", "Low Sideboard"],
        "lighting": "Warm pendant lighting",
        "atmosphere": "Natural and welcoming"
    },
}
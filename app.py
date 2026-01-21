from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Indian recipes database for bachelors
recipes = {
    "maggi": {
        "name": "Quick Maggi",
        "time": "5 minutes",
        "difficulty": "Easy",
        "ingredients": ["Maggi noodles", "Water", "Masala packet", "Vegetables (optional)"],
        "steps": [
            "Boil 1.5 cups of water",
            "Add Maggi noodles and vegetables",
            "Add masala packet",
            "Cook for 2-3 minutes",
            "Serve hot"
        ]
    },
    "dal-rice": {
        "name": "Simple Dal Rice",
        "time": "30 minutes",
        "difficulty": "Easy",
        "ingredients": ["Rice - 1 cup", "Toor dal - 1/2 cup", "Turmeric", "Salt", "Ghee"],
        "steps": [
            "Wash rice and dal separately",
            "Pressure cook dal with turmeric and salt for 3 whistles",
            "Cook rice separately",
            "Mash dal and add ghee",
            "Serve dal over rice"
        ]
    },
    "egg-bhurji": {
        "name": "Egg Bhurji",
        "time": "15 minutes",
        "difficulty": "Easy",
        "ingredients": ["Eggs - 3", "Onion - 1", "Tomato - 1", "Green chili - 1", "Oil", "Spices"],
        "steps": [
            "Heat oil in pan",
            "Add chopped onions and green chili",
            "Add tomatoes and cook",
            "Beat eggs and pour into pan",
            "Scramble and add spices",
            "Serve with bread or roti"
        ]
    },
    "aloo-paratha": {
        "name": "Aloo Paratha",
        "time": "30 minutes",
        "difficulty": "Medium",
        "ingredients": ["Wheat flour - 2 cups", "Boiled potatoes - 3", "Spices", "Oil/Ghee"],
        "steps": [
            "Make dough with wheat flour",
            "Mash potatoes with spices",
            "Roll dough, add potato filling",
            "Seal and roll again",
            "Cook on tawa with ghee",
            "Serve with curd or pickle"
        ]
    },
    "paneer-bhurji": {
        "name": "Paneer Bhurji",
        "time": "20 minutes",
        "difficulty": "Easy",
        "ingredients": ["Paneer - 200g", "Onion", "Tomato", "Capsicum", "Spices"],
        "steps": [
            "Crumble paneer",
            "Sauté onions in oil",
            "Add tomatoes and spices",
            "Add crumbled paneer",
            "Cook for 5 minutes",
            "Serve with roti or bread"
        ]
    },
    "chole": {
        "name": "Chole (Chickpea Curry)",
        "time": "40 minutes",
        "difficulty": "Medium",
        "ingredients": ["Chickpeas - 1 cup", "Onion", "Tomato", "Chole masala", "Tea bag"],
        "steps": [
            "Soak chickpeas overnight, pressure cook",
            "Sauté onions and tomatoes",
            "Add chole masala and spices",
            "Add boiled chickpeas",
            "Simmer for 10 minutes",
            "Serve with bhatura or rice"
        ]
    },
    "rajma": {
        "name": "Rajma (Kidney Beans)",
        "time": "45 minutes",
        "difficulty": "Medium",
        "ingredients": ["Kidney beans - 1 cup", "Onion", "Tomato", "Ginger-garlic paste", "Spices"],
        "steps": [
            "Soak rajma overnight, pressure cook",
            "Sauté onions and ginger-garlic paste",
            "Add tomatoes and spices",
            "Add boiled rajma",
            "Simmer for 15 minutes",
            "Serve with rice"
        ]
    },
    "poha": {
        "name": "Poha",
        "time": "15 minutes",
        "difficulty": "Easy",
        "ingredients": ["Poha - 2 cups", "Onion", "Peanuts", "Curry leaves", "Mustard seeds"],
        "steps": [
            "Wash and drain poha",
            "Heat oil, add mustard seeds",
            "Add peanuts and curry leaves",
            "Add onions and sauté",
            "Add poha and mix gently",
            "Serve with lemon juice"
        ]
    },
    "upma": {
        "name": "Rava Upma",
        "time": "20 minutes",
        "difficulty": "Easy",
        "ingredients": ["Semolina - 1 cup", "Onion", "Vegetables", "Mustard seeds", "Curry leaves"],
        "steps": [
            "Roast semolina until fragrant",
            "Heat oil, add mustard seeds",
            "Add onions and vegetables",
            "Add water and bring to boil",
            "Add roasted semolina slowly",
            "Cook until water absorbed"
        ]
    },
    "khichdi": {
        "name": "Moong Dal Khichdi",
        "time": "25 minutes",
        "difficulty": "Easy",
        "ingredients": ["Rice - 1 cup", "Moong dal - 1/2 cup", "Turmeric", "Ghee", "Cumin"],
        "steps": [
            "Wash rice and dal together",
            "Heat ghee, add cumin seeds",
            "Add rice-dal mixture",
            "Add water and pressure cook",
            "Serve with curd or pickle"
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/api/recipes')
def get_recipes():
    return jsonify(recipes)

@app.route('/api/random')
def random_recipe():
    recipe_key = random.choice(list(recipes.keys()))
    return jsonify({recipe_key: recipes[recipe_key]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

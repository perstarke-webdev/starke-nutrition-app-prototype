from flask import Flask, session
from dotenv import load_dotenv
import datetime
import requests
import os

app = Flask(__name__)

parent_dir = os.path.dirname(os.getcwd())

app.secret_key = os.urandom(12)

load_dotenv(parent_dir + "/Envs/key.env")

rapid_api_key = os.getenv("RAPID_API_KEY")

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': rapid_api_key,
}


@app.route("/get_recipes_with_nutrients")
def get_recipes_with_nutrients():

    session["kcal"] = 500
    session["proteins"] = 50
    session["carbs"] = 50
    session["fats"] = 10
    session["allowed_range"] = 0.2

    min_kcal = float(session["kcal"]) - float(session["kcal"]) * float(session["allowed_range"])
    max_kcal = float(session["kcal"]) + float(session["kcal"]) * float(session["allowed_range"])

    min_protein = float(session["proteins"]) - float(session["proteins"]) * float(session["allowed_range"])
    max_protein = float(session["proteins"]) + float(session["proteins"]) * float(session["allowed_range"])

    min_carbs = float(session["carbs"]) - float(session["carbs"]) * float(session["allowed_range"])
    max_carbs = float(session["carbs"]) + float(session["carbs"]) * float(session["allowed_range"])

    min_fats = float(session["fats"]) - float(session["fats"]) * float(session["allowed_range"])
    max_fats = float(session["fats"]) + float(session["fats"]) * float(session["allowed_range"])

    querystring = {"random": "true",
                   "minCalories": min_kcal, "maxCalories": max_kcal,
                   "minProtein": min_protein, "maxProtein": max_protein,
                   "minCarbs": min_carbs, "maxCarbs": max_carbs,
                   "minFat": min_fats, "maxFat": max_fats}

    recipes = requests.request("GET", url + "recipes/findByNutrients", headers=headers, params=querystring).json()

    return recipes

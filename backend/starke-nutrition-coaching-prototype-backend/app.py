from flask import Flask, session
from dotenv import load_dotenv
import requests
import datetime
import os

app = Flask(__name__)

parent_dir = os.path.dirname(os.getcwd())

app.secret_key = os.urandom(12)
app.permanent_session_lifetime = datetime.timedelta(days=7)

load_dotenv(parent_dir + "/Envs/key.env")

rapid_api_key = os.getenv("RAPID_API_KEY")

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': rapid_api_key,
}


def write_recipes_in_list(kcal, proteins, carbs, fats):
    """
    :param kcal: the required calories, as int
    :param proteins: the required grams of proteins, as int
    :param carbs: the required grams of carbs, as int
    :param fats: the required grams of fats, as int
    Creates a list of recipes matching the give nutrients within a 10% range
    """

    session["recipe_counter"] = 0

    allowed_range = 0.1

    min_kcal = float(kcal) - float(kcal) * float(allowed_range)
    max_kcal = float(kcal) + float(kcal) * float(allowed_range)

    min_protein = float(proteins) - float(proteins) * float(allowed_range)
    max_protein = float(proteins) + float(proteins) * float(allowed_range)

    min_carbs = float(carbs) - float(carbs) * float(allowed_range)
    max_carbs = float(carbs) + float(carbs) * float(allowed_range)

    min_fats = float(fats) - float(fats) * float(allowed_range)
    max_fats = float(fats) + float(fats) * float(allowed_range)

    querystring = {"random": "true",
                   "minCalories": min_kcal, "maxCalories": max_kcal,
                   "minProtein": min_protein, "maxProtein": max_protein,
                   "minCarbs": min_carbs, "maxCarbs": max_carbs,
                   "minFat": min_fats, "maxFat": max_fats}

    return requests.request("GET", url + "recipes/findByNutrients", headers=headers, params=querystring).json()


@app.route("/get_recipe")
def get_recipe():
    """
    Get a recipe with specified nutrients
    """

    if "recipes_counter" in session.keys():
        session["recipes_counter"] += 1

        if session["recipes_counter"] == 9:
            session["recipes_counter"] = 0
            session["recipes"] = write_recipes_in_list(500, 50, 50, 10)

        return session["recipes"][session["recipes_counter"]]

    else:
        session["recipes"] = write_recipes_in_list(500, 50, 50, 10)
        session["recipes_counter"] = 0
        return session["recipes"][0]



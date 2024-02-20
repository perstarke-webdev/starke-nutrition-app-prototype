from flask import Flask, session, request
from dotenv import load_dotenv
import requests
import datetime
import os

from werkzeug.exceptions import BadRequestKeyError

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

    session["recipe_counters"] = 0

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

    response = requests.request("GET", url + "recipes/findByNutrients", headers=headers, params=querystring)

    if response.status_code != 200:
        print("Request failed with status code:", response.status_code)
        print(response.text)
        return "Error"
    else:
        try:
            json_response = response.json()
            print(json_response)
        except ValueError as e:
            print("Failed to parse JSON response:", e)
            return "Error"

    return json_response


@app.route("/get_recipe")
def get_recipe():
    """
    Get a random recipe with specified nutrients.
    Call with parameters to create new recipe list,
    call without to get a new recipe with same nutrients as from the call before
    """

    # Get nutrients from URL
    try:
        session["kcal"] = request.args["kcal"]
    except BadRequestKeyError:
        if "kcal" in session.keys():
            pass
        else:
            session["kcal"] = 0
    try:
        session["proteins"] = request.args["proteins"]
    except BadRequestKeyError:
        if "proteins" in session.keys():
            pass
        else:
            session["proteins"] = 0
    try:
        session["carbs"] = request.args["carbs"]
    except BadRequestKeyError:
        if "carbs" in session.keys():
            pass
        else:
            session["carbs"] = 0
    try:
        session["fats"] = request.args["fats"]
    except BadRequestKeyError:
        if "fats" in session.keys():
            pass
        else:
            session["fats"] = 0

    # Route has been called before
    if "recipes_counter" in session.keys():

        # Nutrients given, create new recipe list
        if session["kcal"] and session["proteins"] and session["carbs"] and session["fats"]:
            session["recipes"] = write_recipes_in_list(session["kcal"], session["proteins"], session["carbs"], session["fats"])
            session["recipes_counter"] = 0
            return session["recipes"][0]

        session["recipes_counter"] += 1

        # List of recipes has been fully iterated
        if session["recipes_counter"] == 9:
            session["recipes_counter"] = 0
            session["recipes"] = write_recipes_in_list(session["kcal"], session["proteins"], session["carbs"], session["fats"])

        return session["recipes"][session["recipes_counter"]]

    # First ever call
    else:
        session["recipes"] = write_recipes_in_list(session["kcal"], session["proteins"], session["carbs"], session["fats"])
        session["recipes_counter"] = 0
        return session["recipes"][0]


if __name__ == "__main__":
    app.run(port=8000, debug=True)
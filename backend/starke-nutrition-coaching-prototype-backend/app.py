from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from flask import Flask, session, request, make_response
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import datetime
import os

from werkzeug.exceptions import BadRequestKeyError


# Create App
app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(12)
app.permanent_session_lifetime = datetime.timedelta(days=7)


# Setup environmental variables and Spoonacular headers and URL
parent_dir = os.path.dirname(os.getcwd())
load_dotenv(parent_dir + "/Envs/key.env")
rapid_api_key = os.getenv("RAPID_API_KEY")
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"
headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': rapid_api_key,
}

# Create the database engine
engine = create_engine("mysql+pymysql://root:24Zorg42@localhost/recipes")

# Define the metadata
meta = MetaData()

# Define the recipes table
recipes = Table(
    'recipes',
    meta,
    Column('recipe_id', Integer, primary_key=True),
    Column('recipe_title', String(255)),
    Column('recipe_kcal', Float),
    Column('recipe_proteins', String(255)),
    Column('recipe_carbs', String(255)),
    Column('recipe_fats', String(255)),
    Column('image_path', String(255))
)


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

    try:
        min_kcal = float(kcal) - float(kcal) * float(allowed_range)
        max_kcal = float(kcal) + float(kcal) * float(allowed_range)

        min_protein = float(proteins) - float(proteins) * float(allowed_range)
        max_protein = float(proteins) + float(proteins) * float(allowed_range)

        min_carbs = float(carbs) - float(carbs) * float(allowed_range)
        max_carbs = float(carbs) + float(carbs) * float(allowed_range)

        min_fats = float(fats) - float(fats) * float(allowed_range)
        max_fats = float(fats) + float(fats) * float(allowed_range)
    except ValueError:
        return make_response("ValueError", 500)

    querystring = {"random": "true",
                   "minCalories": min_kcal, "maxCalories": max_kcal,
                   "minProtein": min_protein, "maxProtein": max_protein,
                   "minCarbs": min_carbs, "maxCarbs": max_carbs,
                   "minFat": min_fats, "maxFat": max_fats}

    response = requests.request("GET", url + "recipes/findByNutrients", headers=headers, params=querystring)

    if response.status_code != 200:
        print("Request failed with status code:", response.status_code)
        print(response.text)
        return "Error Status Code != 200", response.status_code
    else:
        try:
            json_response = response.json()
            print(json_response)
        except ValueError as e:
            print("Failed to parse JSON response:", e)
            return "Error parsing JSON", response.status_code

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


@app.route("/write_recipe")
def write_recipe_to_db():
    """
    Writes the recipe that is written into the session by get_recipe into the database.
    Only to be called after calling get_recipe
    """

    recipe = session["recipes"][0]

    recipe_id = recipe["id"]
    recipe_title = recipe["title"]
    recipe_kcal = recipe["calories"]
    recipe_proteins = recipe["protein"]
    recipe_carbs = recipe["carbs"]
    recipe_fats = recipe["fat"]
    recipe_image_path = recipe["image"]

    # Connect to the database
    with engine.connect() as conn:
        # Insert a new row into the table
        result = conn.execute(
            recipes.insert().values(recipe_id=recipe_id, recipe_title=recipe_title, recipe_kcal=recipe_kcal,
                                    recipe_proteins=recipe_proteins, recipe_carbs=recipe_carbs, recipe_fats=recipe_fats,
                                    image_path=recipe_image_path))

        conn.commit()

        # Check if the insertion was successful
        if result.rowcount == 1:
            message = "INSERTION SUCCESSFUL"
        else:
            message = "FAILED TO INSERT"

        return message


if __name__ == "__main__":
    app.run(port=8000, debug=True)
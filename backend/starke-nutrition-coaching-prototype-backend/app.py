from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from flask import Flask, session, request, make_response, jsonify
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

# rapid_api_key = os.environ.get('RAPID_API_KEY')

# Before, for local testing, it was:
load_dotenv(parent_dir + "/Envs/key.env")
rapid_api_key = os.getenv("RAPID_API_KEY")

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"
headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': rapid_api_key,
}

# Create the database engine
connection_string = "mysql+pymysql://root:12345@34.122.247.82/recipes"
engine = create_engine(connection_string)

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
    Column('image_path', String(255)),
    Column('wanted_kcal', Float),
    Column('wanted_proteins', String(255)),
    Column('wanted_carbs', String(255)),
    Column('wanted_fats', String(255))
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
        kcal = request.args["kcal"]
    except BadRequestKeyError:
        kcal = 0

    try:
        proteins = request.args["proteins"]
    except BadRequestKeyError:
        proteins = 0

    try:
        carbs = request.args["carbs"]
    except BadRequestKeyError:
        carbs = 0

    try:
        fats = request.args["fats"]
    except BadRequestKeyError:
        fats = 0

    recipe_list = write_recipes_in_list(kcal, proteins, carbs, fats)

    return recipe_list[0]


@app.route("/write_recipe", methods=['POST'])
def write_recipe():
    """
    Writes a recipe into the database
    """

    # Extract the recipe data from the request body
    data = request.json
    recipe_id = data.get('id', None)
    recipe_title = data.get('title', None)
    recipe_kcal = data.get('kcal', None)
    recipe_proteins = data.get('proteins', None)
    recipe_carbs = data.get('carbs', None)
    recipe_fats = data.get('fats', None)
    recipe_image_path = data.get('image_path', None)
    wanted_kcal = data.get('wanted_kcal', None)
    wanted_proteins = data.get('wanted_proteins', None)
    wanted_carbs = data.get('wanted_carbs', None)
    wanted_fats = data.get('wanted_fats', None)

    # Connect to the database
    with engine.connect() as conn:
        # Insert a new row into the table
        result = conn.execute(
            recipes.insert().values(
                recipe_id=recipe_id, recipe_title=recipe_title, recipe_kcal=recipe_kcal,
                recipe_proteins=recipe_proteins, recipe_carbs=recipe_carbs, recipe_fats=recipe_fats,
                image_path=recipe_image_path, wanted_kcal=wanted_kcal, wanted_proteins=wanted_proteins,
                wanted_carbs=wanted_carbs, wanted_fats=wanted_fats
            )
        )

        conn.commit()

        # Check if the insertion was successful
        if result.rowcount == 1:
            message = "INSERTION SUCCESSFUL"
        else:
            message = "FAILED TO INSERT"

        return message


@app.route("/delete_all_recipes")
def delete_all_recipes():
    """
    Deletes all recipes from the database.
    """

    # Connect to the database
    with engine.connect() as conn:
        # Delete all rows from the table
        result = conn.execute(
            recipes.delete()
        )

        conn.commit()

        # Check if the deletion was successful
        if result.rowcount >= 0:
            message = "DELETION SUCCESSFUL"
        else:
            message = "FAILED TO DELETE"

        return message


@app.route("/latest_recipe")
def latest_recipe():
    """
    Reads the latest recipe from the database and returns it as a dict.
    """

    # Connect to the database
    with engine.connect() as conn:
        # Fetch the first recipe from the table
        recipe = conn.execute(
            recipes.select().limit(1)
        ).fetchone()

        # Check if a recipe was found
        if recipe:
            recipe_dict = {
                "calories": recipe.recipe_kcal,
                "carbs": recipe.recipe_carbs,
                "fat": recipe.recipe_fats,
                "id": recipe.recipe_id,
                "image": recipe.image_path,
                "protein": recipe.recipe_proteins,
                "title": recipe.recipe_title,
                "wanted_kcal": recipe.wanted_kcal,
                "wanted_proteins": recipe.wanted_proteins,
                "wanted_carbs": recipe.wanted_carbs,
                "wanted_fats": recipe.wanted_fats,
            }
        else:
            recipe_dict = {}

        return jsonify(recipe_dict)


@app.route("/get_link")
def get_link():
    """
    Get the link to a recipe, identified by the recipe id
    """

    try:
        recipe_id = request.args.get('recipe_id', None)
    except BadRequestKeyError:
        return "Error"

    response = requests.request("GET", url + "recipes/{}/information".format(recipe_id), headers=headers).json()

    return response["sourceUrl"]


@app.route("/startpage")
def startpage():
    return "<h1>Startpage</h1>"


if __name__ == "__main__":
    app.run()

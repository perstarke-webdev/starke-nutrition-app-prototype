from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float

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
    Column('recipe_proteins', Float),
    Column('recipe_carbs', Float),
    Column('recipe_fats', Float),
    Column('image_path', String(255))
)

# Connect to the database
with engine.connect() as conn:
    # Insert a new row into the table
    result = conn.execute(
        recipes.insert().values(recipe_id=4, recipe_title='Salmon with Roasted Vegetables', recipe_kcal=500,
                                recipe_proteins=40, recipe_carbs=20, recipe_fats=30,
                                image_path='path/to/salmon_with_roasted_vegetables.jpg'))

    conn.commit()

    # Check if the insertion was successful
    if result.rowcount == 1:
        print("Insertion successful")
    else:
        print("Insertion failed")

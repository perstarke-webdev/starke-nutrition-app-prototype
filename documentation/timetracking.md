# Time-tracking for developing the prototype

### Monday, 19.02.24

- 75 min
  - Watch Quasar Tutorials
  - Install node.js, yarn and Quasar
  - Testwise create and run Quasar project in localhost
  - Watch Vue + Flask Tutorial
- 75 min
  - Add basic setup for Quasar + Flask project in repo
  - Some trying out with Quasar:
    - create and style header
    - remove left toolbar
    - add placeholder footer nav buttons

### Tuesday, 20.02.24

- 100 min
  - Create nutritional requirements input table
  - Add recommended recipe placeholder
  - -> Coach view frontend (with placeholders) finished for now
- 100 min
  - Create clickable nav for trainee/coach view
  - Add second page for trainee view with second layout
  - add routes
- 20 min
  - Quick update with placeholders for trainee view
- 90 min
  - Basic (~29€/month) subscription to Spoonacular API
  - Basic Spoonacular setup with headers and key as ENV
  - Create Python function to continuously get new random recipe with given (currently hard-coded) 
    nutrients (within 10%-range) using Spoonacular

### Wedesney, 21.02.24

- 30 min
  - Change Python function for getting recipe so that nutrients are given as parameters, not hard-coded
- 45 min
  - Setup CORS for Flask
  - Setup Axios for making HTTP requests to the backend in the frontend
- 45 min
  - Get recipe with given nutrient values, givable in a table,
    and display title, image and nutrients instead of placeholder

### Thurday, 22.02.24

- 30 min
  - Read about testing in Python (and in general)
- 60 min
  - Trying around with pytests in Flask
  - Get basic Flask testing up and running, but without real testing functionality yet
- 30 min
  - Write meaningful tests for get_recipe route


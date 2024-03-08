## Documentation of the deployment decisions and steps

### Backend 
Vercel for backend, as its quite simple and straightforward, and offers easy ENV usage as well, plus
has good documentation for Python / Flask projects. 

Spoonacular API key is given to Vercel as ENV and automatically encrypted, and can then be accessed
in the code directly. Solves the ENV-task quite conveniently for our purpose.  

I created a Vercel project for the backend deployment, the backend api is now reachable at
[https://sna-prototype-backend-v2.vercel.app](https://sna-prototype-backend-v2.vercel.app) + the respective route.  
So for example an endpoint for getting a recipe would be 
[https://sna-prototype-backend-v2.vercel.app/get_recipe?kcal=500&proteins=50&carbs=50&fats=10](https://sna-prototype-backend-v2.vercel.app/get_recipe?kcal=500&proteins=50&carbs=50&fats=10).

Vercel automatically deploys on Git commit&push, so all pushed changes are deployed automatically.

### Frontend

Frontend deployment via Vercel as well.  
Quasar offers good docu and support for that.  
Available here: 
[https://sna-prototype-frontend.vercel.app/#/coach](https://sna-prototype-frontend.vercel.app/#/coach)  

Not deploying on commit&push automatically, as quasar project must be build first
and then can be easily deployed via CLI:
- Navigate to the ```starke-nutrition-coaching-frontend``` directory
- Run ```quasar build```
- Navigate to ```dist/spa```
- Run ```vercel```
- Follow the given steps there





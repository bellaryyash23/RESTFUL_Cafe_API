# 🛌RESTful Cafe API using Postman, SQLite & Flask of Python

🌟An API which provides users details regarding Cafés in London and allows users to GET cafes data, POST a new café entry, PATCH update the coffee price of certain cafe &
DELETE a café from the database. The API is built on the REST API architecture and provides access to the cafe database built using SQLite. Postman application is used for
sending requests to API in an easy way. The server for the API is hosted locally using Flask.

🌟Also, one neat trick of using Postman for API requests is its feature to create documentation for the designed API. 

📃View Documentation: https://documenter.getpostman.com/view/17703132/2s7Z7ZoZMz

👉The Home page for details regarding the API along with documentation is provided on the home route of the API. 

![Home Page of API](https://github.com/bellaryyash23/RESTFUL_Cafe_API/blob/master/samples/home.jpg?raw=true)

👆Home Page of API for details👆

👉The different request methods setup for API are listed below:

👉GET: /all -> This route returns a JSON with the data from all cafes in the database.

![GET request of API for all cafes](https://github.com/bellaryyash23/RESTFUL_Cafe_API/blob/master/samples/get.JPG?raw=true)

👆GET all cafes list👆

👉GET: /random -> Returns a random cafe from the database.

![GET request of API for random cafe](https://github.com/bellaryyash23/RESTFUL_Cafe_API/blob/master/samples/random.JPG?raw=true)

👆GET request of API for random cafe👆

👉GET: /search?loc='value' -> The /search route will search the cafe database for a cafe that matches the location queried. Use the loc parameter to pass a location name.

![GET request of API for a cafe with paricular location](https://github.com/bellaryyash23/RESTFUL_Cafe_API/blob/master/samples/search.JPG?raw=true)

👆GET request of API for a cafe with paricular location👆

👉POST: /add -> Adds a new cafe entry to the database. Requires authentication with api-key parameter.

![POST request of API to add a new cafe entry to database](https://github.com/bellaryyash23/RESTFUL_Cafe_API/blob/master/samples/post.JPG?raw=true)

👆POST request of API to add a new cafe entry to database👆

👉PATCH: /update-price/1?new_price=$5 -> Update the price of a black coffee at a particular cafe. Using the id and new_price parameters.

![PATCH request of API to update coffee price for particular cafe](https://github.com/bellaryyash23/RESTFUL_Cafe_API/blob/master/samples/patch.JPG?raw=true)

👆PATCH request of API to update coffee price for particular cafe👆

👉DELETE: /report-closed/9?api_key=TopSecretAPIKey -> Deletes a cafe from the database. You will need to provide the id of the cafe to delete as a route. 
You will also need to provide a valid API for this operation to be allowed.

![DELETE request of API to delete a paricular cafe](https://github.com/bellaryyash23/RESTFUL_Cafe_API/blob/master/samples/delete.JPG?raw=true)

👆DELETE request of API to delete a paricular cafe👆

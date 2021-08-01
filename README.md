# REST-API-for-Countries-Spatial-Data

## In this challenge we will develop python django REST api for spatial data and test the API Data

You can download world countries geojson data here: https://datahub.io/core/geo-countries#resource-geo-countries_zip 

### Tasks

- Download the world countries geojson data 
- Create REST API for that data.  
- Test CRUD operations for a country. (Delete a country by name, insert new country) 
- Test spatial and non spatial query 
  - Non spatial query : Get all matching country names by string 
  - Spatial query: Get all counties Intersecting with India 
 
### Requirements and submission guidelines 

- The solution needs to be implemented in Python, preferably 3.x 
- Please use multiple docker containers for the application. 
  - Ex: One container for Django APP, One for database.  
- Please use docker-compose to run the application.  
- Code and commit messages should be treated as you would on a real- world task 
- Please take some time to think about code quality and testing 
- Provide a README with instructions on how to set up, run and test the solution

### Installation

It's a pretty simple 2 step installation process. Installation will take care of the following:
- Setting up the django, geo-django docker container
- Setting up the post-gis docker container
- Loading up the countries data in the db
- Running the geo-django app and serving it on port 8000

#### Steps
- docker-compose build
- docker-compose up

### Api Lists
| S.No 	| Operation Type| Use case    	                    | Api (curl) 	| Description                                                               |
|------	| ------------ |---------------                     |------------	| ------------------------------------------------------------------------- |
| 1    	| CRUD          | List countries   	                | curl "http://localhost:8000/countries/"                                                   | Return a list of countries in paginated manner with links to previous and next cursor |
| 2    	| CRUD          | Search by matching country name   | curl http://localhost:8000/countries/?search=India                                        | Return a list of countries which matches the input name                               |
| 3    	| CRUD          | Create a country                  | curl -X POST "http://localhost:8000/countries/Bangladesh/"  -d "{  \"name\": \"country name\", \"geom\": \"your geom\" }"| |
| 4    	| CRUD          | Get a country                     | curl "http://localhost:8000/countries/India"              	                            |                                                                                   |
| 5    	| CRUD          | Delete a country                  | curl -X DELETE "http://localhost:8000/countries/Bangladesh/" |                            |
| 6    	| CRUD          | Update a country                  | curl -X PUT "http://localhost:8000/countries/Bangladesh/"  -d "{  \"geom\": \"your geom\" }"| |
| 7    	| SPACTIAL      | Get intersecting countries        | curl http://localhost:8000/countries/India/get_intersecting_countries/                    | Gives a list of countries wich intersects with this country|
| 8    	| SPACTIAL      | Get touching countries            | curl http://localhost:8000/countries/India/get_neighbor_countries/                        | Gives a list of countries wich touches with this country|

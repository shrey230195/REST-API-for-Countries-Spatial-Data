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
- Provide a README with instructions on how to set up, run and test the

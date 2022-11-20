# Lab3_SquirrelDB
## BigQuery Database
This API is meant to facilitate the management of the squirrel sightings
on Brooklyn College's campus.

Since BigQuery is a Cloud Database there is no software to install on the local machine. However, you will need to have Service Account Credentials saved somewhere locally to be referenced in the `Settings.py` file, at the top. This lets Google authenticate the API before it accesses the data in the cloud.
# Setup
## Please run the make file to:
- Check for or install Python and virtual environment
- Activate Python virtual environment
- Install dependencies (requirements.txt)
- Make migrations and migrate
- Run Server (http://localhost:8000/)

# Endpoints
## create
This database supports inserting new squirrel sightings in detail for accurate tracking of squirrel species and associated behavior. New sightings show genealogy migration across campus and mating patterns throughout the year. A constant influx of new sightings is important to refine and derive truer insights from our squirrel population.

To access this functionality navigate to `/create` in the browser.
## read
This database supports reading information to gain insights from the data. Since there is one large table, no joins need to be performed to query the database using as many constraints as necessary. Insights can be obtained very efficiently.

To access this functionality navigate to `/view-all` in the browser.
## update
This database supports updating information in case of human error while inputting data. Mistakes will happen and it is important to have this functionality to preserve the integrity of the data.

To access this functionality navigate to `/update` in the browser.
## delete
This database supports deleting information in case a duplicate sighting is entered by mistake.Duplicate data can skew findings if left unchecked.

To access this functionality navigate to `/delete` in the browser.
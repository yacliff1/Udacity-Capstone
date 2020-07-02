This is the capstone full-stack development project.

This project simulates a casting agency with ways to view, add, edit, and delete actors and movies.

Login and set up with auth0 in the link below:

https://yangcliff.auth0.com/authorize?audience=castingagency&response_type=token&client_id=2TeVQLv79mBscs1Nligg4GtoCvnjBFr2&redirect_uri=https://castingagencyprojectyangcliff.herokuapp.com/login-results

url for the API is: https://castingagencyprojectyangcliff.herokuapp.com/

Three roles are Casting Assistant, Casting Director, and Executive Producer

Endpoints:

'/actors' GET: Endpoint fetches all actors in database and displays them.

'/actors/create' POST: Endpoint creates a new actor in database.

'/actors/int:actor_id' PATCH: Endpoint modifies an actor in the database.

'/actors/int:actor_id' DELETE: Endpoint deletes an actor in the database.

'/movies' GET: Endpoint fetches all movies in database and displays them.

'/movies/create' POST: Endpoint creates a new movie in the database.

'/movies/int:movie_id' PATCH: Endpoint modifies a movie in the database.

'/movies/int:movie_id' DELETE: Endpoint deletes a movie in the database.

Casting Assistant can use both get endpoints.

Casting Director has the casting assistant permissions and can create, delete, edit actors as well as edit movies.

Executive Producer has all of the permissions.

Make sure to have an updated requirements.txt
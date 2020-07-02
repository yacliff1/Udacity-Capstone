This is the capstone full-stack development project.

This project simulates a casting agency with ways to view, add, edit, and delete actors and movies.

Login and set up with auth0 in the link below:

https://yangcliff.auth0.com/authorize?audience=castingagency&response_type=token&client_id=2TeVQLv79mBscs1Nligg4GtoCvnjBFr2&redirect_uri=https://castingagencyprojectyangcliff.herokuapp.com/login-results

url for the API is: https://castingagencyprojectyangcliff.herokuapp.com/

Three roles are Casting Assistant, Casting Director, and Executive Producer

Project Motivation: I chose this project because I wanted to test the skills that I have accumulated throughout the entire course.
It allowed me to practice more on developing skills in creating models, databases, authorization, and deployment.

Endpoints:

'/actors' GET: Endpoint fetches all actors in database and displays them.

{
    "success": true,
    "actors": [
    {
        "age": 40,
        "gender": "male",
        "id": 1,
        "name": "Joseph Lee"
    },
    {
        "age": 50,
        "gender": "male",
        "id": 2,
        "name": "John Doe"
    }
    ],
    "total_actors": 2
}

'/actors/create' POST: Endpoint creates a new actor in database.

{
    "success": true,
    "actor": [
    {
        "age": 20,
        "gender": "male",
        "id": 1,
        "name": "New Guy"
    }
    ]
}

'/actors/int:actor_id' PATCH: Endpoint modifies an actor in the database.

{
    "success": true,
    "actor": [
    {
        "age": 20,
        "gender": "male",
        "id": 1,
        "name": "Edited Guy"
    }
    ]
}

'/actors/int:actor_id' DELETE: Endpoint deletes an actor in the database.

{
    "success": true,
    "deleted_actor": 1
}

'/movies' GET: Endpoint fetches all movies in database and displays them.

{
    "success": true,
    "movies": [
    {
        "title": "Inception",
        "release_date": "July 16, 2010"
    },
    {
        "title": "Another movie",
        "release_date": "March 23, 2014"
    }
    ],
    "total_movies" : 2
}

'/movies/create' POST: Endpoint creates a new movie in the database.

{
    "success": true,
    "movies": [
    {
        "title": "New Movie",
        "release_date": "Random Date"
    }
    ]
}

'/movies/int:movie_id' PATCH: Endpoint modifies a movie in the database.

{
    "success": true,
    "movies": [
    {
        "title": "Edited Movie",
        "release_date": "Edited Date"
    }
    ]
}

'/movies/int:movie_id' DELETE: Endpoint deletes a movie in the database.

{
    "success": true,
    "deleted_movie": 1
}

Casting Assistant can use both get endpoints.

Casting Director has the casting assistant permissions and can create, delete, edit actors as well as edit movies.

Executive Producer has all of the permissions.

Make sure to have an updated requirements.txt
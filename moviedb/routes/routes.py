from fastapi import APIRouter,HTTPException, Query, Path
from moviedb.models.models import NewMovie
from moviedb.config.config import client,collection
from moviedb.utils.validate import is_valid_korean_movie


movie_router = APIRouter()







                                                        
 
# Step 1: Validate the title
@movie_router.post("/wizard/step1")
def step1(step1_input: NewMovie):
    title = step1_input.title

    if not is_valid_korean_movie(title):
        raise HTTPException(
            status_code=400,
            detail="The provided title is not a valid Korean movie title."
        )

    # If the title is valid, you can proceed to Step 2
    # You may want to store the title for later use
    return {"message": "Valid Korean movie title. Proceed to Step 2."}


@movie_router.get('/')
async def hello_world():
    return "hello world"
# @movie_router.post("/add-movie/")
# def add_movie(new_movie: NewMovie):
#     # Perform validation and database insertion here
#     # You can also check if the country is "Korean" and take appropriate action

#     # Replace this with your database insertion logic
#     # For example, if you are using MongoDB:
#     # mongo_collection.insert_one(new_movie.dict())

#     return {"message": "Movie added successfully"}
# # Define the route to search movies
# @movie_router.get("/search-movies/{search_type}")
# def search_movies(
#     search_type: str = Path(..., title="Search Type (actor, title, genre)"),
#     search_query: str = Query(..., title="Search Query"),
# ):
#     # Define an empty list to store search results
#     search_results = []

#     if search_type == "actor":
#         # Search for movies based on actor and return the latest movie and all others
#         cursor = collection.find({"actors": search_query})
#         movies = list(cursor)
#         if movies:
#             movies.sort(key=lambda x: x["release_date"], reverse=True)  # Sort by release date
#             latest_movie = movies[0]
#             other_movies = movies[1:]
#             return {"latest_movie": latest_movie, "other_movies": other_movies}
#         else:
#             raise HTTPException(status_code=404, detail="No movies found for the actor.")

#     elif search_type == "title":
#         # Search for movies based on title and return the most corresponding one
#         cursor = collection.find({"title": {"$regex": f".*{search_query}.*", "$options": "i"}})
#         movies = list(cursor)
#         if movies:
#             movies.sort(key=lambda x: x["title"], key=len)  # Sort by title length (most corresponding)
#             most_corresponding_movie = movies[-1]
#             return {"most_corresponding_movie": most_corresponding_movie}
#         else:
#             raise HTTPException(status_code=404, detail="No movies found for the title.")

#     elif search_type == "genre":
#         # Search for movies based on genre and return in descending order of release date
#         cursor = collection.find({"genre": search_query})
#         movies = list(cursor)
#         if movies:
#             movies.sort(key=lambda x: x["release_date"], reverse=True)  # Sort by release date
#             return movies
#         else:
#             raise HTTPException(status_code=404, detail="No movies found for the genre.")

#     else:
#         raise HTTPException(status_code=400, detail="Invalid search type. Use 'actor', 'title', or 'genre'.")
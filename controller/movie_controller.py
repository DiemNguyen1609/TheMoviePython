from database.database import movies_collection
from model.movie_model import Movie
from bson import ObjectId
from service.conversion_service import convert_objectid_and_decimal

class MovieController:
    
    @staticmethod
    def get_movies():
            results = movies_collection.find()
            movies = Movie.to_list([convert_objectid_and_decimal(result) for result in results])
            return movies

    @staticmethod
    def get_movie(_id: str):
        movie = movies_collection.find_one({"_id": ObjectId(_id)})
        return Movie.to_item(movie) if movie else None
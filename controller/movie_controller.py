from database.database import movies_collection
from model.movie_model import Movie
from bson import ObjectId
from service.conversion_service import convert_objectid_and_decimal
from typing import Dict, Any

class MovieController:
    
    @staticmethod
    def get_movies(page: int = 1, limit: int = 10) -> Dict[str, Any]:
            skip = (page - 1) * limit
            total = movies_collection.count_documents({})
            cursor = movies_collection.find().skip(skip).limit(limit)
            movies = [Movie.to_item(movie) for movie in cursor]
            
            return {
                "page": page,
                "limit": limit,
                "total_items": total,
                "total_pages": (total + limit - 1) // limit,
                "data": [m.model_dump() for m in movies]
            }

    @staticmethod
    def get_movie(_id: str):
        movie = movies_collection.find_one({"_id": ObjectId(_id)})
        return Movie.to_item(movie) if movie else None
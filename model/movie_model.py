from typing import List, Optional, Dict, Union, Any
from pydantic import BaseModel
from datetime import datetime
from service.conversion_service import safe_float, safe_int

class IMDBInfo(BaseModel):
    rating: Optional[float] = 0
    votes: Optional[int] = 0
    id: Optional[int] = 0

class TomatoViewer(BaseModel):
    rating: Optional[float] = 0
    numReviews: Optional[int] = 0
    meter: Optional[int] = 0

class TomatoCritic(BaseModel):
    rating: Optional[float] = 0
    numReviews: Optional[int] = 0
    meter: Optional[int] = 0

class Tomatoes(BaseModel):
    viewer: TomatoViewer
    fresh: Optional[int] = 0
    critic: TomatoCritic
    rotten: Optional[int] = 0
    lastUpdated: Optional[datetime] = None

class Awards(BaseModel):
    wins: Optional[int] = 0
    nominations: Optional[int] = 0
    text: Optional[str] = None

class Movie(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    plot: Optional[str] = None
    fullplot: Optional[str] = None
    genres: List[str] = []
    runtime: Optional[int] = 0
    cast: List[str] = []
    poster: Optional[str] = None
    languages: List[str] = []
    released: Optional[datetime] = None
    directors: List[str] = []
    rated: Optional[str] = None
    awards: Optional[Awards] = None
    lastupdated: Optional[str] = None
    year: Optional[int] = 0
    imdb: Optional[IMDBInfo] = None
    countries: List[str] = []
    type: Optional[str] = None
    tomatoes: Optional[Tomatoes] = None
    num_mflix_comments: Optional[int] = 0

    @staticmethod
    def _parse_awards(data: Dict[str, Any]) -> Awards:
        return Awards(
            wins=data.get("wins", 0),
            nominations=data.get("nominations", 0),
            text=data.get("text", "")
        )

    @staticmethod
    def _parse_imdb(data: Dict[str, Any]) -> IMDBInfo:
        return IMDBInfo(
            rating=safe_float(data.get("rating", 0.0)),
            votes=safe_int(data.get("votes", 0)),
            id=safe_int(data.get("id", 0)),
        )

    @staticmethod
    def _parse_tomatoes(data: Dict[str, Any]) -> Tomatoes:
        viewer_data = data.get("viewer") or {}
        critic_data = data.get("critic") or {}
        
        return Tomatoes(
            viewer=TomatoViewer(
                rating=safe_float(viewer_data.get("rating")),
                numReviews=safe_int(viewer_data.get("numReviews")),
                meter=safe_int(viewer_data.get("meter")),
            ),
            fresh=safe_int(data.get("fresh")),
            critic=TomatoCritic(
                rating=safe_float(critic_data.get("rating")),
                numReviews=safe_int(critic_data.get("numReviews")),
                meter=safe_int(critic_data.get("meter")),
            ),
            rotten=safe_int(data.get("rotten")),
            lastUpdated=data["lastUpdated"] if "lastUpdated" in data else None,
        )


    @classmethod
    def to_item(cls, data: Dict[str, Any]):
        return cls(
            id=str(data.get("_id", "")),
            title=data.get("title", ""),
            plot=data.get("plot", ""),
            fullplot=data.get("fullplot", ""),
            genres=data.get("genres", []),
            runtime=data.get("runtime", 0),
            cast=data.get("cast", []),
            poster=data.get("poster", ""),
            languages=data.get("languages", []),
            released=data["released"] if "released" in data else None,
            directors=data.get("directors", []),
            rated=data.get("rated", ""),
            awards=cls._parse_awards(data.get("awards", {})),
            lastupdated=data.get("lastupdated", ""),
            year=safe_int(data.get("year")),
            imdb=cls._parse_imdb(data.get("imdb", {})),
            countries=data.get("countries", []),
            type=data.get("type", ""),
            tomatoes=cls._parse_tomatoes(data.get("tomatoes", {})),
            num_mflix_comments=data.get("num_mflix_comments", 0)
        )

    @classmethod
    def to_list(cls, data_list: List[Dict[str, Any]]):
        return [cls.to_item(item) for item in data_list]

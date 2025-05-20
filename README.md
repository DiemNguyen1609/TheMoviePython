# Python Project with MongoDB

This project is a Python-based application that integrates with MongoDB and uses FastAPI for building APIs.

## Prerequisites
1. Install Python (>= 3.8).
2. Install MongoDB and ensure it is running. On macOS, you can start MongoDB using:
   ```bash
   brew services start mongodb-community
   pip install fastapi uvicorn pymongo motor
3. To run project
   ```bash
   cd <project>
   
   # Create a virtual environment
   source venv/bin/activate
   # Activate the virtual environment
   source venv/bin/activate
   # Install dependencies and Save dependencies
   pip install uvicorn
   pip freeze > requirements.txt
   # Deactivate the virtual environment
   deactivate   
   # Run project
   uvicorn main:app --reload

## MongoDB
MongoDB is a popular NoSQL database. It is a document-oriented database, which means that data is stored as documents, rather than rows and columns.
Access localhost url: mongodb://mongo:27017

## FastAPI
FastAPI is a modern, fast (high performance), web framework for building APIs with Python 3.6+ based on starlette.
Access localhost docs: http://localhost:8000/docs
Access localhost redocs: http://localhost:8000/redocs

## Pydantic
Pydantic is a data validation and settings management library.

## Project Structure
project/
├── app/
│   └── __init__.py
├── model/
│   ├── model.py
│   └── *_model.py
├── router/
│   ├── router.py
│   └── *_router.py
├── controller/
│   ├── controller.py
│   └── *_controller.py
├── database/
│   └── database.py
├── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


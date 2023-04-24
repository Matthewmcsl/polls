# Fiddling with FastAPI and Github's API!
Can we find a person's github information just by parsing their username??

## Technologies
- Python 3.9+
- FastAPI
- Poetry
- Uvicorn

## Local Development
1. Clone repo -> `cd` into repo dir
2. Ensure [Poetry](https://python-poetry.org/docs/basic-usage/)
3. Create virtual environment: `python3 -m venv venv`
4. Activate virtual environment `source venv/bin/activate`
5. Install dependencies: `poetry install` -> `poetry init`
6. Run server: `uvicorn main:app --reload`
7. Access swagger: http://127.0.0.1:800/docs  

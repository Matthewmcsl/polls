Drawn massive inspiration (and copied from) [Gwenf](https://github.com/gwenf/python-polls)

# polls polls!
1. Anyone can vote
2. Anyone can add an option to the poll
3. Dont need to be logged in unless adding options to the poll

## Technologies
- Python 3.9+
- FastAPI
- Poetry
- Uvicorn
- Pydantic

## Local Development
1. Clone repo -> `cd` into repo dir
2. Ensure [Poetry](https://python-poetry.org/) is installed 
3. create virtual env: `python3 -m venv venv`
4. Install dependencies: `poetry install`
5. activate virtual env `source venv/bin/activate`
6. Run server: `uvicorn main:app --reload`
7. access swagger: http://127.0.0.1:8000/docs

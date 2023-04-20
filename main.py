from fastapi import FastAPI
import requests
import json

app = FastAPI()

# asynchronous function
## api.github.com
@app.get("/github/{username}")
async def get_github_profile(username: str):
    response = requests.get(f"https://api.github.com/users/{username}")
    # to check if my requests is successful
    if response.status_code == 200:
        user_json = response.json()
        # user_dict = json.loads(user_json)
        public_repo_cnt = user_json["public_repos"]

        return public_repo_cnt
    else:
        return {"error": "User not found"}


# def get_repo_count(username:str):
#     repo_response = requests.get(f"https://api.github.com/user/{username}/")

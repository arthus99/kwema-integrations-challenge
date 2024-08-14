from fastapi import HTTPException
import httpx
from typing import List, Dict

GITHUB_API_URL = "https://api.github.com"

async def get_user_repositories(username: str):
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching repositories from GitHub")
        return response.json()

async def get_pull_requests_count(username: str, repo_name: str):
    url = f"{GITHUB_API_URL}/repos/{username}/{repo_name}/pulls?state=closed"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error fetching pull requests from GitHub")
        
        pull_requests = response.json()
        accepted_count = sum(1 for pr in pull_requests if pr.get("merged_at"))
        return accepted_count

async def get_languages_from_repositories(username: str):
    repos = await get_user_repositories(username)
    languages = []
    for repo in repos:
        repo_name = repo.get("name")
        if repo_name:
            url = f"{GITHUB_API_URL}/repos/{username}/{repo_name}/languages"
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                if response.status_code == 200:
                    repo_languages = response.json()
                    languages.extend(repo_languages.keys())
    return languages

async def fetch_user_activity(self, username: str, activity_type: str, since_date: str) -> List[Dict]:
    url = f"{GITHUB_API_URL}/search/{activity_type}?q=author:{username}+created:>{since_date}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=f"Error fetching {activity_type} from GitHub")
        return response.json().get('items', [])



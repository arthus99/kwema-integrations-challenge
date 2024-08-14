from fastapi import FastAPI, HTTPException
from models import UserInsights
from github_api import get_user_repositories, get_pull_requests_count, get_languages_from_repositories
from metricas.languages import LanguagesMetric
from metricas.pull_requests import PullRequestsMetric
from metricas.activity import ActivityMetric


app = FastAPI()

@app.get("/user-insights/{username}",
         summary="Get Programming Language and Activity Insights for a GitHub User",
         description="Returns the top 3 most common programming languages used by the specified GitHub user, along with their count, and the repositories with the highest number of accepted pull requests. Also provides monthly counts of pull requests, issues, and commits for the last 6 months.",
         response_description="A list of the top 3 most common programming languages and their count, the repositories with the highest number of accepted pull requests, and monthly activity counts of pull requests, issues, and commits.",
         responses={
             200: {
                 "description": "Successful response",
                 "content": {
                     "application/json": {
                         "example": {
                             "languages": [
                                 {"language": "Python", "count": 10},
                                 {"language": "JavaScript", "count": 5},
                                 {"language": "HTML", "count": 3}
                             ],
                             "repositories": [
                                 {"repository": "repo1", "accepted_pull_requests": 12},
                                 {"repository": "repo2", "accepted_pull_requests": 8},
                                 {"repository": "repo3", "accepted_pull_requests": 5}
                             ],
                             "monthly_activity": {
                                 "pull_requests": [5, 3, 2, 4, 6, 7],
                                 "issues": [3, 1, 4, 2, 5, 3],
                                 "commits": [10, 15, 12, 20, 25, 30]
                             }
                         }
                     }
                 }
             },
             404: {
                 "description": "No data found for the user",
                 "content": {
                     "application/json": {
                         "example": {"detail": "No data found for the user"}
                     }
                 }
             },
             500: {
                 "description": "Internal server error",
                 "content": {
                     "application/json": {
                         "example": {"detail": "Error fetching data from GitHub"}
                     }
                 }
             }
         })
async def get_user_insights(username: str):
    metrics = [
        LanguagesMetric(),
        PullRequestsMetric(),
        # ActivityMetric(),
        # Add new metrics here
    ]

    results = {}
    for metric in metrics:
        try:
            result = await metric.calculate(username)
            results.update(result)
        except HTTPException as e:
            raise HTTPException(status_code=e.status_code, detail=f"Error fetching data: {e.detail}")

    if not results.get('languages') and not results.get('repositories') and not results.get('monthly_activity'):
        raise HTTPException(status_code=404, detail="No data found for the user")

    return results

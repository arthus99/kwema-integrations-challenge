# metricas/pull_requests.py

from typing import Dict
from metricas.base import Metric
from github_api import get_user_repositories, get_pull_requests_count

class PullRequestsMetric(Metric):
    async def calculate(self, username: str) -> Dict:
        repos = await get_user_repositories(username)
        repo_pull_counts = []
        for repo in repos:
            repo_name = repo.get("name")
            if repo_name:
                accepted_count = await get_pull_requests_count(username, repo_name)
                repo_pull_counts.append((repo_name, accepted_count))
        top_repositories = sorted(repo_pull_counts, key=lambda x: x[1], reverse=True)[:3]
        return {"repositories": [{"repository": repo, "accepted_pull_requests": count} for repo, count in top_repositories]}

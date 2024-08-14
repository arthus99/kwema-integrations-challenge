# metricas/activity.py

from typing import Dict, List
from datetime import datetime, timedelta
from fastapi import HTTPException
import httpx
from metricas.base import Metric


class ActivityMetric(Metric):
    async def fetch_user_activity(self, username: str, activity_type: str, since_date: str) -> List[Dict]:
        url = f"https://api.github.com/search/{activity_type}?q=author:{username}+created:>{since_date}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail=f"Error fetching {activity_type} from GitHub")
            return response.json().get('items', [])

    async def calculate(self, username: str) -> Dict:
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=180)
        date_format = "%Y-%m-%dT%H:%M:%SZ"

        monthly_counts = {
            'pull_requests': [0] * 6,
            'issues': [0] * 6,
            'commits': [0] * 6
        }

        for i in range(6):
            start_of_month = start_date.replace(day=1) + timedelta(days=30 * i)
            end_of_month = start_of_month + timedelta(days=30)
            since_date = start_of_month.strftime(date_format)
            until_date = end_of_month.strftime(date_format)

            pull_requests = await self.fetch_user_activity(username, 'pulls', since_date)
            issues = await self.fetch_user_activity(username, 'issues', since_date)
            commits = await self.fetch_user_activity(username, 'commits', since_date)

            monthly_counts['pull_requests'][i] = len(pull_requests)
            monthly_counts['issues'][i] = len(issues)
            monthly_counts['commits'][i] = len(commits)

        return {
            "monthly_activity": {
                "pull_requests": monthly_counts['pull_requests'],
                "issues": monthly_counts['issues'],
                "commits": monthly_counts['commits']
            }
        }

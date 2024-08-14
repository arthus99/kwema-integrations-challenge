# metricas/activity_pattern.py

from  metricas.base import Metric
from github_api import fetch_user_activity
import httpx
from datetime import datetime, timedelta
from fastapi import HTTPException, Query
from collections import Counter
from typing import List, Dict

class ActivityPatternMetric(Metric):
    async def get_user_activity(
    username: str = Query(..., description="The GitHub username"),
    activity_type: str = Query(..., description="The type of activity to fetch (e.g., issues, pulls)"),
    since_date: str = Query(..., description="Fetch activities since this date (format: YYYY-MM-DD)")
    ):
        try:
            activities = await fetch_user_activity(username, activity_type, since_date)
            return activities
        except HTTPException as e:
            raise e

    async def calculate(self, username: str) -> Dict:
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=365)  # Analizar el último año
        date_format = "%Y-%m-%dT%H:%M:%SZ"

        activities = await self.fetch_user_activity(username, 'events', start_date.strftime(date_format))
        
        days_of_week = Counter()
        time_of_day = Counter()
        
        for activity in activities:
            created_at = datetime.strptime(activity['created_at'], date_format)
            day_of_week = created_at.strftime("%A")
            hour_of_day = created_at.hour
            
            days_of_week[day_of_week] += 1
            if 0 <= hour_of_day < 12:
                time_of_day['Morning'] += 1
            elif 12 <= hour_of_day < 18:
                time_of_day['Afternoon'] += 1
            else:
                time_of_day['Evening'] += 1
        
        return {
            "activity_pattern": {
                "days_of_week": dict(days_of_week),
                "time_of_day": dict(time_of_day)
            }
        }

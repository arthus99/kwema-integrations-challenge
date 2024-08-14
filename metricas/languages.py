# metricas/languages.py

from typing import Dict
from collections import Counter
from  metricas.base import Metric
from github_api import get_languages_from_repositories

class LanguagesMetric(Metric):
    async def calculate(self, username: str) -> Dict:
        languages = await get_languages_from_repositories(username)
        language_counter = Counter(languages)
        most_common_languages = language_counter.most_common(3)
        return {"languages": [{"language": lang, "count": count} for lang, count in most_common_languages]}

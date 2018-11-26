from app.models.daily_news import DailyNews


class GroupNews:
    def __init__(self, daily_news):
        self.news = [
            DailyNews(*[field for field in news]).__dict__
            for news in daily_news
        ]

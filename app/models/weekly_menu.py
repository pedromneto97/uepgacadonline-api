from app.models.daily_menu import DailyMenu


class WeeklyMenu:
    def __init__(self, daily_menus):
        self.daily_menus = [
            DailyMenu(*[field for field in daily_menu]).__dict__
            for daily_menu in daily_menus
        ]

import requests


class EpicGames:
    __BASE_API_URL = "https://store-site-backend-static.ak.epicgames.com/"

    def __init__(
        self, locale: str = "en-US", country: str = "US", allow_countries: str = "US"
    ) -> None:
        """Initialize EpicGames

        Args:
            locale (str, optional): Locale. Defaults to "en-US".
            country (str, optional): Country. Defaults to "US".
            allow_countries (str, optional): Allow countries. Defaults to "US".
        """
        self.__locale = locale
        self.__country = country
        self.__allow_countries = allow_countries

    @property
    def locale(self) -> str:
        """Return locale

        Returns:
            str: Locale
        """
        return self.__locale

    @property
    def country(self) -> str:
        """Return country

        Returns:
            str: Country
        """
        return self.__country

    @property
    def allow_countries(self) -> str:
        """Return allow countries

        Returns:
            str: Allow countries
        """
        return self.__allow_countries

    @property
    def base_api_url(self) -> str:
        """Return Epic Games API URL

        Returns:
            str: Epic Games API URL
        """
        return self.__BASE_API_URL

    def get_full_url(self, path: str) -> str:
        """Return full URL

        Args:
            path (str): API path

        Returns:
            str: Full URL
        """
        return f"{self.base_api_url}{path}"

    def _requests(self, path: str, params: dict) -> dict:
        """Make a request to Epic Games API

        Args:
            path (str): API path
            params (dict): Request parameters

        Returns:
            dict: Response
        """
        response = requests.get(self.get_full_url(path), params=params)
        return response.json()

    def get_free_games(self) -> dict:
        """Return free games

        Returns:
            dict: Free games
        """
        return self._requests(
            "freeGamesPromotions",
            {
                "locale": self.locale,
                "country": self.country,
                "allowCountries": self.allow_countries,
            },
        )

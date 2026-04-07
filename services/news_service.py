# services/news_service.py

import requests
from models.article import Article
from config import API_KEY, BASE_URL

class NewsService:
    def __init__(self):
        self.api_key  = API_KEY
        self.base_url = BASE_URL

    def _build_url(self, endpoint):
        """Build full API URL"""
        return f"{self.base_url}/{endpoint}"

    def _parse_articles(self, data, category="general"):
        """Convert raw API response → list of Article objects"""
        articles = []

        if data.get("status") != "ok":
            print("❌ API Error:", data.get("message", "Unknown error"))
            return articles

        for item in data.get("articles", []):
            # Skip articles with missing title
            if not item.get("title"):
                continue

            article = Article(
                title        = item.get("title", "No Title"),
                description  = item.get("description", ""),
                url          = item.get("url", ""),
                source       = item.get("source", {}).get("name", "Unknown"),
                author       = item.get("author", "Unknown"),
                published_at = item.get("publishedAt", ""),
                category     = category
            )
            articles.append(article)

        return articles

    def fetch_top_headlines(self):
        """Fetch top headlines — works on free plan"""
        try:
            url    = self._build_url("top-headlines")
            params = {
                "sources": "bbc-news,cnn,the-hindu,reuters",
                "apiKey" : self.api_key
            }
            response = requests.get(url, params=params)
            data     = response.json()

            # Debug: show raw response if 0 articles
            if data.get("status") != "ok":
                print("❌ API Error:", data.get("message"))

            return self._parse_articles(data, category="headlines")

        except requests.exceptions.ConnectionError:
            print("❌ No internet connection!")
            return []
        except Exception as e:
            print(f"❌ Error: {e}")
            return []

    def fetch_by_category(self, category):
        """Fetch news by category"""
        try:
            url    = self._build_url("everything")
            params = {
                "q"       : category,  # search by keyword instead
                "language": "en",
                "sortBy"  : "publishedAt",
                "apiKey"  : self.api_key
            }
            response = requests.get(url, params=params)
            data     = response.json()
            return self._parse_articles(data, category=category)

        except requests.exceptions.ConnectionError:
            print("❌ No internet connection!")
            return []
        except Exception as e:
            print(f"❌ Error: {e}")
            return []

    def fetch_by_keyword(self, keyword):
        """Search news by keyword"""
        try:
            url    = self._build_url("everything")
            params = {
                "q"       : keyword,
                "language": "en",
                "sortBy"  : "publishedAt",
                "apiKey"  : self.api_key
            }
            response = requests.get(url, params=params)
            data     = response.json()
            return self._parse_articles(data, category="search")

        except requests.exceptions.ConnectionError:
            print("❌ No internet connection!")
            return []
        except Exception as e:
            print(f"❌ Error: {e}")
            return []
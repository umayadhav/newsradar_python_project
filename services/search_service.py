# services/search_service.py

from datetime import datetime, timezone

class SearchService:

    def filter_by_source(self, articles, source_name):
        """Filter articles by source name"""
        source_name = source_name.lower()
        filtered = [
            article for article in articles
            if source_name in article.source.lower()
        ]
        return filtered

    def filter_by_keyword(self, articles, keyword):
        """Filter articles where keyword appears in title or description"""
        keyword = keyword.lower()
        filtered = [
            article for article in articles
            if keyword in (article.title or "").lower()
            or keyword in (article.description or "").lower()
        ]
        return filtered

    def filter_today(self, articles):
        """Filter only today's articles"""
        today   = datetime.now(timezone.utc).date()
        filtered = []

        for article in articles:
            try:
                pub_date = datetime.strptime(
                    article.published_at, "%Y-%m-%dT%H:%M:%SZ"
                ).date()
                if pub_date == today:
                    filtered.append(article)
            except:
                pass

        return filtered

    def sort_by_latest(self, articles):
        """Sort articles — newest first"""
        def get_date(article):
            try:
                return datetime.strptime(
                    article.published_at, "%Y-%m-%dT%H:%M:%SZ"
                )
            except:
                return datetime.min

        return sorted(articles, key=get_date, reverse=True)

    def sort_by_source(self, articles):
        """Sort articles alphabetically by source name"""
        return sorted(articles, key=lambda a: a.source.lower())
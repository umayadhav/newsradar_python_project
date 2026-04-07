# models/article.py

class Article:
    def __init__(self, title, description, url, source, author, published_at, category="general"):
        self.title        = title
        self.description  = description
        self.url          = url
        self.source       = source
        self.author       = author
        self.published_at = published_at
        self.category     = category

    def display(self, index):
        """Print article in a clean readable format"""
        print(f"\n[{index}] {self.title}")
        print(f"    📰 Source   : {self.source}")
        print(f"    ✍️  Author   : {self.author or 'Unknown'}")
        print(f"    🕒 Published: {self.format_date()}")
        print(f"    📝 Summary  : {self.description or 'No description available'}")
        print(f"    🔗 URL      : {self.url}")
        print("-" * 60)

    def format_date(self):
        """Convert '2024-01-15T10:30:00Z' → '15 Jan 2024, 10:30'"""
        try:
            from datetime import datetime
            dt = datetime.strptime(self.published_at, "%Y-%m-%dT%H:%M:%SZ")
            return dt.strftime("%d %b %Y, %H:%M")
        except:
            return self.published_at

    def to_dict(self):
        """Convert Article object → dictionary (for saving to JSON)"""
        return {
            "title"       : self.title,
            "description" : self.description,
            "url"         : self.url,
            "source"      : self.source,
            "author"      : self.author,
            "published_at": self.published_at,
            "category"    : self.category
        }

    @classmethod
    def from_dict(cls, data):
        """Convert dictionary → Article object (for loading from JSON)"""
        return cls(
            title        = data.get("title", "No Title"),
            description  = data.get("description", ""),
            url          = data.get("url", ""),
            source       = data.get("source", "Unknown"),
            author       = data.get("author", "Unknown"),
            published_at = data.get("published_at", ""),
            category     = data.get("category", "general")
        )

    def __str__(self):
        return f"{self.title} | {self.source}"

    def __repr__(self):
        return f"Article(title='{self.title}', source='{self.source}')"
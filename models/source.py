# models/source.py

class NewsSource:
    def __init__(self, name, country, language, category, url):
        self.name     = name        # e.g. "TechCrunch"
        self.country  = country     # e.g. "us"
        self.language = language    # e.g. "en"
        self.category = category    # e.g. "technology"
        self.url      = url         # e.g. "https://techcrunch.com"

    def display(self, index):
        """Print source details in clean format"""
        print(f"\n[{index}] {self.name}")
        print(f"    🌍 Country  : {self.country.upper()}")
        print(f"    🗣️  Language : {self.language.upper()}")
        print(f"    📂 Category : {self.category.capitalize()}")
        print(f"    🔗 URL      : {self.url}")
        print("-" * 60)

    def to_dict(self):
        """Convert NewsSource object → dictionary"""
        return {
            "name"    : self.name,
            "country" : self.country,
            "language": self.language,
            "category": self.category,
            "url"     : self.url
        }

    @classmethod
    def from_dict(cls, data):
        """Convert dictionary → NewsSource object"""
        return cls(
            name     = data.get("name", "Unknown"),
            country  = data.get("country", "unknown"),
            language = data.get("language", "unknown"),
            category = data.get("category", "general"),
            url      = data.get("url", "")
        )

    def __str__(self):
        return f"{self.name} ({self.country.upper()}) - {self.category}"

    def __repr__(self):
        return f"NewsSource(name='{self.name}', category='{self.category}')"
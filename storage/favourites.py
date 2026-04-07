# storage/favourites.py

import json
import os
from models.article import Article

class FavouritesManager:
    def __init__(self, filepath="favourites.json"):
        self.filepath    = filepath
        self.favourites  = []
        self.load()         # Auto-load saved favourites on startup

    def load(self):
        """Load favourites from JSON file"""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    data             = json.load(f)
                    self.favourites  = [Article.from_dict(item) for item in data]
                print(f"✅ Loaded {len(self.favourites)} saved favourites.")
            except Exception as e:
                print(f"❌ Error loading favourites: {e}")
                self.favourites = []
        else:
            self.favourites = []

    def save(self):
        """Save favourites to JSON file"""
        try:
            with open(self.filepath, "w") as f:
                json.dump(
                    [article.to_dict() for article in self.favourites],
                    f,
                    indent=4
                )
        except Exception as e:
            print(f"❌ Error saving favourites: {e}")

    def add_article(self, article):
        """Add article to favourites"""
        # Check if already saved (avoid duplicates)
        for fav in self.favourites:
            if fav.url == article.url:
                print("⚠️  Article already in favourites!")
                return

        self.favourites.append(article)
        self.save()
        print(f"⭐ Saved: '{article.title}'")

    def remove_article(self, index):
        """Remove article by index"""
        if 0 <= index < len(self.favourites):
            removed = self.favourites.pop(index)
            self.save()
            print(f"🗑️  Removed: '{removed.title}'")
        else:
            print("❌ Invalid index!")

    def show_favourites(self):
        """Display all saved favourites"""
        if not self.favourites:
            print("\n⚠️  No favourites saved yet!")
            return

        print(f"\n⭐ Your Favourites ({len(self.favourites)} articles)")
        print("=" * 60)
        for i, article in enumerate(self.favourites, 1):
            article.display(i)

    def count(self):
        """Return total number of favourites"""
        return len(self.favourites)

    def __len__(self):
        return len(self.favourites)

    def __str__(self):
        return f"FavouritesManager({len(self.favourites)} articles saved)"
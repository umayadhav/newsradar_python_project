# test.py
from services.news_service import NewsService
from models.digest import DailyDigest

news_service = NewsService()

# Fetch live articles
print("Fetching live news...")
articles = news_service.fetch_top_headlines()
print(f"Total fetched: {len(articles)}\n")

# Test 1: Display digest
print("=" * 60)
print("📋 TEST 1: Display Daily Digest")
print("=" * 60)
digest = DailyDigest(articles)
digest.display()

# Test 2: Export to file
print("\n" + "=" * 60)
print("💾 TEST 2: Export Digest to File")
print("=" * 60)
digest.export_to_file()

# Test 3: Print digest object
print("\n" + "=" * 60)
print("🖨️  TEST 3: Print Digest Object")
print("=" * 60)
print(digest)
print(f"Total articles in digest: {len(digest)}")
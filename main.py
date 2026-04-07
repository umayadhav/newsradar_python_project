# main.py

from services.news_service import NewsService
from services.search_service import SearchService
from storage.favourites import FavouritesManager
from models.digest import DailyDigest

# ── Helpers ───────────────────────────────────────────────
def print_banner():
    print("\n" + "=" * 60)
    print("        📰  NEWSRADAR — Live News Intelligence")
    print("=" * 60)

def print_menu():
    print("\n📌 MAIN MENU")
    print("-" * 40)
    print("1. 🌍 Top Headlines")
    print("2. 💻 Technology News")
    print("3. 🏏 Sports News")
    print("4. 💰 Business News")
    print("5. 🔍 Search by Keyword")
    print("6. ⭐ My Favourites")
    print("7. 📋 Daily Digest")
    print("8. 🚪 Exit")
    print("-" * 40)

def browse_articles(articles, favourites):
    """Let user browse articles and save to favourites"""
    if not articles:
        print("\n⚠️  No articles found!")
        return

    # Display all articles
    for i, article in enumerate(articles[:10], 1):
        article.display(i)

    # Ask user to save any article
    while True:
        print("\nOptions:")
        print("  Enter article NUMBER to save to favourites")
        print("  Press ENTER to go back to menu")
        choice = input("\n→ ").strip()

        if choice == "":
            break

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(articles[:10]):
                favourites.add_article(articles[index])
            else:
                print("❌ Invalid number!")
        else:
            print("❌ Please enter a valid number!")

def search_news(news_service, favourites):
    """Search news by keyword"""
    keyword = input("\n🔍 Enter keyword to search: ").strip()

    if not keyword:
        print("❌ Keyword cannot be empty!")
        return

    print(f"\nSearching for '{keyword}'...")
    articles = news_service.fetch_by_keyword(keyword)

    if not articles:
        print("⚠️  No articles found!")
        return

    print(f"✅ Found {len(articles)} articles\n")
    browse_articles(articles, favourites)

def show_favourites(favourites):
    """Show and manage favourites"""
    favourites.show_favourites()

    if len(favourites) == 0:
        return

    while True:
        print("\nOptions:")
        print("  Enter article NUMBER to remove from favourites")
        print("  Press ENTER to go back to menu")
        choice = input("\n→ ").strip()

        if choice == "":
            break

        if choice.isdigit():
            index = int(choice) - 1
            favourites.remove_article(index)
            favourites.show_favourites()
        else:
            print("❌ Please enter a valid number!")

def show_digest(news_service):
    """Generate and show daily digest"""
    print("\n📋 Generating Daily Digest...")
    articles = news_service.fetch_top_headlines()
    digest   = DailyDigest(articles)
    digest.display()

    # Ask to export
    choice = input("\n💾 Export digest to file? (y/n): ").strip().lower()
    if choice == "y":
        digest.export_to_file()

# ── Main App ──────────────────────────────────────────────
def main():
    # Initialize all services
    news_service   = NewsService()
    search_service = SearchService()
    favourites     = FavouritesManager()

    print_banner()
    print("\n🚀 Welcome to NewsRadar!")
    print("   Your personal news intelligence app.\n")

    while True:
        print_menu()
        choice = input("→ Enter your choice (1-8): ").strip()

        if choice == "1":
            print("\n🌍 Fetching Top Headlines...")
            articles = news_service.fetch_top_headlines()
            articles = search_service.sort_by_latest(articles)
            browse_articles(articles, favourites)

        elif choice == "2":
            print("\n💻 Fetching Technology News...")
            articles = news_service.fetch_by_keyword("technology")
            articles = search_service.sort_by_latest(articles)
            browse_articles(articles, favourites)

        elif choice == "3":
            print("\n🏏 Fetching Sports News...")
            articles = news_service.fetch_by_keyword("sports cricket IPL")
            articles = search_service.sort_by_latest(articles)
            browse_articles(articles, favourites)

        elif choice == "4":
            print("\n💰 Fetching Business News...")
            articles = news_service.fetch_by_keyword("business economy market")
            articles = search_service.sort_by_latest(articles)
            browse_articles(articles, favourites)

        elif choice == "5":
            search_news(news_service, favourites)

        elif choice == "6":
            show_favourites(favourites)

        elif choice == "7":
            show_digest(news_service)

        elif choice == "8":
            print("\n👋 Thanks for using NewsRadar! Goodbye!\n")
            break

        else:
            print("❌ Invalid choice! Please enter 1-8.")

if __name__ == "__main__":
    main()
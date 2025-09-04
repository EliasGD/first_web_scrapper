"""
Required packages:
        pip install requests beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup


def scrape_website(url: str) -> BeautifulSoup:
    """
    Scrapes the given website and returns a BeautifulSoup object of the page content.

    Args:
            url (str): The website URL to scrape.

    Returns:
            BeautifulSoup: Parsed HTML content of the page.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raises HTTPError for bad responses
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


if __name__ == "__main__":
    url = "https://www.cdcr.ca.gov/operations-manual/dom/"
    soup = scrape_website(url)
    # Find all links with class="chapter-toggle-heading-link"
    links = soup.find_all("a", class_="chapter-toggle-heading-link")
    print(f"Found {len(links)} chapter links.")

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(f"Main page: {url}\n\n")

    for i, link in enumerate(links, 1):
        href = link.get("href")
        if not href:
            continue
        # Handle relative URLs
        if href.startswith("/"):
            full_url = f"https://www.cdcr.ca.gov{href}"
        elif href.startswith("http"):
            full_url = href
        else:
            full_url = url.rstrip("/") + "/" + href.lstrip("/")

        print(f"Scraping link {i}/{len(links)}: {full_url}")
        try:
            page_soup = scrape_website(full_url)
            # Get main content (can be customized)
            content = page_soup.get_text(separator="\n", strip=True)
        except Exception as e:
            content = f"Error scraping {full_url}: {e}"

        with open("output.txt", "a", encoding="utf-8") as f:
            f.write(f"\n---\nURL: {full_url}\n---\n")
            f.write(content)
            f.write("\n\n")

    print("All chapter links scraped and saved to output.txt")

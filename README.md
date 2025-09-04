
# Beautiful Web Scrapper

This project scrapes a website using Python and BeautifulSoup. The target URL is configurable.

## Requirements
- Python 3.8 or newer
- `requests` and `beautifulsoup4` packages

## How to Run Locally

1. **Clone the repository**
   ```powershell
   git clone <your-repo-url>
   cd beautiful_web_scrapper
   ```

2. **Install Python dependencies**
   Open a terminal in the project directory and run:
   ```powershell
   pip install requests beautifulsoup4
   ```

3. **Run the scraper**
   ```powershell
   python main.py
   ```

4. **View the output**
   - The scraped content will be saved incrementally to `output.txt` in the project directory.
   - Each chapter link's content will be appended to the file.

## Example Output
After running, check `output.txt` for scraped content from all chapter links on the target page.

## Customization
- To scrape a different website, change the `url` variable in `main.py`.
- The script currently scrapes all links with `class="chapter-toggle-heading-link"` and saves their text content.

## Azure App Service Deployment

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd beautiful_web_scrapper
   ```

2. **Install dependencies**
   Azure App Service will automatically install dependencies listed in `requirements.txt`. If you do not have one, create it:
   ```bash
   echo requests > requirements.txt
   echo beautifulsoup4 >> requirements.txt
   ```

3. **Configure Startup Command**
   In the Azure Portal, set the startup command to run your script:
   ```bash
   python main.py
   ```
   Or set this in the App Service configuration under **Startup Command**.

4. **Deploy to Azure App Service**
   - Use Azure Portal, VS Code Azure extension, or GitHub Actions to deploy your code.
   - Ensure your `main.py` is in the root directory or update the startup command accordingly.

5. **View Output**
   - The script saves the scraped content to `output.txt`.
   - Check the App Service logs and file system for output.

## Notes
- For production, consider handling exceptions and logging output to a file or Azure Application Insights.
- You can modify `main.py` to scrape other URLs by changing the `url` variable.

---
For more details, see [Azure App Service Python Quickstart](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=cmd%2Cbrowser).

## **Overview:**

This script scrapes the targeted html elements from any an article to provide the list in .txt format.

It uses Python's `requests` library to fetch the webpage's content and the `BeautifulSoup` library from `bs4` to parse and extract html elements.

The extracted data can be used for various purposes, such as creating a list, analyzing trends, or archiving.

## **How It Works:**

1. **Request the Webpage:**  
   The script sends a GET request to the specified article URL using the `requests` library. It includes a User-Agent header to mimic a real browser request, ensuring access to the webpage.

2. **Check Response Status:**  
   It checks the HTTP status code of the response to confirm that the request was successful (status code `200`).

3. **Parse HTML Content:**  
   Using `BeautifulSoup`, the HTML content of the webpage is parsed into a structured format.

4. **Extract List Elements:**  
   The script searches for all `<h2>` elements with the class `title2` that contain the elements of list. It then extracts and prints the text of each title.

*Changed this based on your url.

## **Example Output:**

IGN's top 100 ps games..

If the webpage structure matches expectations, the script will print the following (partial) output:

```
1. Hotline Miami 
2. God of War
3. Bloodborne
...
```

## **Requirements:**

1. **Python Version:**  
   Python 3.x is required to run this script.

2. **Libraries:**  
   - `requests`: For sending HTTP requests.  
   - `bs4` (BeautifulSoup): For parsing and extracting HTML content.

   Install these libraries using pip:
   ```bash
   pip install requests beautifulsoup4
   ```

## **Example:**

Below is a snapshot of how the code operates:

![IGN Scraper Example](https://github.com/Bosaif39/example-pics/blob/main/example-output.png?raw=true)

This image demonstrates the successful extraction of game titles printed in the terminal after running the script.

## **Notes:**

- Ensure the URL of the article is up-to-date. If the website's structure changes, you might need to update the class or tag used for finding the titles.
- Always comply with the terms of service of the website being scraped.

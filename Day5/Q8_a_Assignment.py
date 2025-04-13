import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse, urljoin, urldefrag
import sys

def get_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content, response.url
    except Exception as e:
        print(f"Error in  downloading {url}")
        return None, None

def extract_links(base_url, content):
    soup = BeautifulSoup(content, 'html.parser')
    links = set()
    
    for link in soup.find_all('a', href=True):
        href = link['href']
        absolute_url = urljoin(base_url, href)
        absolute_url, _ = urldefrag(absolute_url)  # Remove fragment
        parsed = urlparse(absolute_url)
        
        if parsed.scheme not in ('http', 'https'):
            continue
        
        links.add(absolute_url)
    
    return links

def main(url):
    content, final_url = get_content(url)
    if not content:
        print("Failed to download initial URL")
        return
    
    base_url = final_url if final_url else url
    print(f"Base URL for link resolution: {base_url}")
    
    links = extract_links(base_url, content)
    print(f"Found {len(links)} unique links to download")
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Create a list of URLs to process
        future_to_url = {executor.submit(get_content, link): link for link in links}
        
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                content, final_url = future.result()
                if content:
                    print(f"Successfully downloaded: {url} (length: {len(content)})")
                else:
                    print(f"Failed to download: {url}")
            except Exception as e:
                print(f"Exception occurred while processing {url}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python link_downloader.py <URL>")
        sys.exit(1)
    
    main(sys.argv[1])
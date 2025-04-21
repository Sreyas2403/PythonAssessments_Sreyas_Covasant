import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

def download_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print(f"Downloaded: {url}")
        return response.text
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

def parse_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for tag in soup.find_all('a', href=True):
        href = tag['href']
        full_url = urljoin(base_url, href)
        if urlparse(full_url).scheme in ['http', 'https']:
            links.add(full_url)
    return list(links)

def save_content(url, content, output_dir='downloads'):
    os.makedirs(output_dir, exist_ok=True)
    filename = urlparse(url).netloc.replace('.', '_') + '_' + str(abs(hash(url))) + '.html'
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved: {url} -> {filepath}")

def process_url(url):
    html = download_page(url)
    if html:
        save_content(url, html)
    return url

def main(start_url, max_workers=5):
    print(f"Starting with URL: {start_url}")
    main_html = download_page(start_url)
    if not main_html:
        return

    save_content(start_url, main_html)

    links = parse_links(main_html, start_url)
    print(f"Found {len(links)} links.")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(process_url, url): url for url in links}

        for future in as_completed(future_to_url):
            result_url = future_to_url[future]
            try:
                future.result()
            except Exception as e:
                print(f"Error in {result_url}: {e}")

if __name__ == "__main__":
    target_url = "https://docs.python.org/3/library/os.path.html"  
    main(target_url)

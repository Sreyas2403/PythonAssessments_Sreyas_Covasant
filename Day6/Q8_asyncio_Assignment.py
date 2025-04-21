import asyncio
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests

def save_content(url, content, output_dir='downloads'):
    os.makedirs(output_dir, exist_ok=True)
    filename = urlparse(url).netloc.replace('.', '_') + '_' + str(abs(hash(url))) + '.html'
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved: {url} -> {filepath}")

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
        full_url = urljoin(base_url, tag['href'])
        if urlparse(full_url).scheme in ['http', 'https']:
            links.add(full_url)
    return list(links)

async def async_download_and_save(url):
    html = await asyncio.to_thread(download_page, url)
    if html:
        await asyncio.to_thread(save_content, url, html)

async def main(start_url):
    print(f"Starting with: {start_url}")

    main_html = await asyncio.to_thread(download_page, start_url)
    if not main_html:
        return

    await asyncio.to_thread(save_content, start_url, main_html)
    links = await asyncio.to_thread(parse_links, main_html, start_url)

    print(f"Found {len(links)} links")

    tasks = [async_download_and_save(link) for link in links]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_url = "https://docs.python.org/3/library/os.path.html" 
    asyncio.run(main(start_url))

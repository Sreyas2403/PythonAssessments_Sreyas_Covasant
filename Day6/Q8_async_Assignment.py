import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag
import sys

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            content = await response.read()
            return content, str(response.url)
    except Exception as e:
        print(f"Error downloading in {url}")
        return None, None

def extract_links(base_url, content):
    soup = BeautifulSoup(content, 'html.parser')
    links = set()
    
    for tag in soup.find_all(['a', 'link', 'script', 'img'], href=True):
        href = tag['href']
        absolute_url = urljoin(base_url, href)
        absolute_url, _ = urldefrag(absolute_url)
        parsed = urlparse(absolute_url)
        
        if parsed.scheme in ('http', 'https') and parsed.netloc:
            links.add(absolute_url)
    
    return links

async def main(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    async with aiohttp.ClientSession(headers=headers) as session:
        # Fetch initial URL
        content, final_url = await fetch(session, url)
        if not content:
            print("Failed to download initial URL")
            return
        
        base_url = final_url or url
        print(f"Base URL: {base_url}")
        
        links = extract_links(base_url, content)
        print(f"Found {len(links)} unique links to download")
        
        tasks = [fetch(session, link) for link in links]
        
        for future in asyncio.as_completed(tasks):
            content, url = await future
            if content:
                print(f"Downloaded: {url} ({len(content)} bytes)")
            else:
                print(f"Failed: {url}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python async_link_downloader.py <URL>")
        sys.exit(1)
    
    asyncio.run(main(sys.argv[1]))
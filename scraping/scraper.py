import os
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import mimetypes
import json
from datetime import datetime, timezone

class Scraper:
    def __init__(self, base_url, output_dir, max_depth=2, filter_keyword=None):
        self.base_url = base_url
        self.output_dir = output_dir
        self.max_depth = max_depth
        self.filter_keyword = filter_keyword
        self.visited_urls = set()
        self.target_extensions = {
            '.txt', '.pptx', '.xlsx', '.doc', '.docx', '.pdf'
        }

        # メタデータ収集用
        self.scrape_start_time = datetime.now(timezone.utc).astimezone()
        self.files_metadata = {}

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def is_valid_url(self, url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def get_extension(self, url):
        path = urlparse(url).path
        ext = os.path.splitext(path)[1].lower()
        return ext

    def download_file(self, url, page_url=None, page_title=None, link_text=None, crawl_depth=0):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, stream=True, timeout=10, headers=headers)
            response.raise_for_status()

            ext = self.get_extension(url)
            content_type = response.headers.get('content-type', '')
            if not ext:
                # Try to guess from content-type if no extension in URL
                ext = mimetypes.guess_extension(content_type)

            if ext not in self.target_extensions:
                return

            original_filename = os.path.basename(urlparse(url).path)
            if not original_filename:
                original_filename = "downloaded_file" + ext

            # Ensure unique filename
            filename = original_filename
            filepath = os.path.join(self.output_dir, filename)
            counter = 1
            while os.path.exists(filepath):
                name, file_ext = os.path.splitext(original_filename)
                filename = f"{name}_{counter}{file_ext}"
                filepath = os.path.join(self.output_dir, filename)
                counter += 1

            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            # ファイルサイズ取得
            file_size = os.path.getsize(filepath)

            # Last-Modifiedヘッダー取得
            last_modified = response.headers.get('Last-Modified')

            # メタデータ記録
            self.files_metadata[filename] = {
                "source_url": url,
                "page_url": page_url,
                "page_title": page_title,
                "link_text": link_text,
                "original_filename": original_filename,
                "downloaded_at": datetime.now(timezone.utc).astimezone().isoformat(),
                "file_size": file_size,
                "content_type": content_type,
                "last_modified": last_modified,
                "crawl_depth": crawl_depth
            }

            print(f"Downloaded: {url} -> {filepath}")

        except Exception as e:
            print(f"Failed to download {url}: {e}")

    def crawl(self, url, current_depth):
        if current_depth > self.max_depth:
            return

        if url in self.visited_urls:
            return

        # Check filter
        if self.filter_keyword and self.filter_keyword not in url:
            # Allow the starting URL even if it doesn't match, or maybe strict?
            # Usually strict is better if user asked for it.
            # But if base_url doesn't match, nothing happens.
            # Let's assume base_url is always allowed to start crawling.
            if url != self.base_url:
                return

        print(f"Crawling: {url} (Depth: {current_depth})")
        self.visited_urls.add(url)

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, timeout=10, headers=headers)
            response.raise_for_status()

            # Check if it's a file we want to download directly
            ext = self.get_extension(url)
            if ext in self.target_extensions:
                self.download_file(url, crawl_depth=current_depth)
                return  # Don't parse files as HTML

            # If it's HTML, parse for links
            content_type = response.headers.get('content-type', '')
            if 'text/html' not in content_type:
                return

            soup = BeautifulSoup(response.text, 'html.parser')

            # ページタイトルを取得
            page_title = None
            title_tag = soup.find('title')
            if title_tag:
                page_title = title_tag.get_text(strip=True)

            for link in soup.find_all('a', href=True):
                href = link['href']
                absolute_url = urljoin(url, href)

                if not self.is_valid_url(absolute_url):
                    continue

                # リンクテキストを取得
                link_text = link.get_text(strip=True)

                # Check if the link is a file to download
                link_ext = self.get_extension(absolute_url)
                if link_ext in self.target_extensions:
                    # Download files regardless of filter
                    self.download_file(
                        absolute_url,
                        page_url=url,
                        page_title=page_title,
                        link_text=link_text,
                        crawl_depth=current_depth
                    )
                else:
                    # Only crawl pages if they match the filter
                    if self.filter_keyword and self.filter_keyword not in absolute_url:
                        continue
                    self.crawl(absolute_url, current_depth + 1)

        except Exception as e:
            print(f"Error processing {url}: {e}")

    def save_metadata(self):
        """メタデータをJSONファイルとして保存"""
        completed_at = datetime.now(timezone.utc).astimezone()

        metadata = {
            "scrape_info": {
                "base_url": self.base_url,
                "started_at": self.scrape_start_time.isoformat(),
                "completed_at": completed_at.isoformat(),
                "filter_keyword": self.filter_keyword,
                "max_depth": self.max_depth,
                "total_files": len(self.files_metadata)
            },
            "files": self.files_metadata
        }

        metadata_path = os.path.join(self.output_dir, "metadata.json")
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        print(f"Metadata saved: {metadata_path}")
        return metadata_path


def main():
    parser = argparse.ArgumentParser(description="Scrape files from a URL with depth 2.")
    parser.add_argument("url", help="The starting URL")
    parser.add_argument("--output_dir", default="downloads", help="Directory to save downloaded files")
    parser.add_argument("--filter", help="Only crawl/download URLs containing this string")
    
    args = parser.parse_args()

    scraper = Scraper(args.url, args.output_dir, max_depth=2, filter_keyword=args.filter)
    scraper.crawl(args.url, 0)
    scraper.save_metadata()


if __name__ == "__main__":
    main()

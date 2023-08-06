import csv
import os
import sys
from datetime import datetime
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup

from .utils import HEADERS, SaveFile


class CitiBusinessOnline:
    def __init__(self, url):
        if not url.startswith(("http://", "https://")):
            raise ValueError("Invalid URL: must start with 'http://' or 'https://'")
        self.url = url
        self.file_name = unquote(
            url.split("/")[-2] if url.endswith("/") else url.split("/")[-1]
        )

    def download(self, output_dir=None):
        """scrape data"""
        with requests.Session() as session:
            response = session.get(self.url, headers=HEADERS)

        if response.status_code != 200:
            print(f"Request: {requests}; status code:{response.status_code}")
            response.raise_for_status()
            sys.exit(1)

        soup = BeautifulSoup(response.text, "html.parser")

        lst_pages = [
            page.a["href"] for page in soup.find_all("div", class_="jeg_thumb")
        ]

        try:
            print("saving results to csv...")
            if output_dir is None:
                output_dir = os.getcwd()
                SaveFile.mkdir(output_dir)
            if not os.path.isdir(output_dir):
                raise ValueError(
                    f"Invalid output directory: {output_dir} is not a directory"
                )
            print(f"File will be saved to: {output_dir}")

            stamp = datetime.strftime(datetime.utcnow(), "%Y-%m-%d")
            with open(
                os.path.join(output_dir, self.file_name + f"_{stamp}.csv"),
                mode="w",
                newline="",
                encoding="utf-8",
            ) as csv_file:
                fieldnames = ["title", "content", "author", "published_date", "page_url"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

                for page_url in lst_pages:
                    with requests.Session() as session:
                        response_page = session.get(page_url, headers=HEADERS)
                        soup_page = BeautifulSoup(response_page.text, "html.parser")

                        title = soup_page.find("h1", class_="jeg_post_title")
                        title = title.text.strip() if title else ""

                        content = soup_page.find("div", class_="content-inner")
                        content = content.text.strip() if content else ""

                        published_date = soup_page.find("div", class_="jeg_meta_date")
                        published_date = published_date.text.strip() if published_date else ""

                        author = soup_page.find("div", class_="jeg_meta_author coauthor").find("a")
                        author = author.text.strip() if author else ""

                        writer.writerow(
                            {
                                "title": title,
                                "content": content,
                                "author": author,
                                "published_date": published_date,
                                "page_url": page_url,
                            }
                        )
                print("Writing data to file...")
        except Exception as err:
            print(f"error: {err}")

        print(f"All file(s) saved to: {output_dir} successfully!")
        print("Done!")

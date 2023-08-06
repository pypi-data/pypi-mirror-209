import csv
import os
import sys
from datetime import datetime
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup

from .utils import HEADERS, SaveFile


class Yen:
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
        pages = soup.find_all(
            "a",
            {
                "class": [
                    "c-article-card-with-badges__headline",
                    "c-article-card__headline",
                    "c-article-card-main__headline",
                    "c-article-card-horizontal__headline",
                    "c-article-card-featured__headline",
                ]
            },
        )

        links = [page["href"] for page in pages]

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
                fieldnames = [
                    "title",
                    "content",
                    "published_date",
                    "author",
                    "page_url",
                ]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for link in links:
                    if link:
                        with requests.Session() as session:
                            response_page = session.get(link, headers=HEADERS)
                        soup_page = BeautifulSoup(response_page.text, "html.parser")

                        title = soup_page.find("h1", class_="c-main-headline")
                        title_main = title.text.strip()

                        content_main = ""
                        content_div = [
                            item
                            for item in soup_page.find(
                                "div", {"class": "post__content"}
                            ).select("ul li strong")
                        ]

                        for tag in content_div:
                            content_main = (
                                content_main + tag.get_text().strip() if tag else ""
                            )

                        meta_date = soup_page.find(
                            "div", {"class": "c-article-info post__info"}
                        )
                        published_date = meta_date.text.strip() if meta_date else ""

                        author = soup_page.find(
                            "a", {"class": "c-article-info__author"}
                        ).text.strip()

                        writer.writerow(
                            {
                                "title": title_main,
                                "content": content_main,
                                "published_date": published_date,
                                "author": author,
                                "page_url": link,
                            }
                        )
                print("Writing data to file...")
        except Exception as err:
            print(f"error: {err}")

        print(f"All file(s) saved to: {output_dir} successfully!")
        print("Done!")

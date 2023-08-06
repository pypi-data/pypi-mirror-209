import csv
import os
import sys
from datetime import datetime
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup

from .utils import HEADERS, SaveFile


class GhanaWeb:
    def __init__(self, url, home_page="https://www.ghanaweb.com"):
        if not url.startswith(("http://", "https://")):
            raise ValueError("Invalid URL: must start with 'http://' or 'https://'")
        self.url = url
        self.home_page = home_page
        self.file_name = unquote(
            url.split("/")[-2] if url.endswith("/") else url.split("/")[-1]
        )
        self.response = None
        self.soup = None

    def download(self, output_dir=None):
        """scrape data"""
        self.response = requests.request(
            "GET", self.url, headers=HEADERS
        )
        if self.response.status_code != 200:
            print(f"Request: {requests}; status code:{self.response.status_code}")
            self.response.raise_for_status()
            sys.exit(1)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        lst_pages = [
            a for a in self.soup.find("div", {"class": "afcon-news list"}).find_all("a")
        ]

        try:
            print("saving results to csv...")
            output_dir = output_dir or os.getcwd()
            SaveFile.mkdir(output_dir)
            if not os.path.isdir(output_dir):
                raise ValueError(
                    f"Invalid output directory: {output_dir} is not a directory"
                )
            print(f"File will be saved to: {output_dir}")

            stamp = datetime.strftime(datetime.utcnow(), "%Y-%m-%d")
            with open(
                    os.path.join(output_dir, self.file_name + f"_{stamp}.csv"), mode="w", newline=""
            ) as csv_file:
                fieldnames = ["title", "content", "author", "published_date", "page_url"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for page in lst_pages:
                    try:
                        page_url = self.home_page + page["href"]  # get("href", "")
                        if page_url:
                            with requests.Session() as session:
                                response_page = session.get(page_url, headers=HEADERS)
                            # response_page = requests.request("GET", page_url, headers=HEADERS)
                            soup_page = BeautifulSoup(response_page.text, "html.parser")
                            try:
                                title = soup_page.find("h1", {"style": "clear: both;"}).text.strip()
                                # title = title.text.strip if title else ""
                            except Exception:
                                title = ""
                            try:
                                content = soup_page.find("p", {"style": "clear:right"}).text.strip()
                                # content = content.text.strip() if content else ""
                            except Exception:
                                content = ""
                            try:
                                published_date = soup_page.find("p", class_="floatLeft").text.split(",")[-1]
                            except Exception:
                                published_date = ""
                            try:
                                author = soup_page.find("p", class_="floatRight").text.split(":")[-1].split(",")[-2]
                            except Exception:
                                author = ""

                            writer.writerow(
                                {
                                    "title": title,
                                    "content": content,
                                    "author": author,
                                    "published_date": published_date,
                                    "page_url": page_url,
                                }
                            )
                    except Exception:
                        continue
                print("Writing data to file...")
        except Exception as e:
            print(f"error: {e}")

        print(f"All file(s) saved to: {output_dir} successfully!")
        print("Done!")

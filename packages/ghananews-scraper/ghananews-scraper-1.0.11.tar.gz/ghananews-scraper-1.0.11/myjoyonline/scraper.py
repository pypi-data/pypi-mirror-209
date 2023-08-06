import csv
import os
import sys
from datetime import datetime
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup

from .utils import HEADERS, SaveFile


class MyJoyOnline:
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
            page
            for page in soup.find_all(
                ["li", "div"],
                {
                    "class": [
                        "mostrecent_btf",
                        "faded-bar",
                        "home-section-story-list tt-center",
                    ]
                },
            )
            + soup.find("ul", {"class": "home-latest-list"}).find_all("li")
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
                    encoding='utf-8'
            ) as csv_file:
                fieldnames = ["title", "content", "author", "published_date", "page_url"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for page in lst_pages:
                    page_url = page.find("a").attrs.get("href")
                    if page_url:
                        with requests.Session() as session:
                            response_page = session.get(page_url, headers=HEADERS)
                        soup_page = BeautifulSoup(response_page.text, "html.parser")

                        title = soup_page.find("div", {"class": "article-title"})
                        title = title.text.strip() if title else ""

                        content = soup_page.find("div", {"id": "article-text"})
                        content = content.text.strip() if content else ""

                        published_date = soup_page.find("div", class_="article-meta").find("div")
                        published_date = published_date.text.strip() if published_date else ""

                        author = soup_page.find("div", class_="article-meta").find("a")
                        author = author.text.strip().split(":")[-1] if author else ""

                        writer.writerow(
                            {"title": title,
                             "content": content,
                             "author": author,
                             "published_date": published_date,
                             "page_url": page_url
                             }
                        )
                print("Writing data to file...")
        except Exception as err:
            print(f"error: {err}")

        print(f"All file(s) saved to: {output_dir} successfully!")
        print("Done!")


# class MyJoyOnline:
#     def __init__(self, url):
#         self.url = url
#         self.file_name = url.split("/")[-2] if url.endswith("/") else url.split("/")[-1]
#
#     def download(self, output_dir=None):
#         """scrape data"""
#         response = requests.request('GET', self.url, headers=headers)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         lst_pages = soup.find_all('li', {'class': 'mostrecent_btf'}) \
#                     + soup.find_all('li', {'class': 'faded-bar'}) \
#                     + soup.find_all('div', {'class': 'home-section-story-list tt-center'}) \
#                     + soup.find('ul', {'class': 'home-latest-list'}).find_all('li')
#
#         try:
#             print("saving results to csv...")
#             if output_dir is None:
#                 output_dir = os.getcwd()
#                 SaveFile.mkdir(output_dir)
#             print(f"File will be saved to: {output_dir}")
#             with open(f"{output_dir}/{self.file_name}" + ".csv", mode='w', newline='') as csv_file:
#                 fieldnames = ['title', 'content', 'page_url']
#                 writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#                 print("Writing column names...")
#                 writer.writeheader()
#                 for page in lst_pages:
#                     try:
#                         page_url = page.find("a").attrs['href']
#                         response_page = requests.request('GET', page_url, headers=headers)
#                         soup_page = BeautifulSoup(response_page.text, 'html.parser')
#                         try:
#                             title = soup_page.find('div', {'class': 'article-title'}).text.strip()
#                         except Exception:
#                             title = ""
#                         try:
#                             content = soup_page.find('div', {'id': 'article-text'}).text.strip()
#                         except Exception:
#                             content = ""
#
#                         writer.writerow({'title': title, 'content': content, 'page_url': page_url})
#                     except Exception:
#                         continue
#                 print("Writing artitle titles...")
#                 print("Writing article content...")
#                 print("Writing data to file...")
#         except Exception as e:
#             print(f"error: {e}")
#
#         print(f"All file(s) saved to: {output_dir} successfully!")
#         print("Done!")

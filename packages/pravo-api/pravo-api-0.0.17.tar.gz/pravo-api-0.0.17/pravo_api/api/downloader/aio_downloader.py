import asyncio
import json
import os
import time
import urllib
from pathlib import Path
from random import uniform
from typing import List, Union

import inspect
import backoff
import aiohttp
from aiohttp import ClientSession
from aiohttp_retry import ExponentialRetry, RetryClient
from bs4 import BeautifulSoup
from pravo_api.api.downloader.meta_data_getter import MetaGetter
from pravo_api.api.utils.my_logger import get_struct_logger
from pravo_api.api.config import Configs


class FilesDownloader:
    """скачивает и сохраняет файлы по ссылке"""

    def __init__(
        self,
        result_folder: Path,
        links_to_load: List[str],
        failed_links_file: Union[Path, str],
        meta_data_file: Union[str, Path],
        format: str,
        config: Configs,
    ) -> None:
        """принимает ссылки на доки"""
        self.result_folder = Path(result_folder)
        self.filelogger = get_struct_logger(__name__, os.environ["pravo_api_log_file"])
        self.links = links_to_load
        self.downloaded = 0
        self.failed_links_file = failed_links_file
        if meta_data_file:
            self.meta_getter = MetaGetter(meta_data_file=meta_data_file)
        self.format = format
        self.config = config

    def _get_file_id(self, url) -> str:
        return urllib.parse.parse_qs(url).get("nd")[0]

    def save_document(self, file_name, doc_body: str, format):
        if format not in ["html", "txt"]:
            raise ValueError(f"допустимые форматы: txt, html")
        file_path = self.result_folder / (file_name + f".{format}")

        soup = BeautifulSoup(doc_body, "html.parser")

        if format == "html" and self.meta_getter:
            # вставялем метаданные
            doc_body = self.meta_getter.insert_meta_in_html(html=soup, doc_id=file_name)

        if format == "txt":
            raw_text = soup.get_text("|||", strip=True).split("|||")
            raw_text = [e.replace("\xa0", " ") for e in raw_text]
            doc_body = "\n".join(raw_text).replace("Complex", "")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(doc_body)
            self.downloaded += 1

    def _save_html_to_result_folder(self, file_name: str, html: str):
        file_path = self.result_folder / file_name
        with open(file_path, "w", encoding="cp1251") as f:
            f.write(html)
            self.downloaded += 1

    def _save_failed_links(self, failed_links: List[str]):
        with open(self.failed_links_file, "w", encoding="utf-8") as f:
            json.dump(failed_links, f, ensure_ascii=False)

    def _handle_failed_load(loading_info):
        link = loading_info["args"][0]
        print("_handle_failed_load ---", link)

    aiohttp_exceptions = tuple(
        obj
        for name, obj in inspect.getmembers(aiohttp.client_exceptions)
        if inspect.isclass(obj) and issubclass(obj, Exception)
    )

    def eat_exception(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                pass

        return wrapper

    @eat_exception  # do not raise when backoff gives up
    @backoff.on_exception(
        backoff.expo,
        aiohttp_exceptions,
        on_giveup=_handle_failed_load,
        max_tries=4,
        max_time=30,
    )
    async def download_file(self, link: str) -> None:
        file_name = self._get_file_id(link)
        self.filelogger.bind(filename=file_name)

        async with ClientSession() as client:
            async with client.get(link) as response:
                time.sleep(uniform(0.2, 0.6))
                if response.status != 200:
                    self.filelogger.error(event=f"{response.content.decode()}")
                else:
                    html = await response.text()
                    self.save_document(
                        file_name=file_name, doc_body=html, format=self.format
                    )
                    self.filelogger.debug(event=f"Соханили файл {file_name}")
                    return f"{file_name} -- OK"

    def _get_tasks(self):
        for link in self.links:
            yield self.download_file(link)

    async def gather_tasks(self):
        tasks = self._get_tasks()
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        return responses

    def go(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.gather_tasks())

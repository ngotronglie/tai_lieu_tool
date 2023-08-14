#deobfuscator by HuyAnh
#Zalo:0905491417
#huyanhnong.21
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import re
import os,sys
from pathlib import Path
from random import shuffle
from shutil import rmtree
from time import perf_counter
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from typing import Callable, Dict, Iterable, List, Optional, Set, Tuple, Union

from aiohttp import ClientSession
from aiohttp_socks import ProxyConnector
from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeRemainingColumn,
)
from rich.table import Table

#import config
def clear():
	if os.name=='nt':os.system('cls')
	else:os.system('clear')
clear()
def banner():
 banner = Colorate.Diagonal(Colors.green_to_white, f"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║ ██╗  ██╗██╗  ██╗ █████╗  ████████╗ ██████╗  ██████╗ ██╗      ║
║ ██║ ██╔╝██║  ██║██╔══██╗ ╚══██╔══╝██╔═══██╗██╔═══██╗██║      ║
║ █████╔╝ ███████║███████║    ██║   ██║   ██║██║   ██║██║      ║
║ ██╔═██╗ ██╔══██║██╔══██║    ██║   ██║   ██║██║   ██║██║      ║
║ ██║  ██╗██║  ██║██║  ██║    ██║   ╚██████╔╝╚██████╔╝███████╗ ║
║ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ ║
║══════════════════════════════════════════════════════════════║
║    Youtube -> Le Kha                                         ║
║    Telegram -> @lechaukhasupport                             ║
║    Zalo Support -> 0912119945                                ║
║    Facebook Support -> www.facebook.com/lechaukha.suppot     ║
║══════════════════════════════════════════════════════════════║
║      Mọi Hướng Dẫn Bạn Cần Đều Nằm Ở Trên Kênh Youtube       ║
║        Le Kha, Vui Lòng Xem Kỹ Hướng Dẫn Và Sử Dụng.         ║
╚══════════════════════════════════════════════════════════════╝
 ---------------TOOL GEN/CHECK-LIVE-DIE----------------
════════════════════════════════════════════════════════════════
PROXIES NÀY VẪN SỬ DỤNG ĐƯỢC CHO TOOL VALID SỐ 9 NGOÀI MENU NHÉ
TUY NHIÊN ĐÂY LÀ PROXIES 1 IP KHÔNG PHẢI XOAY VÌ THẾ SẼ BỊ BLOCK
IP VÀ CŨNG CÓ THẾ LỌC CHẬM HƠN PROXIES XOAY NHÉ....
════════════════════════════════════════════════════════════════
════════════════════════════════════════════════════════════════""")
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
banner()
class Proxy:
    def __init__(self, socket_address: str, ip: str) -> None:
        self.socket_address = socket_address
        self.ip = ip
        self.is_anonymous: Optional[bool] = None
        self.geolocation: str = "None"
        self.timeout = float("inf")

    def update(self, info: Dict[str, str]) -> None:
        country = info.get("country") or None
        region = info.get("regionName") or None
        city = info.get("city") or None
        self.geolocation = f" -> {country} | {region} | {city}"
        self.is_anonymous = self.ip != info.get("query")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Proxy):
            return NotImplemented
        return self.socket_address == other.socket_address

    def __hash__(self) -> int:
        return hash(("socket_address", self.socket_address))


class Folder:
    def __init__(self, folder_name: str, path: Path) -> None:
        self.folder_name = folder_name
        self.path = path / folder_name
        self.for_anonymous = "anon" in folder_name
        self.for_geolocation = "geo" in folder_name

    def remove(self) -> None:
        try:
            rmtree(self.path)
        except FileNotFoundError:
            pass

    def create(self) -> None:
        self.path.mkdir(parents=True, exist_ok=True)


class ProxyScraperChecker:

    def __init__(
        self,
        *,
        timeout: float,
        max_connections: int,
        sort_by_speed: bool,
        save_path: str,
        proxies: bool,
        proxies_Ẩn_Danh: bool,
        proxies_Định_Vị: bool,
        proxies_Định_Vị_Ẩn_Danh: bool,
        http_sources: Optional[Iterable[str]],
        console: Optional[Console] = None,
    ) -> None:
        self.path = Path(save_path)
        folders_mapping = {
            "proxies": proxies,
            "proxies_Ẩn_Danh": proxies_Ẩn_Danh,
            "proxies_Định_Vị": proxies_Định_Vị,
            "proxies_Định_Vị_Ẩn_Danh": proxies_Định_Vị_Ẩn_Danh,
        }
        self.all_folders = [
            Folder(folder_name, self.path) for folder_name in folders_mapping
        ]
        self.enabled_folders = [
            folder
            for folder in self.all_folders
            if folders_mapping[folder.folder_name]
        ]
        if not self.enabled_folders:
            raise ValueError("Tất Cả Các Thư Mục Bị Khoá")

        regex = r"(?:^|\D)(({0}\.{1}\.{1}\.{1}):{2})(?:\D|$)".format(
            r"(?:[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])",  # 1-255
            r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])",  # 0-255
            r"(?:\d|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}"
            + r"|65[0-4]\d{2}|655[0-2]\d|6553[0-5])",  # 0-65535
        )
        self.regex = re.compile(regex)

        self.sort_by_speed = sort_by_speed
        self.timeout = timeout
        self.sources = {
            proto: (sources,)
            if isinstance(sources, str)
            else frozenset(sources)
            for proto, sources in (
                ("http", http_sources),
            )
            if sources
        }
        self.proxies: Dict[str, Set[Proxy]] = {
            proto: set() for proto in self.sources
        }
        self.proxies_count = {proto: 0 for proto in self.sources}
        self.c = console or Console()
        self.sem = asyncio.Semaphore(max_connections)

    async def fetch_source(
        self,
        session: ClientSession,
        source: str,
        proto: str,
        progress: Progress,
        task: TaskID,
    ) -> None:
        try:
            async with session.get(source.strip(), timeout=15) as r:
                text = await r.text(encoding="utf-8")
        except Exception as e:
            self.c.print(f"{source}: {e}")
        else:
            for proxy in self.regex.finditer(text):
                self.proxies[proto].add(Proxy(proxy.group(1), proxy.group(2)))
        progress.update(task, advance=1)

    async def check_proxy(
        self, proxy: Proxy, proto: str, progress: Progress, task: TaskID
    ) -> None:
        try:
            async with self.sem:
                start = perf_counter()
                async with ClientSession(
                    connector=ProxyConnector.from_url(
                        f"{proto}://{proxy.socket_address}"
                    )
                ) as session:
                    async with session.get(
                        "http://ip-api.com/json/", timeout=self.timeout
                    ) as r:
                        res = (
                            None
                            if r.status in {403, 404, 429}
                            else await r.json()
                        )
        except Exception as e:
            # Too many open files
            if isinstance(e, OSError) and e.errno == 24:
                self.c.print(
                    "[red]Vui Lòng Đặt MAX_CONNECTIONS Thành Giá Trị Thấp Hơn"
                )

            self.proxies[proto].remove(proxy)
        else:
            proxy.timeout = perf_counter() - start
            if res:
                proxy.update(res)
        progress.update(task, advance=1)

    async def fetch_all_sources(self) -> None:
        with self._progress as progress:
            tasks = {
                proto: progress.add_task(
                    f"Gen Proxies: {proto.upper()}",
                    total=len(sources),
                )
                for proto, sources in self.sources.items()
            }
            async with ClientSession() as session:
                coroutines = (
                    self.fetch_source(
                        session, source, proto, progress, tasks[proto]
                    )
                    for proto, sources in self.sources.items()
                    for source in sources
                )
                await asyncio.gather(*coroutines)

        for proto, proxies in self.proxies.items():
            self.proxies_count[proto] = len(proxies)

    async def check_all_proxies(self) -> None:
        with self._progress as progress:
            tasks = {
                proto: progress.add_task(
                    f"Check Live/Die: {proto.upper()}",
                    total=len(proxies),
                )
                for proto, proxies in self.proxies.items()
            }
            coroutines = [
                self.check_proxy(proxy, proto, progress, tasks[proto])
                for proto, proxies in self.proxies.items()
                for proxy in proxies
            ]
            shuffle(coroutines)
            await asyncio.gather(*coroutines)

    def save_proxies(self) -> None:
        sorted_proxies = self.sorted_proxies.items()
        for folder in self.all_folders:
            folder.remove()
        for folder in self.enabled_folders:
            folder.create()
            for proto, proxies in sorted_proxies:
                text = "\n".join(
                    "{}{}".format(
                        proxy.socket_address,
                        proxy.geolocation if folder.for_geolocation else "",
                    )
                    for proxy in proxies
                    if (proxy.is_anonymous if folder.for_anonymous else True)
                )
                (folder.path / f"{proto}.txt").write_text(
                    text, encoding="utf-8"
                )

    async def main(self) -> None:
        await self.fetch_all_sources()
        await self.check_all_proxies()

        table = Table()
        table.add_column("Định Dạng")
        table.add_column("Proxies Sống")
        table.add_column("Tổng Cộng")
        for proto, proxies in self.proxies.items():
            working = len(proxies)
            total = self.proxies_count[proto]
            percentage = working / total * 100 if total else 0
            table.add_row(
                proto.upper(), f"{working} ({percentage:.1f}%)", str(total)
            )
        self.c.print(table)

        self.save_proxies()
        self.c.print(f"Tất Cả File Và Thư Mục Đã Lưu Vào Đường Dẫn \n{self.path.absolute()}\nCảm Ơn Bạn Đã Sử Dụng Proxies Của Mình...")

    @property
    def sorted_proxies(self) -> Dict[str, List[Proxy]]:
        key = self._sorting_key
        return {
            proto: sorted(proxies, key=key)
            for proto, proxies in self.proxies.items()
        }

    @property
    def _sorting_key(
        self,
    ) -> Union[Callable[[Proxy], float], Callable[[Proxy], Tuple[int, ...]]]:
        if self.sort_by_speed:
            return lambda proxy: proxy.timeout
        return lambda proxy: tuple(
            map(int, proxy.socket_address.replace(":", ".").split("."))
        )

    @property
    def _progress(self) -> Progress:
        return Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:3.0f}%"),
            TextColumn("[{task.completed}/{task.total}]"),
            TimeRemainingColumn(),
            console=self.c,
        )


async def main() -> None:
    await ProxyScraperChecker(
        timeout=5,
        max_connections=900,
        sort_by_speed=True,
        save_path="",
        proxies=True,
        proxies_Ẩn_Danh=True,
        proxies_Định_Vị=True,
        proxies_Định_Vị_Ẩn_Danh=True,
        http_sources= (
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
            "https://openproxy.space/list/http",
            "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http%2Bhttps.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
            "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/UserR3X/proxy-list/main/http%2Bs.txt",
            "https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://www.proxy-list.download/api/v1/get?type=https",
            "https://www.proxyscan.io/download?type=http",
            "https://www.proxyscan.io/download?type=https",
)
        if True and (
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
    "https://openproxy.space/list/http",
    "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http%2Bhttps.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/UserR3X/proxy-list/main/http%2Bs.txt",
    "https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
    "https://www.proxyscan.io/download?type=http",
    "https://www.proxyscan.io/download?type=https",
)
        else None,
    ).main()


if __name__ == "__main__":
    asyncio.run(main())

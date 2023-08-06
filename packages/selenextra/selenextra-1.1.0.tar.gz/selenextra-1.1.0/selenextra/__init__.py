from urllib.parse import urlparse

try:
    from undetected_chromedriver import ChromeOptions
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        'undetected_chromedriver not found. ' 'Install it with `pip install git+https://github.com/nguyenvantat1182002/undetected-chromedriver@master`.'
    ) from e
    
from seleniumwire.undetected_chromedriver import Chrome
from selenium.common.exceptions import TimeoutException
from seleniumwire.request import Request, Response
from typing import Union, Callable, Any, List, Tuple
from .exceptions import *

import json
import re
import random as rnd
import time


class ChromeDriver(Chrome):
    CONNECTION_TIMEOUT = 30

    def __init__(self, **kwargs) -> None:
        kwargs['seleniumwire_options'] = kwargs.get('seleniumwire_options', {})
        kwargs['seleniumwire_options']['mitm_http2'] = False

        super().__init__(**kwargs)

    def get_user_agent(self) -> str:
        return self.execute_script('return navigator.userAgent')

    def get_cookie_string(self) -> str:
        cookies = self.get_cookies()
        cookies = [f'{item["name"]}={item["value"]}' for item in cookies]

        return '; '.join(cookies) + ';'
    
    def get_browser_ip(self) -> str:
        url = 'https://httpbin.org/ip'

        try:
            self.get(url)
            
            request = self.wait_for_request('/ip')
            body = request.response.body.decode('utf-8')
            data = json.loads(body)
            ip = data['origin']
        except:
            raise UnableToFetchIP
        
        return ip

    def callback_with_timeout(self, callback: Callable[[Tuple], Any], params: tuple, timeout: Union[int, float] = 30) -> Any:
        end_time = time.time() + timeout

        while time.time() < end_time:
            result = callback(*params)

            if not result:
                continue

            return result

        raise TimeoutException(f'Callback execution timed out: {callback.__name__}')

    def _process_requests(self, callback: Callable[[Request, Response], Any]) -> Any:
        for request in self.requests:
            if not request.response:
                continue

            response = request.response
            result = callback(request, response)

            if not result:
                continue

            return result

    def process_requests(self, callback: Callable[[Request, Response], Any], timeout: Union[int, float] = 30) -> Any:
        return self.callback_with_timeout(self._process_requests, (callback,), timeout)

    def sleep_random_time(self, a: Union[int, float], b: Union[int, float]) -> None:
        time.sleep(round(rnd.uniform(a, b), 1))

    def add_cookie_string(self, cookie_string: str) -> None:
        cookie_regex = re.compile(r"([^=]+)=([^;]+)?;")
        cookies = cookie_regex.findall(cookie_string)

        for cookie in cookies:
            name, value = cookie
            name = name.strip()
            value = value.strip()

            self.add_cookie({'name': name, 'value': value})

        self.sleep_random_time(1, 2.5)
        self.refresh()

    def _find_first_matching_request(self, paths: List[Tuple[str, Callable[[Request], Any]]]) -> Any:
        for item in paths:
            path, callback = item

            request = self.backend.storage.find(path)
            if request is None:
                time.sleep(1/5)
                continue

            return callback(request) if callback else request

    def find_first_matching_request(self, paths: List[Tuple[str, Callable[[Request], Any]]], timeout: Union[int, float] = 30) -> Any:
        return self.callback_with_timeout(self._find_first_matching_request, (paths, ), timeout)

    def add_proxy(self, proxy: str) -> None:
        scheme = urlparse(proxy).scheme
        http_proxy = f'{proxy.replace("https", "http") if scheme == "https" else proxy}'

        self.proxy = {
            'http': http_proxy,
            'https': proxy,
            'no_proxy': 'localhost,127.0.0.1'
        }

    def quit(self) -> None:
        super().quit()
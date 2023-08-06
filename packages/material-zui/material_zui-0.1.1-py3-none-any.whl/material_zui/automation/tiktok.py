from bs4 import BeautifulSoup, ResultSet
import requests

from material_zui.array import is_not_last_index
from material_zui.file import download
from material_zui.selenium import Zui_Selenium_Chrome


class Zui_Tiktok(Zui_Selenium_Chrome):
    '''
    Base on repo: https://github.com/codewithvincent1/tiktokVideoScraper
    '''

    def set_browser_info(self, cookies: dict[str, str] = {}, headers: dict[str, str] = {}) -> None:
        '''
        1. Access https://ssstik.io to get `cUrl` request
        2. Access https://curlconverter.com to convert that `cUrl` to `Python request`, then only need to use `cookies` and `headers`
        '''
        self.cookies: dict[str, str] = cookies
        self.headers: dict[str, str] = headers

    def get_video_urls_from_channel(self, channel_url: str, limit: int = 0, start_index: int = 0) -> list[str]:
        '''
        Get all video url of channel
        @limit: number of url to get
        @start_index: position index to start, default from `0`
        '''
        videos: ResultSet
        i = 1
        end_index = start_index+limit

        print("Open channel", channel_url)
        self.driver.get(channel_url)

        print("Geting video url")
        self.delay()
        screen_height = self.driver.execute_script(
            "return window.screen.height;")
        if end_index != 0:  # incase exist limit param
            while True:
                soup = BeautifulSoup(self.driver.page_source, "html.parser")
                videos = soup.find_all(
                    "div", {"class": "tiktok-yz6ijl-DivWrapper"})
                scroll_height = self.driver.execute_script(
                    "return document.body.scrollHeight;")
                if (screen_height) * i > scroll_height or len(videos) >= end_index:
                    break
                self.driver.execute_script(
                    "window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
                i += 1
                self.delay()
        else:  # get all channel video url
            while True:
                self.driver.execute_script(
                    "window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
                i += 1
                self.delay()
                scroll_height = self.driver.execute_script(
                    "return document.body.scrollHeight;")
                if (screen_height) * i > scroll_height:
                    break

            self.delay()
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            videos = soup.find_all(
                "div", {"class": "tiktok-yz6ijl-DivWrapper"})

        urls = list(map(lambda video: video.a["href"], videos))
        return urls[start_index:end_index] if end_index != 0 else urls

    def download_video(self, url: str, output_directory_path: str) -> None:
        '''
        Use https://ssstik.io to download tiktok video
        '''
        params = {'url': 'dl'}
        data = {
            'id': url,
            'locale': 'en',
            'tt': '',  # NOTE: This value gets changed, please use the value that you get when you copy the curl command from the network console
        }

        print(f"Getting the download link: {url}")
        response = requests.post('https://ssstik.io/abc', params=params,
                                 cookies=self.cookies, headers=self.headers, data=data)
        downloadSoup = BeautifulSoup(response.text, "html.parser")
        downloadLink: str = downloadSoup.a["href"]  # type: ignore
        videoTitle: str = downloadSoup.p.getText().strip()  # type: ignore

        print("Saving the video")
        self.delay()
        download(downloadLink,
                 f"{output_directory_path}/{videoTitle}.mp4")

    def download_videos(self, urls: list[str], output_directory_path: str) -> None:
        '''
        Download video by list url
        @urls: list video url to download
        @output_directory_path: path to save all video downloaded
        '''
        print(f"Downloading {len(urls)} videos")
        for index, url in enumerate(urls):
            self.download_video(
                url=url, output_directory_path=output_directory_path)
            if is_not_last_index(urls, index):
                self.delay(5)

    def download_channel_videos(self, channel_url: str, output_directory_path: str, limit: int = 0, start_index: int = 0) -> None:
        '''
        Use to download all channel video
        @output_directory_path: path to save all video downloaded
        @limit: number of url to get
        @start_index: position index to start, default from `0`
        '''
        urls: list[str] = self.get_video_urls_from_channel(
            channel_url=channel_url, limit=limit, start_index=start_index)
        self.download_videos(urls, output_directory_path)
        # print(f"Downloading {len(urls)} videos")
        # for index, url in enumerate(urls):
        #     self.download_video(
        #         url=url, output_directory_path=output_directory_path)
        #     if is_not_last_index(urls, index):
        #         self.delay(5)

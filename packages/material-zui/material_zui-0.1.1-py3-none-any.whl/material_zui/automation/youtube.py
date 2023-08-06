import os
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from datetime import datetime

from material_zui.automation.type import Video, Videos
from material_zui.automation.Constant import Constant
from material_zui.file import load_json_array
from material_zui.selenium import safe_find_element, Zui_Selenium_Chrome
from material_zui.array import is_not_last_index


class Zui_Youtube(Zui_Selenium_Chrome):
    '''
    - Automation base on the system UI, so it can be out updated in the future due to the update UI
    - Tested on `Ubuntu` platform, it might work on `Linux` (or `MacOS`), not sure for `Window`
    '''

    def get_account_info(self) -> str:
        '''
        Example result:
        ```txt
        Google Account: {Account name}
        ({username}@gmail.com)
        ```
        '''
        self.driver.get("https://google.com")
        account_element = self.driver.find_element(By.CLASS_NAME, "gb_3a")
        return account_element.get_attribute("aria-label")

    def upload_video(self, video: Video) -> None:
        '''
        Upload single video to YouTube
        @is_publish: direct publish
        @schedule: format `MM/DD/YYYY, HH:MM`
        '''
        title = video['title']
        description = video['description']
        path = video['path']
        is_publish = video['is_publish']
        playlist = video.get('playlist')
        tags = video.get('tags')
        schedule = video.get('schedule')

        print('Access youtube studio')
        self.driver.get("https://studio.youtube.com")

        # click upload
        self.delay()
        upload_button = self.driver.find_element(
            By.XPATH, '//*[@id="upload-icon"]')
        upload_button.click()

        # import video
        print('Importing video')
        self.delay()
        file_input = self.driver.find_element(
            By.XPATH, '//*[@id="content"]/input')
        abs_path = os.path.abspath(str(path))
        file_input.send_keys(abs_path)

        # set title
        print('Setting title')
        sleep(7)
        title_element = self.driver.find_element(
            By.XPATH, '//*[@id="textbox"]')
        title_element.send_keys(Keys.CONTROL + 'a')
        title_element.send_keys(Keys.BACKSPACE)
        title_element.send_keys(title)

        # set description
        print('Setting description')
        self.delay()
        description_element = self.driver.find_element(
            By.XPATH, '//*/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div')
        description_element.send_keys(description)

        # set playlist
        self.delay()
        if playlist:
            print('Setting playlist')
            # open playlist
            self.driver.find_element(
                By.CLASS_NAME, Constant.PL_DROPDOWN_CLASS).click()

            # load playlist
            sleep(5)
            playlist_items_container = self.driver.find_element(
                By.ID, Constant.PL_ITEMS_CONTAINER_ID)
            playlist_item = self.find_element(
                By.XPATH, Constant.PL_ITEM_CONTAINER.format(playlist), playlist_items_container)
            sleep(Constant.USER_WAITING_TIME)
            if playlist_item:
                # choose playlist existed
                playlist_item.click()
            else:
                # new playlist
                self.driver.find_element(
                    By.XPATH, '//*[@id="dialog"]/div[2]/div/ytcp-button').click()
                self.delay()
                self.driver.find_element(
                    By.XPATH, '//*/tp-yt-paper-listbox/tp-yt-paper-item[1]').click()

                # edit playlist title
                self.delay()
                self.driver.find_element(
                    By.XPATH, "//*/ytcp-playlist-metadata-editor/div/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div").send_keys(playlist)

                # create new playlist
                sleep(Constant.USER_WAITING_TIME)
                self.driver.find_element(
                    By.XPATH, '//*[@id="create-button"]').click()

            # save playist
            sleep(Constant.USER_WAITING_TIME)
            done_button = self.driver.find_element(
                By.CLASS_NAME, Constant.PL_DONE_BUTTON_CLASS)
            done_button.click()

        # select kid option
        self.delay()
        self.driver.find_element(
            By.XPATH, '//*[@id="audience"]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]').click()

        # set tags
        if tags and len(tags):
            print('Setting tags')
            print(tags)

            # open advance option
            self.delay()
            self.driver.find_element(
                By.XPATH, '//*[@id="toggle-button"]/div').click()

            # click tags
            self.delay()
            tags_element = self.driver.find_element(
                By.XPATH, '//*/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[4]/ytcp-form-input-container/div[1]/div/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input')
            tags_element.click()

            # add tags
            for tag in tags:
                tags_element.send_keys(tag)
                tags_element.send_keys(Keys.ENTER)

        # click next 3 time
        self.delay()
        next_button = self.driver.find_element(
            By.XPATH, '//*[@id="next-button"]')
        for i in range(3):
            next_button.click()
            self.delay(1)

        # publish or schedule
        self.delay()
        if is_publish:  # click public to direct publish
            self.driver.find_element(
                By.XPATH, '//*[@id="privacy-radios"]/tp-yt-paper-radio-button[3]').click()
        elif schedule:  # schedule
            date_time = datetime.strptime(str(schedule), "%m/%d/%Y, %H:%M")
            self.driver.find_element(
                By.ID, Constant.SCHEDULE_CONTAINER_ID).click()
            self.driver.find_element(By.ID, Constant.SCHEDULE_DATE_ID).click()
            self.driver.find_element(
                By.XPATH, Constant.SCHEDULE_DATE_TEXTBOX).clear()
            self.driver.find_element(By.XPATH, Constant.SCHEDULE_DATE_TEXTBOX).send_keys(
                datetime.strftime(date_time, "%b %e, %Y"))
            self.driver.find_element(
                By.XPATH, Constant.SCHEDULE_DATE_TEXTBOX).send_keys(Keys.ENTER)
            self.driver.find_element(By.XPATH, Constant.SCHEDULE_TIME).click()
            self.driver.find_element(By.XPATH, Constant.SCHEDULE_TIME).clear()
            self.driver.find_element(By.XPATH, Constant.SCHEDULE_TIME).send_keys(
                datetime.strftime(date_time, "%H:%M"))
            self.driver.find_element(
                By.XPATH, Constant.SCHEDULE_TIME).send_keys(Keys.ENTER)

        # submit
        # 1. click done (for private video)
        # 2. click publish (for publish video)
        # 3. click schedule (for schedule video)
        print('Submit video')
        self.delay()
        self.driver.find_element(
            By.XPATH, '//*[@id="done-button"]').click()
        self.delay(10)

        video_processing_element = self.find_element(
            By.XPATH, '//*[@id="close-button"]/div')
        if video_processing_element:
            video_processing_element.click()

    def upload_videos(self, videos: Videos) -> None:
        '''
        Upload multiple videos to YouTube
        '''
        for index, video in enumerate(videos):
            self.upload_video(video)
            if is_not_last_index(videos, index):
                self.delay()

    def upload_videos_from_file_info(self, video_path: str, json_file_path: str) -> None:
        '''
        Upload multiple videos from json data file
        @video_path: video path including video to publish
        @json_file_path: json file path including video info
        '''
        def map_item(video: dict) -> Video:
            file_name = str(video['file_name'])
            path = f'{video_path}/{file_name}'
            return {
                'title': video['title'],
                'description': video['description'],
                'path': path,
                'playlist': video.get('playlist'),
                'tags': video.get('tags'),
                'is_publish': video.get('is_publish') or False,
                'schedule': video.get('schedule')
            }
        items = load_json_array(json_file_path)
        videos: Videos = list(map(map_item, items))
        self.upload_videos(videos)

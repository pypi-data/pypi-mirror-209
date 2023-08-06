from urllib.request import urlopen
from collections import defaultdict
import json
from typing import DefaultDict


def download(url: str, output_path: str):
    mp4File = urlopen(url)
    with open(output_path, "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break


def load_json_object(json_file_path: str) -> DefaultDict[str, str]:
    '''
    Load json file data to dict type
    @json_file_path: json file path
    @return: dict json data
    '''
    with open(json_file_path, encoding='utf-8') as json_data:
        return defaultdict(str, json.load(json_data))


def load_json_array(json_file_path: str) -> list:
    '''
    Load json file data to list type
    @json_file_path: json file path
    @return: list json data
    '''
    with open(json_file_path, "r") as f:
        data = json.load(f)
    return list(data)

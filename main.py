import os
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_upload_link(self, disk_file_path):
        headers = {"Authorization": f"OAuth {self.token}"}
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            headers=headers,
            params=params,
        )
        response.raise_for_status()
        return response.json()["href"]

    def upload(self, file_list: list):
         """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        for file_path in file_list:
            file_name = os.path.basename(file_path)
            upload_link = self.get_upload_link(file_name)
            with open(file_path, 'rb') as file:
                response = requests.put(upload_link, data=file)
                response.raise_for_status()


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Введите путь к файлу: ')
    token = input('Введите токен Яндекс.Диска: ')
    uploader = YaUploader(token)
    uploader.upload([path_to_file])

from abc import ABC, abstractmethod

class Scraper(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def scrape_data(self):
        pass

    def save_to_excel(self, df, file_name):
        df.to_excel(file_name, index=False)
        print(f"저장된 Excel 파일 경로: {file_name}")
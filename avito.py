from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pytesseract import image_to_string
from PIL import Image


class Bot:
    def __init__(self):
        options = Options()
        #options.headless = True
        self.driver = webdriver.Firefox(options=options)
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')

    def navigate(self):
        self.driver.get('https://www.avito.ru/sankt-peterburg/telefony/apple_iphone_se_2020_64gb_1934918193')
        # Один слеш - адресация от начала документа, два слеша - относительная
        button = self.driver.find_element_by_xpath('//button[@class="button-button-2Fo5k button-size-l-3LVJf button-success-1Tf-u width-width-12-2VZLz"]')
        button.click()
        image = button.screenshot_as_png
        with open('my_screenshot.gif', 'wb') as file:
            file.write(image)

            file.close()
        image = Image.open('my_screenshot.gif')
        print(image_to_string(image))



        # image = self.driver.




def main():
    b = Bot()


if __name__ == '__main__':
    main()

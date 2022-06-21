from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging


if __name__ == '__main__':
    logging.basicConfig(filename='test_1.log',
                        level=logging.INFO,
                        format='%(asctime)s %(message)s')
    logger = logging.getLogger('testing_task')
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(executable_path="chromedriver",
                              chrome_options=options)
    driver.set_window_size(1420, 900)

    logger.info("Test akceptacji cookies, wyszukania produktu na stronie ceneo.pl i uzycia sortowania")
    driver.get('https://www.ceneo.pl')
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, 'btn.btn-info.btn-origin.js_cookie-monster-agree.js_gtm_button').click()
    driver.switch_to.default_content()
    logger.info("Kliknieto 'Akceptuj cookies'")
    time.sleep(2)
    logger.info("Zakceptowano polityke cookies")
    driver.find_element(By.NAME, 'search-query').click()
    logger.info("Znaleziono wyszukiwarke")
    input_1 = driver.find_element(By.ID, 'form-head-search-q')
    input_1.send_keys("xbox")
    logger.info("Wpisano fraze do wyszukiwarki")
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'header-search__button__text').click()
    logger.info("Kliknieto 'Szukaj'")
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@title='Microsoft Xbox Series X']").click()
    logger.info("Znaleziono szukany element po atrybucie title")
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[5]/div[2]/div[1]/div/div/div[1]/a/b').click()
    logger.info("Kliknieto 'Sortuj od'")
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[5]/div[2]/div[1]/div/div/div[1]/div/a[3]').click()
    logger.info("Wybrano sortowanie wedlug 'najnizszej ceny z dostawa'")
    logger.info("Test zaliczony!")
    time.sleep(10)
    driver.quit()
    print("Done")

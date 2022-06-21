from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging


if __name__ == '__main__':
    logging.basicConfig(filename='test_2.log',
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

    logger.info("Test akceptacji cookies, wyszukania i dodania produktu do koszyka na stronie morele.net, oraz proby zalogowania do serwisu."
                "Oczekiwany wynik: znaleziony produkt zostanie dodany do koszyka i nie uda sie zalogowac podanymi danymi")
    driver.get('https://www.morele.net/')
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, 'btn.btn-secondary.btn-secondary-outline.btn-md.close-cookie-box').click()
    driver.switch_to.default_content()
    logger.info("Kliknieto 'Akceptuj cookies'")
    time.sleep(3)
    logger.info("Zaakceptowano polityke cookies")
    driver.find_element(By.NAME, 'search').click()
    logger.info("Znaleziono wyszukiwarke")
    input_1 = driver.find_element(By.CLASS_NAME, 'form-control.quick-search-autocomplete')
    input_1.send_keys("xbox")
    logger.info("Wpisano fraze do wyszukiwarki")
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'btn.btn-primary.h-quick-search-submit').click()
    logger.info("Kliknieto 'Szukaj'")
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[2]/div/div[6]/div[1]/div[2]/div/div[2]/div[1]/div/p/a").click()
    logger.info("Znaleziono szukany element")
    driver.find_element(By.XPATH, "/html/body/main/div/section/div[1]/div[7]/aside/div[1]/div[4]/div[3]/div[1]/a").click()
    logger.info("Kliknieto 'Dodaj do koszyka'")
    time.sleep(3)
    try:
        driver.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/div[3]/button').click()
        logger.info("Kliknieto 'Nie potrzebuje dodatkowej ochrony'")
        time.sleep(1)
    except:
        logger.warning("Nie znaleziono elementu")
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "btn.btn-primary.show-basket").click()
    logger.info("Kliknieto 'Zobacz koszyk'")
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "confirm-button.btn.btn-primary.btn-block").click()
    logger.info("Kliknieto 'Wybierz dostawe i platnosc'")
    username = driver.find_element(By.NAME, "_username")
    password = driver.find_element(By.NAME, "_password")
    username.send_keys("user1@mail.com")
    logger.info("Wpisano email")
    time.sleep(1)
    password.send_keys("password")
    logger.info("Wpisano haslo")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[2]/div/div[1]/div[1]/form/button").click()
    logger.info("Kliknieto 'Zaloguj sie'")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[2]")
    logger.info("Strona zwrocila komunikat o nieudanym logowaniu")
    logger.info("Test zaliczony!")
    time.sleep(10)
    driver.quit()
    print("Done")

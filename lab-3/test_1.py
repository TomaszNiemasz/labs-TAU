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

    logger.info("Test akceptacji cookies i stworzenia uzytownika")
    driver.get("https://www.morele.net/")
    time.sleep(4)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div/button').click()
    time.sleep(4)
    logger.info("Kliknieto 'Akceptuj cookies'")
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/div/div/div/div[2]/div/div[2]/div/div[4]/a').click()
    logger.info("Kliknieto 'Zaloz konto'")
    time.sleep(4)
    driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div[2]').click()
    logger.info("Rozpoczeto tworzenie uzytkownika")
    time.sleep(4)
    input_email = driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/div[1]/input')
    input_email.send_keys("pawelpawel335542@gmail.com")
    logger.info("Wpisano email")
    time.sleep(4)
    input_pass = driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/div[2]/input')
    input_pass.send_keys("!@fcb$#hggK29304")
    logger.info("Wpisano haslo")
    time.sleep(4)
    driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/div[3]/label/span[1]').click()
    time.sleep(3)
    logger.info("Zaakceptowano regulamin")
    driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/main/div/div/div[4]/form/button').click()
    logger.info("Kliknieto 'Utworz konto'")
    time.sleep(3)
    logger.info("Test zakonczony!")
    time.sleep(10)
    driver.quit()
    print("Done")

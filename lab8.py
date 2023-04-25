from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ukd.edu.ua/navchalni-plani"
driver.get(URL)

def print_spec(spec):
    print("Бакалаврат:")
    for index, elem in enumerate(spec[0]):
        print(f"{index}. {elem}")
    print("Магістратура:")
    for index, elem in enumerate(spec[1]):
        print(f"{index}. {elem}")
    print("Доктор філософії:")
    for index, elem in enumerate(spec[2]):
        print(f"{index}. {elem}")

def get_education_spec(driver):
    bachelor = list()
    master = list()
    doctor_ph = list()

    for ind in range(4,16):
        bachelor.append(driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/article/div/div[3]/div/div[2]/div/div/div/table/tbody/tr[{ind}]/td[1]").text)

    for ind in range(18,25):
        master.append(driver.find_element(By.XPATH, f"/html/body/div[1]/main/section/div/div/article/div/div[3]/div/div[2]/div/div/div/table/tbody/tr[{ind}]/td[1]").text)

    doctor_ph.append(driver.find_element(By.XPATH, "/html/body/div[1]/main/section/div/div/article/div/div[3]/div/div[2]/div/div/div/table/tbody/tr[27]/td[1]").text)

    print_spec((bachelor,master,doctor_ph))

    driver.close()

get_education_spec(driver)

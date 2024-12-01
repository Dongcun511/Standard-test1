# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


def search_and_process_results(keyword, driver):
    search_bar = driver.find_element(By.ID, "kw")
    search_bar.send_keys(keyword)

    search_button = driver.find_element(By.ID, "su")
    search_button.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "content_left")))

    second_page_url = driver.current_url + "&pn=10"
    driver.get(second_page_url)

    wait.until(EC.presence_of_element_located((By.ID, "content_left")))

    top_domain_count = {}

    search_results = driver.find_elements(By.CLASS_NAME, "t")

    for result in search_results:
        title = result.find_element(By.TAG_NAME, "a").text
        link = result.find_element(By.TAG_NAME, "a").get_attribute("href")
        print("标题:", title)
        print("链接:", link)

        domain = re.search(r'(?<=://)[^/]+', link).group(0)
        top_domain = domain.split('.')[-1] if '.' in domain else domain
        if top_domain in top_domain_count:
            top_domain_count[top_domain] += 1
        else:
            top_domain_count[top_domain] = 1

    print("顶级域名出现次数统计:")
    for domain, count in top_domain_count.items():
        print(domain, count)


if __name__ == "__main__":

    driver = webdriver.Chrome()

    driver.get("https://www.baidu.com")

    search_and_process_results("陈博", driver)

    search_and_process_results("Selenium", driver)

    driver.quit()
import requests as requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


CHROME_DRIVER_PATH = "/Users/parth_gpt/Development/chromedriver"
URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-gb",
}
response = requests.get(url=URL, headers=headers)
page = response.text

soup = BeautifulSoup(page, "lxml")

property_links_tags = soup.select(".list-card-top a")
property_links = []
for link in property_links_tags:
    href = link["href"]
    if "http" not in href:
        property_links.append(f"https://www.zillow.com{href}")
    else:
        property_links.append(href)

print(property_links)

price_tags = soup.find_all(name="div", class_="list-card-price")
prices = []
for price in price_tags:
    p = price.get_text()
    refined_p = p.split("/")[0]
    prices.append(refined_p)

print(prices)

address_tags = soup.select(".list-card-info a address")
addresses = []
for address in address_tags:
    a = address.get_text()
    addresses.append(a)

print(addresses)


driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeKR9GLilYvRmz1g2hV3q--dUm5D5F2BFK_qAmwK4qgLRhPWg/viewform?usp=sf_link")
sleep(2)

ques1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
ques2 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
ques3 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

for i in range(len(prices)):
    ques1.send_keys(addresses[i])
    sleep(1)
    ques2.send_keys(prices[i])
    sleep(1)
    ques3.send_keys(property_links[i])
    sleep(1)
    submit_button.click()
    sleep(1)
    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLSeKR9GLilYvRmz1g2hV3q--dUm5D5F2BFK_qAmwK4qgLRhPWg/viewform?usp=sf_link")
    sleep(2)
    ques1 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ques2 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    ques3 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

driver.quit()
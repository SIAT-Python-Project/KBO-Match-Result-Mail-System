import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get(url="https://www.koreabaseball.com/")
action = ActionChains(driver)


driver.find_element(By.CSS_SELECTOR,'.service-box li:nth-child(5)').click()     # 팀순위 페이지 이동



team_rank_list = driver.find_elements(By.CSS_SELECTOR, 'tData thead tr th')     # 목차
team_rank_one = driver.find_elements(By.CLASS_NAME, 'tData tbody tr td')        # 1등팀
team_rank_two = driver.find_elements(By.CLASS_NAME, 'tData tbody tr:nth-child(2) td')   # 2등팀
team_rank_three = driver.find_elements(By.CLASS_NAME, 'tData tbody tr:nth-child(3) td') # 3등팀
team_rank_four = driver.find_elements(By.CLASS_NAME, 'tData tbody tr:nth-child(4) td')  # 4등팀
team_rank_five = driver.find_elements(By.CLASS_NAME, 'tData tbody tr:nth-child(5) td')  # 5등팀
team_rank_six = driver.find_elements(By.CLASS_NAME, 'tData tbody tr:nth-child(6) td')   # 6등팀
team_rank_seven = driver.find_elements(By.CLASS_NAME, 'tData tbody tr:nth-child(7) td') # 7등팀
team_rank_eight = driver.find_elements(By.CLASS_NAME, 'tData tbody tr:nth-child(8) td') # 8등팀
team_rank_nine = driver.find_elements(By.CLASS_NAME, 'tData tbody tr:nth-child(9) td')  # 9등팀
team_rank_ten = driver.find_elements(By.CLASS_NAME, 'tData tbody tr:nth-child(10) td')  # 10등팀






time.sleep(5)

# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPruebaitla():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pruebaitla(self):
    self.driver.get("https://plataformavirtual.itla.edu.do/login/index.php")
    self.driver.set_window_size(1280, 680)
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("270764Yulian26@")
    self.driver.find_element(By.ID, "loginbtn").click()
    self.driver.find_element(By.ID, "drop-down-64d6e2c814afe64d6e2c6258f88").click()
    self.driver.find_element(By.LINK_TEXT, "Programación III (Presencial / Virtual) | 2023-C-2 | Kelyn Tejada Belliard").click()
    self.driver.execute_script("window.scrollTo(0,200)")
    element = self.driver.find_element(By.CSS_SELECTOR, ".fhs-tooltip")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-cogs").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-bar-chart").click()
    element = self.driver.find_element(By.LINK_TEXT, "Debate 1 calificación")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "h1")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "2023-C-2-1615-2880-TDS-007").click()
    self.driver.find_element(By.CSS_SELECTOR, ".list-group:nth-child(1) li:nth-child(2) .media-body").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "h1")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.LINK_TEXT, "2023-C-2-1615-2880-TDS-007")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.ID, "form_autocomplete_downarrow-1691804411491").click()
    self.driver.find_element(By.CSS_SELECTOR, "#form_autocomplete_suggestions-1691804411491 > li:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#form_autocomplete_suggestions-1691804411491 > li:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".d-flex > .btn-primary").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".fa-cogs")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".fhs-tooltip")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".site-name").click()
    self.driver.find_element(By.LINK_TEXT, "Calendario").click()
    self.driver.execute_script("window.scrollTo(0,127.33333587646484)")
    self.driver.execute_script("window.scrollTo(0,600)")
    self.driver.execute_script("window.scrollTo(0,274)")
    self.driver.find_element(By.CSS_SELECTOR, ".day:nth-child(6) > .d-none .icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".modal-header > .close").click()
    self.driver.find_element(By.ID, "action-menu-toggle-1").click()
    self.driver.find_element(By.ID, "actionmenuaction-7").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("33333333")
    self.driver.find_element(By.ID, "loginbtn").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "yui_3_17_2_1_1691804486178_27").click()
  

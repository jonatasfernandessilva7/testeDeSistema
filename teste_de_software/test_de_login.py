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

class TestesDeLogin():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  def test_testeLoginVazio(self):
    self.driver.get("http://localhost:8000/login")
    self.driver.set_window_size(1849, 1080)
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

  def test_testeLoginSemSenha(self):
    self.driver.get("http://localhost:8000/login")
    self.driver.set_window_size(1849, 1080)
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_username").send_keys("jonatasteste")
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

  def test_testeLoginSemUsuario(self):
    self.driver.get("http://localhost:8000/login")
    self.driver.set_window_size(1849, 1080)
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("jonatas")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
  
  def test_testeLoginCorreto(self):
    self.driver.get("http://localhost:8000/login")
    self.driver.set_window_size(1849, 1080)
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_username").send_keys("jonatasteste")
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("jonatas")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

  def test_testeLoginComUsuarioInexistente(self):
    self.driver.get("http://localhost:8000/login")
    self.driver.set_window_size(1849, 1080)
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_username").send_keys("joojo") 
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("jonatas")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
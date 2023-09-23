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

class TesteTelaInicio():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
    
  def test_teste_tela_inicia_normal_com_todos_os_elementos(self):
    self.driver.get("http://localhost:8000/login")
    self.driver.set_window_size(1849, 1080)
    assert self.driver.find_element(By.LINK_TEXT, "Login").text == "Login"
    assert self.driver.find_element(By.LINK_TEXT, "Cadastrar").text == "Cadastrar"
    
  def test_tela_inicio_vai_para_tela_login(self):
    self.driver.get("http://localhost:8000/login")
    self.driver.set_window_size(1849, 1080)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".btn").text == "Logar" 
        
  def test_tela_inicio_vai_para_tela_cadastro(self):
    self.driver.get("http://localhost:8000/login")
    self.driver.set_window_size(1849, 1080)
    self.driver.find_element(By.LINK_TEXT, "Cadastrar").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".btn").text == "Cadastrar"

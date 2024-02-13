from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button(browser):
    browser.get(url=link)
    all_buttons = WebDriverWait(browser, 5).until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                                                       "button.btn-add-to-basket")),
                                                  message=f'Not find button in this page.')
    button_list = ', '.join([tmp.text for tmp in all_buttons])
    assert len(all_buttons) == 1, f"Find more one buttons in this page. list buttons is: '{button_list}'"
    sleep(30)

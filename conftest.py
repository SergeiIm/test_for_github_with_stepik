import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru')


@pytest.fixture(scope='function')
def browser(request):
    language_session = request.config.getoption('--language')
    language_session = language_session.lower()
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language_session})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

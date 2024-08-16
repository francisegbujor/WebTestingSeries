import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService

driver = None
url = "https://the-internet.herokuapp.com/"

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser to run tests on: chrome, firefox, IE"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = ChromeService()
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = FirefoxService()
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "IE":
        service_obj = IEService()
        driver = webdriver.Ie(service=service_obj)
    else:
        raise ValueError(f"Browser {browser_name} is not supported")

    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    print("Browser:", browser_name)
    yield driver
    print("Close Driver")
    driver.quit()

def _capture_screenshot(driver, name):
    driver.get_screenshot_as_file(name)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(item.instance.driver, file_name)
            if file_name:
                html = f'<div><img src="{file_name}" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

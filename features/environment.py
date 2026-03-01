from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    ### CHROME / FIREFOX ###
    # context.driver = webdriver.Chrome()
    # context.driver = webdriver.Firefox()

    ### HEADLESS MODE ###
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(options=options)

    ### BROWSERSTACK ###
    bs_user = 'olyaqaautomation_TImQYF'
    bs_key = 'eQsmSjDX6v6KysdPxvkn'

    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    options = Options()
    bstack_options = {
        "os": "OS X",
        "osVersion": "Tahoe",
        "browserName": "Chrome",
        "browserVersion": "latest",
        "sessionName": scenario_name,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    # chrome_options = Options()
    # prefs = {"profile.default_content_setting_values.notifications": 2}
    # chrome_options.add_experimental_option("prefs", prefs)
    # context.driver = webdriver.Chrome(options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def accept_alert_if_present(driver, timeout=15):
    try:
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except NoAlertPresentException:
        pass
    except Exception as e:
        print(f"Warning: failed to accept alert: {e}")
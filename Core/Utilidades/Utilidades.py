import datetime
from Core.Base import Base
import random
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utilidades(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def create_umr_code(text = ""):
        umr = text + "umrcode" + str(random.randint(100,999999))
        return umr

    def create_source_system_reference_code(text = ""):
        source_system_reference = text + "sourceSystemReference" + str(random.randint(100,99999999999))
        return source_system_reference

    def set_current_data_time():
        utc_now = datetime.datetime.utcnow()
        utc_now_fixed = utc_now - datetime.timedelta(seconds=10)
        NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        return NVUD



    def check_if_element_exist(self, locator):
        try:
            self.element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

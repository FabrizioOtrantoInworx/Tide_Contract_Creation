from Pages.Shared.Navbar import NavBar
from Core.Base import Base
from Core.Espera import Espera

class HomePage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_for_url_to_contain(driver, "home")
        self.Navbar = NavBar(driver)



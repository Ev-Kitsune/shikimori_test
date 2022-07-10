from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Setting:

    mainPth = ""
    IM_PWAIT = 3
    Keys = Keys
    x = 1500
    y = 768
    browserPth = 'C:\\v-code\\chromedriver.exe'
    
    def initDriver(self):
        """
        Инициализация вебдрайвера
        """
        driver = webdriver.Chrome(self.browserPth)
        
        driver.implicitly_wait(self.IM_PWAIT)
        driver.set_window_size(self.x, self.y)
    
        return driver
class Search:

    def __init__(self, driver):
        self.driver = driver

    def run_search(self, text, point, keys):
        # Шаги
        try:
            text = str(text)
            point = int(point)
        except:
            return 'bad input data'
        try:
            element = self.driver.find_element_by_css_selector('input[placeholder="Поиск..."]')
        except:
            return 'can not find search-input'
        try:
            element.click()
        except:
            return 'can not click to element'
        elements = self.driver.find_elements_by_css_selector('div.search-mode')
        if (len(elements) == 0):
            return 'can not find filtres'
        try:
            elements[point].click()
        except:
            return 'can not click to element'
        try:
            element.send_keys(text)
            element.send_keys(keys.ENTER)
        except:
            return 'can not send text'
        # Проверки
        try:
            self.driver.find_element_by_css_selector('p.age-restricted-warning')
            return True
        except:
            if point == 0:
                try:
                    filter_res = self.driver.find_element_by_css_selector('header.head h1')
                    if ('Лучшие аниме' not in filter_res.text):
                        return 'Bad filter work'
                except:
                    return 'Can not find filter result'
            elif point == 1:
                try:
                    filter_res = self.driver.find_element_by_css_selector('header.head h1')
                    if ('Манга' not in filter_res.text):
                        return 'Bad filter work'
                except:
                    return 'Can not find filter result'
            elif point == 2:
                try:
                    filter_res = self.driver.find_element_by_css_selector('header.head h1')
                    if (str('Ранобэ') != str(filter_res.text)):   
                        return 'Bad filter work'        
                except:
                    return 'Can not find filter result'
            elif point == 3:
                try:
                    filter_res = self.driver.find_element_by_css_selector('header.head h1')
                    if ('Персонажи' not in filter_res.text):
                        return 'Bad filter work'
                except:
                    return 'Can not find filter result'
            elif point == 4:
                try:
                    filter_res = self.driver.find_element_by_css_selector('header.head h1')
                    if ('Поиск людей' not in filter_res.text):
                        return 'Bad filter work'
                except:
                    return 'Can not find filter result'
        try:
            elements = self.driver.find_elements_by_css_selector('span[itemprop="name"]')
            if len(elements) > 0:
                for element in elements:
                    if (text.lower() not in element.text.lower()):
                        return 'bad search'
            else:
                elements = self.driver.find_elements_by_css_selector('a[itemprop="url"]')
                if len(elements) > 0:
                    for element in elements:
                        if (text.lower() not in element.text.lower()):
                            return 'bad search'
                else:
                    return "Not found"
        except:
            return False          
        return True
        

######  работа с переключением вкладок

def switch_window(list_1, list_2):
    for i in list_2:
        if i not in list_1:
            return i
    return False

import pytest
import meta
import lib

settings = meta.Setting()
driver = settings.initDriver()
search = lib.Search(driver)
 
 
def setup_module(module): ## Перед тестовым прогоном
    settings.mainPth = 'https://shikimori.one/'

def teardown_module(module): ## После тестового прогона
    driver.quit()

def setup_function(function): ## Перед каждым тестом
    driver.get(settings.mainPth)
    
def teardown_function(function): ## После каждого теста
    driver.refresh()

def test_t():
    pass

 # # Сами тесты
 @pytest.mark.parametrize("text, point",
 [
 ('naruto', '0'),
 ('naruto', '2'),
 ('naruto', '3'),
 ('NARUTO', '4'),
 ('Покемон', '1'),
 ('Spy x Family', '1'),
 ('naruto', '1'),
 ])
 def test_searchPositive(text, point):
     assert search.run_search(text, point, meta.Keys) is True

 @pytest.mark.parametrize("text, point",
 [
 ('dsfsdkjfbsdkjchbsdlcjkashdbcjlasdcbhsd', '0'),
 ('    ', '2'),
 ])
 def test_searchNegative(text, point):
     assert search.run_search(text, point, meta.Keys) is not True


  

######  работа с переключением вкладок

def test_handle():
    
    list_hnd_1 = driver.window_handles      # сюда положили список айдишноков открытых вкладок
    
    pass                                    # здесь типа открыли еще одну вкладку
    
    list_hnd_2 = driver.window_handles      # снова положили список айдишников открытых вкладок, 
                                            # на этот раз, в списке на 1 вкладку больше чем в предыдущем
    
    list_hnd_3 = list_hnd_2 - list_hnd_1    # данное действие записывает разницу в 1 элемент в новую переменную list_hnd_3
    
    driver.switch_to.window(list_hnd_3[0])  # смещаем фокус селениума вручную на выбранную вкладку. Поскольку разница,
                                            # записанная в переменную list_hnd_3 точно содержит всего один элемент, его индекс
                                            # будет равен 0.


#### вариант кода выше, но взаимодействующий с кусочком кода из lib. 

def test_handle():

    list_hnd_1 = driver.window_handles
    pass                                    
    list_hnd_2 = driver.window_handles      
    handle = lib.switch_window(list_hnd_1, list_hnd_2) # вариант когда для запуска написанного куска в lib. 
    driver.switch_to.window(handle)
    
    driver.switch_to.frame(frame_reference)
    pass
    driver.switch_to.window(list_hnd_1[0])
    driver.close()  
    list_hnd_1 = driver.window_handles
    driver.switch_to.window(list_hnd_1[0])
    a = 1


def test_alert():
    driver.execute_script('alert("123")')
    al = driver.switch_to.alert()
    a = 1
    
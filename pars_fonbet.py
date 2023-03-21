from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, service=Service(
ChromeDriverManager().install()))



def main(): 
    try:
        list_num =[]
        list_second = []
        list_first = []
        list_player = []
        list_liga_durty = []
        list_liga_clear =[]
        driver.get(url='https://www.fon.bet/live/table-tennis/')
        time.sleep(4)

        language = driver.find_element(By.CLASS_NAME, 'header__lang-icon')
        language.click()
        # time.sleep(1)
        driver.maximize_window()
        language_1 = driver.find_element(By.CLASS_NAME, '_icon_en')
        language_1.click()
        
        setings = driver.find_element(By.CLASS_NAME, 'settings__option-link')
        setings.click() 
        # time.sleep(10)

        square = driver.find_elements(By.CLASS_NAME, 'ck__checkbox--63RBar')[4]
        square.click()
        time.sleep(2)

        close = driver.find_element(By.CLASS_NAME, 'settings__close--2boyLZ')
        close.click()
        time.sleep(2)

        head_table = driver.find_elements(By.CLASS_NAME, 'sport-competition--PvDzHX') # _clickable--ogfexh _compact--6zvh5M
        for country in head_table:
            country_set = country.find_element(By.CLASS_NAME, 'table-component-text--5BmeJU').text 
            country_clear = country_set.split('.')
            # print(country_element[0])
            if country_clear[0] == 'BELARUS':
                continue 
            elif country_clear[0] == 'RUSSIA' :
                continue 
            else:
                players = driver.find_elements(By.CLASS_NAME, 'sport-event__name--HefZLq') # sport-event__name--HefZLq _clickable--G5cwQm _event-view--7J8rEd _compact--7BwYe1
                for play in players:
                    play_clear = play.text  #вот игроки ------------------------------------------------
                    # print(play_clear)

                    list_player.append(play_clear)


                head_lig = driver.find_elements(By.CLASS_NAME, 'sport-competition--PvDzHX')
                
                for info_lig_tab in head_lig :
                    list_liga_durty.append(info_lig_tab.text)

                for head_spisok in list_liga_durty:                  #вот тут лиги -----------------------------------------
                    split_list = head_spisok.split('.')
                    if len(split_list) == 4 or len(split_list)==3:
                        clear_lig1 = split_list[1]
                        list_liga_clear.append(split_list[1])
                    elif len(split_list) == 2:
                        clear_lig2 = split_list[0]    
                        list_liga_clear.append(split_list[0])      
                    

                # for f in x:
                #     list = f.split('.')
                #     # print (list)
                #     if len(list) == 4 or len(list)==3:
                #         print (list[1])
                #     elif len(list) == 2:
                #         print(list[0])
                #     else :
                #         print('error')
                    


                all_num = driver.find_elements(By.CLASS_NAME, 'table-component-factor-value_single--6nfox5') #  _compact--7j5yEe cell-state-normal--iYJc0x value-state-normal--4JL4xN 
                for all_n in all_num:
                    all_num_clear = all_n.text 
                    # print (all_num_clear)
                    list_num.append(all_num_clear)
        # print(list_num)

                for first_num in range (0,len(list_num), 4):
                    first_num_clear = list_num[first_num]
                    list_first.append(first_num_clear)


                
                for second_num in range (1,len(list_num), 4):
                    second_num_clear = list_num[second_num]
                    list_second.append(second_num_clear)

        # print (list_player)
        # print('-------------------')
        # print (list_first)
        # print('-------------------')
        # print (list_second)
        # print('-------------------')
        # print(list_liga_clear)
        spisok_fir =[]
        spisok_sec = []
        for num in list_first:
            strnum = str(num) + '='
            spisok_fir.append(strnum)
        for num in list_second:
            strnum = str(num) + '='
            spisok_sec.append(strnum)

        # print(spisok_sec)
        # print('--------------')
        # print(spisok_sec)



        with open('fonbet123.csv', 'w', newline='' ) as file:
            Writer = csv.writer(file, delimiter=';')
            Writer.writerow(
                (
                'liga',
                'players',
                'fir',
                'sec',
                )
            )

        with open ('fonbet123.csv', 'a', newline='') as file:
                writer = csv.writer(file, delimiter=';' )
                for cycle in range(0,len(list_liga_clear)):
                    writer.writerow((
                            list_liga_clear[cycle],
                            list_player[cycle],
                            spisok_fir[cycle],
                            spisok_sec[cycle]
                            )
                    )


    except Exception as ex:
        print (ex)

    finally:
        driver.close
        driver.quit

main()



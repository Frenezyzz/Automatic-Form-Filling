
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

webdriver_path = r'add the webdriver in here'


service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service)


url_form = "add the url link form"
driver.get(url_form)
time.sleep(3)

df = pd.read_csv('Book1.csv')
row_dicts = df.apply(lambda row: row.to_dict(), axis=1).tolist()

for data in row_dicts:

    #Email
    email_input_tag = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input'
    driver.find_element('xpath', email_input_tag).send_keys(data['Mail'])

    # Name
    name_input_tag = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]'
    name_value_select = f'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]//*[@data-value="{data['name']}"]'
    name_input_tag = driver.find_element('xpath',name_input_tag).click()
    time.sleep(1)
    name_value_select = driver.find_element('xpath',name_value_select).click()

    # TL
    time.sleep(1)
    tl_input_tag = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]'
    tl_value_select = f'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]//*[@data-value="{data['TL']}"]'
    tl_input_tag = driver.find_element('xpath',tl_input_tag).click()
    time.sleep(1)
    tl_value_select = driver.find_element('xpath',tl_value_select).click()
    time.sleep(1)
    # Course
    courses_options = {
        'Python'      : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label',
        'Scratch'     : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]/label',
        'Web Design'  : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]/label', 
        'FWD'         : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[4]/label',
        'Roblox'      : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[5]/label',
        'Python Pro'  : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[6]/label',  
        'FWD Pro'     : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[7]/label',
        'FunTech'     : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[8]/label',
        'Math lvl 1'  : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[9]/label',  
        'Math lvl 2'  : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[10]/label',   
        'Math lvl 3'  : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[11]/label',   
        'Math lvl 4'  : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[12]/label',   
        'Math lvl 5'  : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[13]/label',   
        'Unity'       : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[14]/label',
    }
    driver.find_element('xpath',courses_options[data['Course']]).click()
    # Format
    format_options = {
        'Group'                : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label',
        'Extra-class'          : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label',
        'One-time replacement' : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[3]/label',
        'Group (FunTech)'      : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[4]/label',
        'Group (Math)'         : '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[5]/label',
    }
    driver.find_element('xpath',format_options[data['Format']]).click()


    # Group 
    ## COntainer of options

    container_options_groups = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[1]')
    container_options_groups.click()
    time.sleep(1)

    try:
        
        option_group = driver.find_element('xpath', f"//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]//*[@data-value='{data['Group']}']")
        
        option_group.click()
        time.sleep(1)

        container_options_groups = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[1]')
        time.sleep(1)
        container_options_groups.click()

        option_group = driver.find_element('xpath', "//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]//*[@data-value='No grupo']")

        time.sleep(1)
        option_group.click()


    except NoSuchElementException:
        
        option_group = driver.find_element('xpath', "//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]//*[@data-value='No grupo']")
        option_group.click()
        
        time.sleep(1)
        container_options_groups = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[1]')
        time.sleep(1)
        container_options_groups.click()
        time.sleep(1)

        option_group = driver.find_element('xpath', f"//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[2]//*[@data-value='{data['Group']}']")

        time.sleep(1)
        option_group.click()


    # Duracion
    options_duration = {
        '60' : '//*[@id="i90"]',
        '90' : '//*[@id="i93"]',
        '30' : '//*[@id="i96"]',
    }


    duration_option = driver.find_element('xpath', options_duration[str(data['Duration'])])
    duration_option.click()

    # siguiente pagina

    next_button = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    next_button.click()

    # Pagina 2
    # Fecha
    time.sleep(2)
    date_input = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')


    date_input.send_keys(data['Date'])

    # Module

    options_modules = {
        '1' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]',
        '2' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]',
        '3' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]',
        '4' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[4]',
        '5' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[5]',
        '6' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[6]',
        '7' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[7]',
        '8' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[8]',
        '9' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[9]',
        '10' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[10]',
        '11' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[11]',
    }

    module_option = driver.find_element('xpath', options_modules[str(data['Module'])]).click()

    # Lesson
    options_lessons = {
        '1' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]',
        '2' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]',
        '3' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[3]',
        '4' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[4]',
        '5' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[5]',
        '6' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[6]',
        '7' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[7]',
        '8' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[8]',
        '9' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[9]',
        '10' : '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[10]',
    }

    lesson_option = driver.find_element('xpath', options_lessons[str(data['Lesson'])]).click()

    # Link
    link_recording = driver.find_element('xpath', '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_recording.send_keys(data['Link'])

    # Next
    # Pagina 3
    input()
    next_button = driver.find_element('xpath', '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span').click()

    # Summit
    input('Are u sure to summit this form?')
    next_button = driver.find_element('xpath', '/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[3]/div[1]/div[2]/div[2]').click()




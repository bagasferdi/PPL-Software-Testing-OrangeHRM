import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture()

def driver():
    driver = webdriver.Chrome()
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.maximize_window()
    yield driver
    driver.quit()

def test(driver):
    time.sleep(3)
    driver.find_element(By.NAME, 'username').send_keys('Admin')
    driver.find_element(By.NAME, 'password').send_keys('admin123' + Keys.ENTER)
    time.sleep(3)

    # Masuk_Menu_Admin
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
    time.sleep(3)

    # Mencari_User_menggunakan_username_Benar
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys('Siti Maymunah')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Mencari_User_menggunakan_username_Salah
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input').send_keys('Mamung')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Menampilkan_data_User_tanpa_memasukkan_input_apapun
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Menambah_User_baru_tanpa_mengisi_input_apapun
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[1]').click()
    time.sleep(3)

    # Masuk_Menu_PIM
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
    time.sleep(3)

    # Mencari_Employee_menggunakan_Employee_Name_Benar
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys('Siti Maymunah')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()
    
    # Mencari_Employee_menggunakan_Employee_Name_Salah
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys('Mamung')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Mencari_Employee_menggunakan_Employee_Id_Benar
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys('0070')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Mencari_Employee_menggunakan_Employee_Id_Salah
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys('2290')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Menampilkan_data_Employee_tanpa_memasukkan_input_apapun_kecuali_include
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Menambahkan_Employee_baru
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
    time.sleep(3)
    driver.find_element(By.NAME, 'firstName').send_keys('Aurelis')
    driver.find_element(By.NAME, 'middleName').send_keys('Sinta')
    driver.find_element(By.NAME, 'lastName').send_keys('Gros')
    driver.find_element(By.CLASS_NAME, 'oxd-switch-input--active').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input').send_keys('aurelis')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input').send_keys('areli123')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input').send_keys('aureli123')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
    time.sleep(10)

    # Menambah_Employee_baru_tanpa_mengisi_input_apapun
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[1]').click()
    time.sleep(3)

    # Masuk_Menu_Leave
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a').click()
    time.sleep(3)

    # Mencari_Employee_berdasarkan_rentang_waktu_yang_sesuai
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys('2022-01-01')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys('2023-12-31')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[3]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[3]/button[1]').click()

    # Mencari_Employee_berdasarkan_waktu_yang_salah
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys('2026-01-01')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys('2023-12-31')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[3]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[3]/button[1]').click()

    # Mencari_Employee_berdasarkan_waktu_yang_tidak_sesuai_format
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys('Test')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys('31-12-2023')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[3]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[3]/button[1]').click()

    # Menampilkan_data_Employee_tanpa_memasukkan_input_apapun_kecuali_rentang_waktu_dan_Status
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[3]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[3]/button[1]').click()

    # Membuat_Permintaan_Leave_tanpa_mengisi_input_apapun
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[5]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a').click()
    time.sleep(3)

    # Masuk_Menu_Time
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a').click()
    time.sleep(3)

    # Mengupdate_Timesheet_tanpa_memasukkan_input_apapun
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[3]/div/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button[3]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a').click()
    time.sleep(3)

    # Masuk_Menu_Recruitment
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a').click()
    time.sleep(3)

    # Mencari_Candidates_menggunakan_Keywords_Benar
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[2]/div/div[2]/input').send_keys('Network Engineer')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[1]').click()

    # Mencari_Candidates_menggunakan_Keywords_Salah
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[2]/div/div[2]/input').send_keys('Test')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[1]').click()

    # Mencari_Employee_berdasarkan_rentang_waktu_yang_sesuai
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[3]/div/div[2]/div/div/input').send_keys('2022-01-01')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[4]/div/div[2]/div/div/input').send_keys('2023-12-31')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[1]').click()

    # Mencari_Employee_berdasarkan_waktu_yang_salah
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[3]/div/div[2]/div/div/input').send_keys('2026-01-01')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[4]/div/div[2]/div/div/input').send_keys('2023-12-31')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[1]').click()

    # Mencari_Employee_berdasarkan_waktu_yang_tidak_sesuai_format
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[3]/div/div[2]/div/div/input').send_keys('Test')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[4]/div/div[2]/div/div/input').send_keys('31-12-2023')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[1]').click()

    # Menampilkan_data_Candidates_tanpa_memasukkan_input_apapun
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[1]').click()

    # Menambahkan_Candidate_baru
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input').send_keys('Darin ')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[2]/div[2]/input').send_keys('Mahendra')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[3]/div[2]/input').send_keys('Tumaris')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input').send_keys('DMahendraT@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input').send_keys('081234567890')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[5]/div/div[1]/div/div[2]/input').send_keys('Network Engineer')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[6]/div/div/div/div[2]/textarea').send_keys('Hi Manager!')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[7]/div/div/div/div[2]/div/label/span/i').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]').click()
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a').click()
    time.sleep(3)

    # Menambahkan_Candidate_baru_tanpa_input_apapun
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[8]/button[1]').click()
    time.sleep(3)

    # Melihat_detail_data_Candidate
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a').click()
    time.sleep(3)

    # Menghapus_Candidate
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()
    time.sleep(5)

    # # Mengunduh_resume_Candidate
    # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[7]/div/button[3]').click()
    # time.sleep(3)

    # Masuk_Menu_My_Info
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]').click()
    time.sleep(3)

    # Mengupdate_Personal_Details
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys('Bambang')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input').send_keys('Ardiansyah')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button').click()
    time.sleep(3)
    #Tidak bisa pilih dropdown Blood Type

    # Mengupdate_Contact_Details
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]').click()
    time.sleep(3)
    # Tidak bisa pilih dropdown Country
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input').send_keys('0251 123456')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click()
    time.sleep(3)

    # Menambah_Emergency_Contact
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys('Risma')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input').send_keys('Ani')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input').send_keys('0251 123456')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input').send_keys('081234567890')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input').send_keys('111 1221 34456')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]').click()
    time.sleep(3)

    # Immigration
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[1]/div[2]/div').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input').send_keys('1234567')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/input').send_keys('Eligible')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/input').send_keys('2022-12-12')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/div/div/input').send_keys('2025-12-12')
    # Tidak bisa pilih dropdown Country
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[6]/div/div[2]/div/div/input').send_keys('2023-12-12')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[7]/div/div[2]/textarea').send_keys('Test')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]').click()
    time.sleep(3)

    # Melihat_Job
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]').click()
    time.sleep(3)

    # Melihat_Salary
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]').click()
    time.sleep(3)

    # Melihat_Tax_Exemptions
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]').click()
    time.sleep(3)

    # Melihat_Report_to
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]').click()
    time.sleep(3)

    # Masuk_Menu_Performance
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]').click()
    time.sleep(3)

    # Masuk_Sub_Menu_Manage_Reviews
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]').click()
    time.sleep(3)

    # Manage_Performance_Reviews_berdasarkan_rentang_waktu_yang_sesuai
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys('2022-01-01')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys('2023-12-31')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Manage_Performance_Reviews_berdasarkan_waktu_yang_salah
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys('2026-01-01')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys('2023-12-31')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Manage_Performance_Reviews_berdasarkan_waktu_yang_tidak_sesuai_format
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[6]/div/div[2]/div/div/input').send_keys('Test')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div[7]/div/div[2]/div/div/input').send_keys('31-12-2023')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]').click()

    # Menambah_Performance_Review_tanpa_input_apapun
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/button[3]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/button[1]').click()
    time.sleep(3)

    # # Melihat_detail_Performance_Reviews
    # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[8]/div/button[2]').click()
    # time.sleep(3)
    # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
    # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]').click()
    # time.sleep(3)

    # # Menghapus_Performance_Reviews
    # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[8]/div/button[1]').click()
    # driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()
    # time.sleep(3)

    # Melihat_My_Performance_Trackers
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]').click()
    time.sleep(3)

    # Masuk_Menu_Dashboard
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
    time.sleep(3)

    # Membuat_data_Punch_In_dan_Punch_Out
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/form/div[3]/button').click()
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
    time.sleep(3)

    # Melihat_Leave_Request_to_Approve
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
    time.sleep(3)

    # Melihat_Timesheets_to_Approve
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
    time.sleep(3)

    # Melihat_Pending_Self_Review
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[3]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
    time.sleep(3)

    # Melihat_Candidate_to_Interview
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[4]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
    time.sleep(3)

    # Assign_Leave
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
    time.sleep(3)

    # Melihat_Leave_List
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[2]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
    time.sleep(3)

    # Melihat_Timesheets
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[3]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
    time.sleep(3)

    # Melakukan_Apply_Leave
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[4]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
    time.sleep(3)

    # Melihat_My_Leave
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[5]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
    time.sleep(3)

    # Melihat_My_Timesheet
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[6]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
    time.sleep(3)

    # Melihat_Detail_Post
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[4]/div/div[2]/div/div[1]/div').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a').click()
    time.sleep(3)

    # Mengatur_Configuration_untuk_card_Employees_on_Leave_Today
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[5]/div/div[1]/i').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[5]/div[2]/div/div/div/form/div[1]/div/div[2]/div/label/span').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[5]/div[2]/div/div/div/form/div[2]/button[2]').click()
    time.sleep(3)

    # Masuk_Menu_Directory
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a').click()
    time.sleep(3)

    # Mencari_Employee_tanpa_memasukkan_inpu_apapun
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
    time.sleep(3)

    # Melihat_Detail_Employee
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a').click()
    time.sleep(3)

    # Masuk_Menu_Buzz
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]').click()
    time.sleep(3)

    # Membuat_postingan_hanya_teks
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/form/div/textarea').send_keys('Hi Bro! whats up?')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/form/div/div/button').click()
    time.sleep(3)

    # Membuat_postingan_hanya_link_video
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/button[2]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div[2]/div[2]/textarea').send_keys('https://www.youtube.com/watch?v=jfiqzf5MXT8&pp=ygUDbmNz')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div[3]/button').click()
    time.sleep(3)

    # Membuat_postingan_dengan_caption_dan_video
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/form/div/textarea').send_keys('Hi Bro! whats up?')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/button[2]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div[2]/div[2]/textarea').send_keys('https://www.youtube.com/watch?v=jfiqzf5MXT8&pp=ygUDbmNz')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/form/div[3]/button').click()
    time.sleep(3)

    # Membuat_postingan_tanpa_input_apapun
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div[2]/form/div/div/button').click()
    time.sleep(3)

    # Melakukan_filter_post_berdasarkan_Most_Liked_Post
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/button[2]').click()
    time.sleep(3)

    # Melakukan_filter_post_berdasarkan_Most_Commented_Post
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/button[3]').click()
    time.sleep(3)

    # Melakukan_filter_post_berdasarkan_Most_Recent_Post
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/button[1]').click()
    time.sleep(3)

    # Melakukan_like_pada_postingan
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[3]/div[1]/div').click()
    time.sleep(3)

    # Melakukan_komentar_pada_postingan
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[3]/div[1]/button[1]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[4]/div/form/div/div[2]/input').send_keys('Hello Dude, no problem me just testing' + Keys.ENTER)
    time.sleep(3)

    # Melakukan_share_postingan
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[3]/div[1]/button[2]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/form/div[1]/div[2]/div/textarea').send_keys('It is very amazing Bro')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/form/div[3]/button').click()
    time.sleep(3)

    # Melakukan_edit_postingan
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/li/button').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/li/ul/li[2]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/form/div[1]/div[2]/div/textarea').send_keys(Keys.CONTROL, "a", Keys.DELETE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/form/div[1]/div[2]/div/textarea').send_keys('Hi!')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/form/div[3]/button').click()
    time.sleep(3)

    # Menghapus_postingan
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/li/button').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div[2]/li/ul/li[1]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()
    time.sleep(3)
from selenium import webdriver
from selenium.webdriver.common.by import By


from db import insert_data, cur, conn

driver = webdriver.Chrome()

urls = {'https://www.youtube.com/@raily',
        'https://www.youtube.com/@adorplayer',
        'https://www.youtube.com/@soderlingoc',
        'https://www.youtube.com/@sodyan',
        'https://www.youtube.com/@restlgamer',
        'https://www.youtube.com/@drozhzhin',
        'https://www.youtube.com/@empatia_manuchi',
        'https://www.youtube.com/@barsikofficial',
        'https://www.youtube.com/@diodand',
        'https://www.youtube.com/@nedohackerslite'}


# elements_with_video_href1 = None
# video_href1 = None
# channel_username = None
# elements_with_video_href = None
# video_id = None


def get_video_data(urls, elements_with_video_href=None):

    # global elements_with_video_href1, video_href1, channel_username, elements_with_video_href, video_id
    for url in urls:
        if url:

            try:
                '''переход по url адресу'''
                driver.get(url)
                driver.implicitly_wait(0.5)
            except Exception as ex:
                print(f"url not found, error: {ex}")

            try:

                channel_username = url.split('com/')[1]  # имя канала, вычлененное из url
                '''ищем все элементы с ссылкой на видео внутри'''
                elements_with_video_href = driver.find_elements(By.ID, "video-title")
            except Exception as ex:
                print(f"что-то с поиском ссылок на элементы по id video-title, error: {ex}")

            try:
                '''доп. элемент содержащий ссылку на видео, который есть не у всех каналов'''
                elements_with_video_href1 = driver.find_element(By.CSS_SELECTOR, "#title > a")
                '''если элемента нету, идем дальше по коду'''
                if not elements_with_video_href1:
                    continue
            except Exception as ex:
                print(f"что-то с поиском доп. элемента по селектору title > a, error: {ex}")

            try:
                '''вычленение ссылки на видео из элемента'''
                video_href1 = elements_with_video_href1.get_attribute('href')
            except Exception as ex:
                print(f"что-то с вычленением ссылки на видео из элемента href1, error: {ex}")

            try:
                '''Вычленение id видео из ссылки на видео'''
                video_id1 = video_href1.split("v=")[1]
            except Exception as ex:
                print(f'что-то с вычленением id видео из ссылки на видео video_href1, error: {ex}')

            try:
                '''логируем имя канала, ссылку на опциональное видео и его id'''
                print(channel_username, video_href1, video_id1)
                insert_data(channel_username, video_href1, video_id1)
            except Exception as ex:
                print(f'что-то с записью доп. элемента в бд, error: {ex}')
            try:
                '''проходим по всем элементам с видео'''
                for elem in elements_with_video_href:
                    '''вычленение ссылки на видео из элемента'''
                    video_href = elem.get_attribute('href')
                    '''Вычленение id видео из ссылки на видео'''
                    video_id = video_href.split("v=")[1]
                    '''логируем ссылку и id видео'''
            except Exception as ex:
                print(f'что-то в цикле по элементам с видео, error: {ex}')
            try:
                print(channel_username, video_href, video_id)
                insert_data(channel_username, video_href, video_id)
            except Exception as ex:
                print(f"что-то с записью основных данных в бд, message: {ex}")

        else:
            driver.quit()


try:
    get_video_data(urls)
    conn.commit()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cur.close()
    conn.close()
    driver.quit()


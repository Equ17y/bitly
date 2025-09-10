import os
from dotenv import load_dotenv
import requests
from urllib.parse import urlparse
import argparse

def is_shorten_link(token, url):
  
    parsed_url = urlparse(url)
    if parsed_url.netloc != 'vk.cc' or len(parsed_url.path) <= 1:
        return False
            
    link_key = parsed_url.path.split('/')[-1]
        
    api_url = 'https://api.vk.ru/method/utils.getLinkStats'
        
    params = {
        'key': link_key,
        'access_token': token,
        'v': '5.131'
    }
            
    response = requests.get(api_url, params=params)
    response.raise_for_status()
        
    api_response = response.json()
        
    if 'error' in api_response:
        error_message = api_response['error']['error_msg']
        raise Exception(f"Ошибка VK API: {error_message}")
        
    return 'response' in api_response

def shorten_link(token, url):
    api_url = 'https://api.vk.ru/method/utils.getShortLink'
    
    params = {
        'url': url,
        'access_token': token,
        'v': '5.131'
    }
        
    response = requests.get(api_url, params=params)
    response.raise_for_status()
        
    api_response = response.json()
    
    if 'error' in api_response:
        error_message = api_response['error']['error_msg']
        raise Exception(f"Ошибка API: {error_message}")
    
    return api_response['response']['short_url']

def count_clicks(token, short_url):
    
    parsed_url = urlparse(short_url)
    key = parsed_url.path.split('/')[-1]
    
    api_url = 'https://api.vk.ru/method/utils.getLinkStats'
    
    params = {
        'key': key,
        'access_token': token,
        'v': '5.131'
    }
        
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    api_response = response.json()
    
    if 'error' in api_response:
        error_message = api_response['error']['error_msg']
        raise Exception(f"Ошибка API: {error_message}")
    
    
    total_clicks = 0
    for day_stats in api_response['response']['stats']:
        total_clicks += day_stats['views']
        
    return total_clicks
   

def main():
    load_dotenv()
    token = os.environ['VK_API_TOKEN']

    try:
        parser = argparse.ArgumentParser(description='Сокращение ссылок VK и подсчет кликов')
        parser.add_argument('link', help='link для обработки (сокращение или подсчет кликов)')
        args = parser.parse_args()
        user_link = args.link

        if is_shorten_link(token, user_link):
            clicks = count_clicks(token, user_link)
            print(f'Количество кликов по ссылке: {clicks}')
        else:
            short_url = shorten_link(token, user_link)
            print(f'Сокращенная ссылка: {short_url}')
        
    except requests.exceptions.HTTPError as e:
        print(f"Ошибка HTTP: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Ошибка соединения: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Таймаут запроса: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
    except KeyError as e:
        print(f"Ошибка ключа в ответе API: {e}")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        
    
if __name__ == "__main__":
    main()
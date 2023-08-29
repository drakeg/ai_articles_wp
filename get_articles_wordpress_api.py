import requests
import base64
import os
from dotenv import load_dotenv

def get_total_pagecount():
 response = requests.get(api_url)
 pages_count = response.headers['X-WP-TotalPages']
 return int(pages_count)

def read_wordpress_posts_with_pagination():
 total_pages = get_total_pagecount()
 current_page = 1
 all_page_items_json = []
 while current_page <= total_pages:
    api_url = f"{api_url}?page={current_page}&per_page=100"
    page_items = requests.get(api_url)
    page_items_json = page_items.json()
    all_page_items_json.extend(page_items_json)
    current_page = current_page + 1
 return all_page_items_json

load_dotenv()
wordpress_user = os.getenv('WORDPRESS_USER')
wordpress_password = os.getenv('WORDPRESS_PASSWORD')
wordpress_credentials = wordpress_user + ":" + wordpress_password
wordpress_token = base64.b64encode(wordpress_credentials.encode())
wordpress_header = {'Authorization': 'Basic ' + wordpress_token.decode('utf-8')}
api_url = os.getenv('API_URL')

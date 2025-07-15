import threading
import requests
from bs4 import BeautifulSoup
import time

urls = [
    'https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)',
    'https://en.wikipedia.org/wiki/Attention_Is_All_You_Need',
    'https://en.wikipedia.org/wiki/Large_language_model'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched:{len(soup.text)} as characters from {url}')

if __name__=='__main__':

    # Using simple python code--
    t1 = time.time()
    for url in urls:
        fetch_content(url)
    
    tt1 = time.time()-t1
    print(tt1)


    # Now using multithreading--
    t2 = time.time()
    threads = []

    for url in urls:
        thread = threading.Thread(target=fetch_content,args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    tt2 = time.time()-t2
    print(tt2)
    
    print('All webpages fetched.')
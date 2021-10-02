# Video tutorial on how to automate web browser opening and visiting using python script
# You can use this to open web browsers, social media posts, youtube page/video, or blog site
# to increase visitors and views

import time
import webbrowser

count = 0
urls = ['INSERT_URL_HERE']

while count < 100:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(10)
        count = count + 1

    else:
        pass

# Video tutorial on how to automate web browser opening and visiting using python script
# You can use this to open web browsers, social media posts, youtube page/video, or blog site
# to increase visitors and views

import time
import webbrowser

count = 0
urls = ['https://www.youtube.com/watch?v=xmts0wsSShU', 'https://www.youtube.com/watch?v=xhYlCQ9P94Q', 'https://techauthority.tech/2021/10/01/how-to-increase-youtube-views-using-python-script-programming-language-a-youtube-view-bot/', 'https://techauthority.tech/2021/09/18/apples-iphone-13-mini-iphone-13-iphone-13-pro-and-iphone-pro-max-tech-specs-and-new-features/', 'https://www.youtube.com/watch?v=RxriFUt5Fn0', ' https://www.youtube.com/watch?v=azC58dOm2cU', 'https://techauthority.tech/top-aeronautics-opportunities-from-nasa/', 'https://techauthority.tech/2019/08/30/learn-analytics-with-free-online-courses-by-google/']


while count < 100:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(10)
        count = count + 1

    else:
        pass

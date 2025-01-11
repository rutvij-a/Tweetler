import selenium 
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time

model = pickle.load(open("model_kiran.pkl", "rb"))
tv = pickle.load(open("tv_kiran.pkl", "rb"))

opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:9222")
driver = webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=opt)
driver.get('https://twitter.com/i/flow/login') 

# setup of login
sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("KharateBhakti")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

# password
sleep(3)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys('24092001')
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()

sleep(6)

tweets = {}
prediction_interval = 30  # set the minimum time between predictions (in seconds)
stay_threshold = 600  # set the minimum time for the user to stay on a tweet before predicting again (in seconds)

while True:
    articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    for article in articles:
        tweet_text = article.find_element(By.XPATH,".//div[@data-testid='tweetText']")
        current_text = tweet_text.get_attribute("textContent")
        if any(current_text.startswith(tweet) for tweet in tweets.keys()):
            continue
        stay_time = time() - tweets.get(current_text, 0)
        if stay_time > prediction_interval:
            post_vector = tv.transform([current_text])
            prediction = model.predict(post_vector)
            new_text = current_text + f" [{prediction[0]}]"
            driver.execute_script("arguments[0].textContent = arguments[1]", tweet_text, new_text)
            tweets[current_text] = time()
        elif stay_time > stay_threshold:
            post_vector = tv.transform([current_text])
            prediction = model.predict(post_vector)
            new_text = current_text + f" [{prediction[0]}]"
            driver.execute_script("arguments[0].textContent = arguments[1]", tweet_text, new_text)
            tweets[current_text] = time()

    # predict the replies on the page
    reply_articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    for reply_article in reply_articles:
        reply_text = reply_article.find_element(By.XPATH,".//div[@data-testid='tweetText']")
        current_reply_text = reply_text.get_attribute("textContent")
        if any(current_reply_text.startswith(reply) for reply in tweets.keys()):
            continue
        post_vector = tv.transform([current_reply_text])
        prediction = model.predict(post_vector)
        new_reply_text = current_reply_text + f" [{prediction[0]}]"
        driver.execute_script("arguments[0].textContent = arguments[1]", reply_text, new_reply_text)
        tweets[current_reply_text] = time()

    sleep(10)

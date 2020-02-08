from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

class Reddit_bot:

    def __init__(self):

        # Closing popups reqruires modifictation of driver
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")

        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })

        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://reddit.com")

    def login(self, username, password):
        sleep(2)
        login_btn = self.driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[2]/div/div[1]/a[1]')
        login_btn.click()

        # switch to login iframe
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[3]/div/div/iframe'))

        # select and input into the username and password textboxes
        username_in = self.driver.find_element_by_xpath('//*[@id="loginUsername"]')
        username_in.send_keys(username)

        password_in = self.driver.find_element_by_xpath('//*[@id="loginPassword"]')
        password_in.send_keys(password)

        sign_in = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/form/fieldset[5]/button')
        sign_in.click()

        self.driver.switch_to.default_content()
        return

    def auto_upvote(self):
        sleep(2)
        while 1:
            sleep(2)
            btns = bot.driver.find_elements_by_xpath('//*[@aria-label="upvote" and @aria-pressed="false"]')
            for i in range(len(btns)):
                if i % 2 == 0:
                    btn = btns[i]
                    print(btn)
                    btn.click()
            '''try:
                btns = bot.driver.find_elements_by_xpath('//*[@aria-label="upvote" and @aria-pressed="false"]')
                for i in range(len(btns)):
                    if i % 2 == 0:
                        btn = btns[i]
                        print(btn)
                        try:
                            btn.click()
                            print("Successful!")
                        except:
                            print("failed to click button")
            except:
                print("failed to get elements")'''


bot = Reddit_bot()
with open("SECRETS.TXT") as file:
    USERNAME = file.readline().strip()
    PASSWORD = file.readline().strip()
    print(USERNAME, PASSWORD)
    bot.login(USERNAME, PASSWORD)
bot.auto_upvote()




from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from userInfo import username, password
import os

def file_len(fname):
    i = 0
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1

class EpicBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\alexe\bin\chromedriver.exe")

    def createAccounts(self, number = 0):
        print("----- Starting account creation script -----")
        print("----- Creating " + str(number) + " accounts -----")

        for j in range(number):

            print("Creating account number: " + str(j))

            #Get current working directory
            cwd = os.getcwd()
            print("CWD:", cwd)

            firstname = "Alexander"
            lastname = "Ege"
            username = "lagbot"
            custompassword = "lagallday1"

            # Get number of accounts created
            numAccounts = file_len( cwd + "\\accounts.txt")
            print("File length:", numAccounts)

            # Create a new account name with unique number incremented
            if numAccounts < 10:
                username += "00" + str(numAccounts)
            elif numAccounts >= 10 and numAccounts < 100:
                username += "0" + str(numAccounts)
            else:
                numAccounts += numAccounts
            print("New Account: ", username)

            # Write new codename to file to keep track of existing accounts
            with open(cwd + "\\accounts.txt", "a", encoding="utf8") as output:
                output.write("\n" + username + " : " + custompassword)

            # Open EpicGames account website
            self.driver.get('https://www.epicgames.com/id/register/date-of-birth?redirect_uri=https%3A%2F%2Fwww.epicgames.com%2Faccount%3FsessionInvalidated%3Dtrue')
            sleep(2)

            # Click on Month input
            month = self.driver.find_element_by_xpath('//*[@id="month"]')
            month.click()
            sleep(1)

            # Select April
            date = self.driver.find_element_by_xpath('//*[@id="menu-"]/div[3]/ul/li[4]')
            date.click()
            sleep(1)

            # Click on Day input
            day = self.driver.find_element_by_xpath('//*[@id="day"]')
            day.click()
            sleep(1)

            # Select 28th
            myday = self.driver.find_element_by_xpath('//*[@id="menu-"]/div[3]/ul/li[28]')
            myday.click()

            # Click on Year input box
            year = self.driver.find_element_by_xpath('//*[@id="year"]')
            year.click()

            # Write in 1993
            year.send_keys(1993)
            sleep(1)

            # Click submit button
            submit = self.driver.find_element_by_xpath('//*[@id="continue"]')
            submit.click()
            sleep(1)

            # Enter generic name
            name = self.driver.find_element_by_xpath('//*[@id="name"]')
            name.click()
            name.send_keys(firstname)
            lname = self.driver.find_element_by_xpath('//*[@id="lastName"]')
            lname.click()
            lname.send_keys(lastname)
            sleep(1)

            # Select DisplayName input
            displayName = self.driver.find_element_by_xpath('//*[@id="displayName"]')
            displayName.click()

            # Send current username
            displayName.send_keys(username)
            sleep(1)

            # Select Email input
            email = self.driver.find_element_by_xpath('//*[@id="email"]')
            email.click()

            # Send username @ gmail.com
            email.send_keys(username + "@gmail.com")
            sleep(1)

            # Select Password input
            print("Adding password")
            password = self.driver.find_element_by_xpath('//*[@id="password"]')
            password.click()
            sleep(1)

            # Send default password
            password.send_keys(custompassword)
            sleep(1)

            # Select terms and conditions checkmark
            checkmark = self.driver.find_element_by_xpath('//*[@id="termsOfService"]')
            checkmark.click()
            sleep(1)

            # Submit new account creation
            submitButton = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/form/div[8]')
            submitButton.click()

            sleep(60)
            print("Account Created!")

            # while True:
                
            #     sleep(2)
        
        EpicBot().reports()

    def reports(self):
        print("----- Starting reports script -----")
        cwd = os.getcwd()
        accountsFile = cwd + "\\accounts.txt"
        scoreFile = cwd + "\\score.txt"
        custompassword = "lagallday1"
        count = 0

        # Reset score file
        with open(scoreFile, "w+", encoding="utf8") as output:
            output.write("")
        
        # Update score file with accurate values
        with open(accountsFile) as f:
            for line in f:
                print("partition:", line.partition('\n')[0])
                count += 1
                username = line.partition('\n')[0]
                print("username:", username),
                print("username:", username)
                user = self.driver.get(f'https://www.fortnitescout.com/pc/{username}')
                sleep(2)
                
                try:
                    kills = self.driver.find_element_by_xpath('//*[@id="profileCardRightSide"]/div[1]/div[2]')
                    print(kills.get_attribute("innerText"))
                    kills = kills.get_attribute("innerText")
                except NoSuchElementException:
                    print("Username not found or error occurred")
                    kills = "0/0\t(0)\t--- Free To Use ---"
                with open(scoreFile, "a", encoding="utf8") as output:
                    output.write("\n" + username + ":" + kills + " : password:" + custompassword)

        print("Count:", count)
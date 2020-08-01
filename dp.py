#!/usr/bin/python3

# User class that holds the sensitive info 
class User:
    ###############
    # CONSTRUCTOR #
    ###############
    def __init__(self, user=None, passw=None, app_id=None, secret=None, request=None):
        self.m_User = user
        self.m_Pass = passw
        self.m_AppID = app_id
        self.m_Secret = secret
        self.m_Request = request
    
    ###########
    # GETTERS #
    ###########
    def getUser(self):
        return self.m_User
    def getPass(self):
        return self.m_Pass
    def getAppID(self):
        return self.m_AppID
    def getSecret(self):
        return self.m_Secret
    def getRequest(self):
        return self.m_Request

    ###########
    # SETTERS #
    ###########
    def setUser(self, user):
        self.m_User = user
    def setPass(self, passw):
        self.m_Pass = passw
    def setAppID(self, app_id):
        self.m_AppID = app_id
    def setSecret(self, secret):
        self.m_Secret = secret
    def setRequest(self, request):
        self.m_Request = request


import configparser as cfg
import requests, json, praw, pandas, argparse, random, os

# Parsing the sensitive info from the sensitive.ini file
def sensitive_info(user):
    conf = cfg.ConfigParser()
    conf.read("sensitive.ini")

    user.setUser(conf["User Info"]["user"])
    user.setPass(conf["User Info"]["password"])
    user.setAppID(conf["Secret Key"]["app_id"])
    user.setSecret(conf["Secret Key"]["secret"])

# Creating a token for the user
def request_token(user):
    reddit = praw.Reddit(client_id=user.getAppID(), \
                            client_secret=user.getSecret(), \
                            user_agent="dailyprogrammer_downloader", \
                            username=user.getUser(), \
                            password=user.getPass())
    user.setRequest(reddit)

def submission_info(sub, num, diff):
    search = sub.search("#" + str(num) + " " + diff, limit=1)

    # Can't just return the search cause it is an object, so this kinda bypasses it
    for sub in search:
        return sub

# This method aims to print the text to the console
def print_output(text):
    print(text)

def create_dir():
    if not os.path.isdir("challenges/"):
        os.makedirs("challenges/")

def save_sub(num, diff, text):
    create_dir()
    path = str(num)+diff+".txt"

    with open("challenges/"+path, 'w') as f:
        f.write(text)
        



def main():
    # Arguments that can be passed to the program
    arg = argparse.ArgumentParser()
    arg.add_argument("-n", "--number", required=True, help="Input a number for a challenge")
    arg.add_argument("-d", "--difficulty", required=True, help="Input a difficulty (easy/intermediate/hard)")

    # Parse the arguments
    parsed = arg.parse_args()
    num = parsed.number
    diff = parsed.difficulty

    if num in ['random', 'rand']:
        num = random.randint(1, 300)

    # Creating the User object
    user = User()
    sensitive_info(user)
    request_token(user)

    # Change the subreddit to dailyprogrammer
    sub = user.getRequest().subreddit('dailyprogrammer')

    # Get the submission from the subreddit search using the id and difficulty
    submission = submission_info(sub, num, diff)

    # Output for the user
    print_output(submission.selftext)

    save_sub(num, diff, submission.selftext)





















if __name__ == "__main__":
    main()
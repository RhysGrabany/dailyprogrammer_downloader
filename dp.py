#!/usr/bin/python3

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
import requests, json, praw, pandas, argparse



def sensitive_info(user):
    conf = cfg.ConfigParser()
    conf.read("sensitive.ini")

    user.setUser(conf["User Info"]["user"])
    user.setPass(conf["User Info"]["password"])
    user.setAppID(conf["Secret Key"]["app_id"])
    user.setSecret(conf["Secret Key"]["secret"])

def request_token(user):
    reddit = praw.Reddit(client_id=user.getAppID(), \
                            client_secret=user.getSecret(), \
                            user_agent="dailyprogrammer_downloader", \
                            username=user.getUser(), \
                            password=user.getPass())
    user.setRequest(reddit)

def submission_info(sub, num, diff):
    search = sub.search("#" + str(num) + " " + diff)

    print(search)

    '''for submission in search:
        print(submission.title, submission.id)
        print(submission.selftext)
        break'''



def main():
    arg = argparse.ArgumentParser()
    arg.add_argument("-n", "--number", required=True, help="Input a number for a challenge")
    arg.add_argument("-d", "--difficulty", required=True, help="Input a difficulty (easy/intermediate/hard)")


    parsed = arg.parse_args()
    num = parsed.number
    diff = parsed.difficulty

    user = User()
    sensitive_info(user)
    request_token(user)
    sub = user.getRequest().subreddit('dailyprogrammer')

    submission_info(sub, num, diff)

















if __name__ == "__main__":
    main()
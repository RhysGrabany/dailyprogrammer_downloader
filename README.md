# Dailyprogrammer Downloader

Dailyprogrammer is a subreddit, on Reddit, where there are numerous different challenges that users can solve with their choosen language. Every language is available as long as the solution is found.

The challenges are split into three different categories that denote their difficulty to the user. And each challenge has it's own id number.

Using the Reddit API, I am able to create this downloader that can retrieve any challenge from the subreddit and you just need to give it a number and a difficulty. You can also ask for a random number and it will pull a random challenge.

Once the selected challenge has been found, the text of the post will be printed to the console, and a text document will also be created to save the challenge details.

---
This program requires the username, password, secret key, and app id to be provided in a sensitive.ini file. Seeing as this is a security risk, I do not expect anyone to actually fill this out and the code I provided can be a reference for anyone who wants to create their own version. Maybe add hashing for the sensitive material?
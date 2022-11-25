# Scrape https://www.nytimes.com/games/wordle/index.html for color and letter information:
# absent = black, present = yellow, correct = green
# browser automation
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time


def avoid_rules(page):
    # XPath for x-button:
    page.click('//html/body/div/div/dialog/div/button')


def press_letter(page, key):
    top_row = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    mid_row = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    bot_row = ['↵', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

    num = 1
    if key in mid_row: num = 2
    if key in bot_row: num = 3

    page.click(f'//html/body/div/div/div/div/div[2]/div[{num}]/button[@data-key="{key}"]')


def guess_turn(page, guess: str):
    time.sleep(2)

    # Input word
    for i in range(5):
        press_letter(page, guess[i])

    # Enter Button
    press_letter(page, '↵')


def scrape_colors(page, guess: int):
    page.is_visible('div.Tile-module_tile__3ayIZ')
    time.sleep(4)
    html = page.inner_html('//*[@id="wordle-app-game"]/div[1]/div')
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.find_all('div', class_='Tile-module_tile__3ayIZ'))


if __name__ == '__main__':
    url = "https://www.nytimes.com/games/wordle/index.html"

    # New playwright session
    with sync_playwright() as p:
        # Launch browser and page
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        # Click on x button
        avoid_rules(page)

        # Guess a letter and press enter

        guess_turn(page, "crane")  # TO DO
        scrape_colors(page, "guess")
        time.sleep(1000)

        page.close()
        browser.close()

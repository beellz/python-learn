# Download wallpapers from the https://www.uhdpaper.com/
# use Playwright and install chromium 
# use it headless to download the images 
# loop to download all images


# get the links
# get the pagination
# go to each link
# find out the 8k or 4k link
# download the image from that link

from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.uhdpaper.com/search?q=anime+girl&by-date=true&i=1")
    print(page.title())
    # page.get_by_test_id("page_body")
    # load_all = page.get_by_role(".loadM").click()
    # load_all = await page.locator("#YourId").click()
    for i in range(1, 10):
        load_all = page.get_by_text("Load More ").click()
        time.sleep(2)
        link_locators = page.locator('.blog-posts ').get_by_role('link').all()
        for _ in link_locators:
            print(_.get_attribute('href'))
            file1 = open("myfile.txt", "a")  # append mode
            file1.write(_.get_attribute('href') + "\n" )
            file1.close()


    time.sleep(5)
    browser.close()

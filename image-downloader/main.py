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

def check_link_in_file(file_path, link):
    with open(file_path, 'r') as file:
        for line in file:
            if link in line:
                return True
    return False

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.uhdpaper.com/search?q=anime+girl&by-date=true&i=0")
    print(page.title())
    for i in range(1, 20):
        load_all = page.get_by_text("Load More ").click()
        time.sleep(2)
        link_locators = page.locator('.blog-posts ').get_by_role('link').all()
        for links in link_locators:
            get_all = (links.get_attribute('href'))
            file_path = "myfile.txt"
            if check_link_in_file(file_path, get_all):
                # print(f"The link '{get_all}' exists in the file.")
                continue
            else:
                print(f"The link '{get_all}' does not exist in the file.")
                file1 = open("myfile.txt", "a")  # append mode
                file1.write(links.get_attribute('href') + "\n" )
                file1.close()
            #print(get_all)
        

    time.sleep(5)
    browser.close()




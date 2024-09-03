#sorting movies and tv series

# sending api request to imdbi 
# getting resposne and comparing the os.dir to change it depending upon reposne




import requests

url = "https://api.themoviedb.org/3/search/multi?query=lord&of&war&include_adult=false&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZWVmZDM1M2QyMDMyODIyYjY2N2MyZjIxYTk4MzhjZSIsIm5iZiI6MTcyNTAxMzY2MS43ODE4ODQsInN1YiI6IjY0ODJmM2YwYmYzMWYyNTA1NWEwMDRkMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7zygX19zp682a-kbqWcJj9jQWKCLsv5y6netKpf_IZk"
}

response = requests.get(url, headers=headers)

print(response.text)
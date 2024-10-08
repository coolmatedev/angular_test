
import json
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup 
# url = "https://gist.github.com/jvani/57200744e1567f33041130840326d488"
# urs = " https://firststop.sos.nd.gov/search/business"
# data = []
# imageUrl = ''
# def getdata(url): 
# 	r = requests.get(url) 
# 	return r.text 
	
# # htmldata = getdata("https://www.geeksforgeeks.org/") 
# htmldata = getdata(url) 
# soup = BeautifulSoup(htmldata, 'html.parser') 
# print(soup)
# i = 0
# for item in soup.find_all('img'):
#     i += 1
#     img_src = item.get('src')  # Using .get() to avoid KeyError if 'src' is missing
#     data.append({
#         'img_src': img_src,
#         # 'description': item.get('alt')  # Uncomment if you want to add alt text
#     })
#     if i == 2:
#         imageUrl = img_src
#     # print(img_src)  # Print the image source
# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)
# # print
# # Print the collected data
# response = requests.get(imageUrl)
# image_data = response.content

# # Load the image into Pillow
# image = Image.open(BytesIO(image_data))

# # Display the image
# image.show()
# print(imageUrl)
api_url = 'https://firststop.sos.nd.gov/api/Records/businesssearch'

payLoad = {'SEARCH_VALUE': "X", 'STARTS_WITH_YN': "true", 'ACTIVE_ONLY_YN': True}

# Fetch data from API

try:
	response = requests.post(api_url, json=payLoad, timeout=30)  # Increase timeout to 30 seconds
	response.raise_for_status()  # Check for HTTP errors
	data = response.json()  # Process the JSON response
except requests.exceptions.RequestException as e:
	print(f"Request failed: {e}")
print(data)

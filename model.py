import requests

#this function should return a string that is the link to the giphy image based on user input (query)
def getImageUrlFrom(query):
    #GIPHY search URL with dynamic query 
    #(f in front of string in Python creates a formatted string that you can include variables with in {}.
    #This is potentially cleaner then using the + for concantenation)
    giphy_get = f"https://api.giphy.com/v1/gifs/search?api_key=LLbmPKaorNSdpO3G3qhqduUS3u7HzxDZ&q={query}&limit=25&offset=0&rating=g&lang=en"
    #converts data into json data structure
    response = requests.get(giphy_get).json()
    #if condition returns first giphy result if there is at least one result
    if len(response["data"]) > 0:
    #url after analyzing nested json structure of response
        url = response["data"][0]["images"]["fixed_height"]["url"]
        return url
    #else condition deals with possibility user query returns no GIPHY results
    else:
        no_results_img_link = "https://unbxd.com/wp-content/uploads/2014/02/No-results-found.jpg"
        return no_results_img_link
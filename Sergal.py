import requests

def sergal(url, value):
  ### sergal(url of the Episode, Value is max pages)
    for x in range(value+1):
        i = "{0:03}".format(x) #formats to 3 decimals for the URL
        interUrl = url + i + "s.png" #URL to the 

        response = requests.get(interUrl) #Go to URL

        file = open(interUrl.replace("https://vilous.net/wp-content/uploads/comics/",""), "wb") #Filename is now ge{Episode Number}-{}
        file.write(response.content) #Dump image data
        file.close()

        print(interUrl)
    print("----- END -----")

def main():
    sergal("https://vilous.net/wp-content/uploads/comics/ge001-", 8) #Episode 1
    sergal("https://vilous.net/wp-content/uploads/comics/ge002-", 27) #Episode 2
    sergal("https://vilous.net/wp-content/uploads/comics/ge003-", 54) #Episode 3
    sergal("https://vilous.net/wp-content/uploads/comics/ge004-", 146) #Episode 4
    print("----- Download Completed -----") #Finished Dowloading
main()

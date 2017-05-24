import requests, os, bs4, shutil

#url = 'https://store.xkcd.com/collections/posters' # starting rule
url = "http://www.amazon.in/s/ref=lp_1376518031_nr_n_0?fst=as%3Aoff&rh=n%3A976460031%2Cn%3A%21976461031%2Cn%3A1376518031%2Cn%3A1376528031&bbn=1376518031&ie=UTF8&qid=1495206407&rnid=1376518031"
if not os.path.exists('newegg'):
    os.makedirs('newegg') # store comics in ./xkcd

    # Download the page
print('Downloading the page %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")


# Find the URL of the comic image
comicElem = soup.findAll("img")

if comicElem == []:
    print('Could not find comic image.')

else:
    co = comicElem[0]
    i=1

    for co in comicElem:
        i = str(i)
        comicURL = co.get('src')
        comicName = co.get('alt')
        comicName =str(comicName)
        print(comicURL+"::::::"+comicName)
        response = requests.get(comicURL, stream=True)
        with open("newegg/img"+i+".jpg", 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        i = int(i)
        i = i + 1


print('Done.')



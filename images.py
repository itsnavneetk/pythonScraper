import requests, os, bs4, shutil

#url = 'https://store.xkcd.com/collections/posters' # starting rule
url = "http://www.amazon.in/b/ref=s9_acss_bw_cg_HSBeq_1b1_w?node=4068583031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=193W2KEW60KDGSHEEM2A&pf_rd_t=101&pf_rd_p=53342ee5-cd3b-4b6d-a9f9-166e51a78acc&pf_rd_i=976416031"
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



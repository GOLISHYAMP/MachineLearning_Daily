# Create a URL shorter code 
import pyshorteners

def short_url(url):
    short = pyshorteners.Shortener()
    print(short.available_shorteners)
    print(f"tinyurl : {short.tinyurl.short(url)}")
    # print(f"adfly : {short.adfly.short(url)}")    # For this to work you need API key so since we dont have so not using it!

    

url = 'https://www.youtube.com/watch?v=-_39f2oQJMA&list=PLVG0Zju2HPJc_djazvkvbRfKlrkQ1Wl-r&index=29'
short_url(url)
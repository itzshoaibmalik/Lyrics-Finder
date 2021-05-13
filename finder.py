"""
[LYRICS FINDER]

Coded by Shoaib Malik
"""
#######################################################################################################################
# Small Guide / Documentation
#######################################################################################################################
"""
Just input the songs name you want to find lyrics. Mentioning the artist name is recommended! You can enter in any way
just like you search on Google or YouTube, it has got no such limitations. :), also string case doesn't matter, write 
in upper, lower, any case.
Examples:
    Another Life Lucas and Steve
    Lucas and Steve Another Life
    Lucas and Steve - Another Life
    Shape of you
    shape of you ed sheeran
    Ed sheeran castle on the hill
    blinding lights
    Alone Marshmello
    Way Back Home To You
You can just do in any way, just sometimes it messes up when artist name is not mentioned. ):
Try to be as much as specific and clear you can.

Recommended format: [Artist here] - [Title here]

"""
#######################################################################################################################
"""
NOTES / Troubleshoot:
    >>> If this is not your requested track's lyrics, then I'm sorry, please try again mentioning the artist's "
      name. 
    >>> If you enters any album name, then it might show lyrics of any other song or the first or most streamed song of 
      the album. 
    >>> If you forgot song name and remembered any line of it, then you might try with it too. Sometimes it works, try 
      with artist name too, if only a line doesn't works.
    >>> Check Typo
    >>> If still not getting proper results, make sure the song is famous or you gave enough details if not popular.
    >>> Sometimes it might not give results, if not listed on web, then please lemme know so that I can modify the code,
      by telling me the track name and artist in the comments or DM.
    >>> Make sure the track has also got lyrics and not only music.
    >>> But in any condition if none work, please lemme know the details!
    >>> Try to use the recommended format.
    >>> Sometimes it doesn't work if there are multiple artists. So let me know so that I can improve the code.
    """
#######################################################################################################################
"""
If you feels anything you wanna ask about this code or have faced any issue or any stuff, feel free to DM if I don't 
reply in Comments! :)


Aaand you can shorten, modify or use the code but please ask for permission before use and give proper credits with links....
"""
#######################################################################################################################
# FINAL CODE
#######################################################################################################################


import urllib.request
from abc import ABC
import re
from urllib.request import urlopen
from html.parser import HTMLParser
import json


def footer():
    print("\n\n\n")
    print("Created By: Shoaib Malik")
    print()
    print()
    print("This wasn't the song you were finding?")
    print("    Please try again mentioning the artist's name, or check the TYPO.")
    print("    If you enters any album name, then it might show lyrics of any other song or the first or most \n "
          "streamed song of the album.")
    print("    If you forgot song name and remembered any line of it, then you might try with it too. Sometimes it\n "
          "works, try with artist name too, if only a line doesn't works.")
    print("    If still didn't worked, then please let me know in the comments, with the track name and artist. If I\n "
          "don't reply there, then feel free to DM me.")
    print("    Read troubleshoot part in the top of the code!")
    print("\n\n\n")


def trouble():
    print("\n\n\n\n")
    print("Seems Like Something Went Wrong, Sorry! Please try again with any other track and lemme know the name of\n "
          "the track and the artist you searched for, so that I can fix it. You can comment or DM me if I don't \n "
          "reply in the comments.")
    print("----------OR----------")
    print("This wasn't the song you were finding?")
    print("    Please try again mentioning the artist's name, or check the TYPO.")
    print("    If you enters any album name, then it might show lyrics of any other song or the first or most \n "
          "streamed song of the album.")
    print("    If you forgot song name and remembered any line of it, then you might try with it too. Sometimes it\n "
          "works, try with artist name too, if only a line doesn't works.")
    print("    Read troubleshoot part in the top of the code!")
    print("\n\n\n\n")


def search_for():
    print()
    print()
    search = input("What track? Please say track's name (Or any line): ")
    print(search)
    if search.isspace() == True or search == "":
        print("No track name found! Please run again by entering the correct name.")
        exit()
    query = search.replace("&", "and").replace("by", "-").replace(" ", "%20")
    return query


access_token = "tEpvGb9pMzcL_EVu7CKeTXXr_V9OAB5SKib16UbJry6HnnrjK84F-dkvd26lrTcq"
url = "https://api.genius.com/search?access_token=" + access_token + "&q=" + search_for()
print()
print("Please wait... Finding your given track's details from the servers... ")
details = urllib.request.urlopen(url).read().decode()
json_results = json.loads(details)
full_title = str(json_results["response"]["hits"][0]["result"]["full_title"])
main_artist = str(json_results["response"]["hits"][0]["result"]["primary_artist"]["name"])
main_track_name = str(json_results["response"]["hits"][0]["result"]["title"])
full_track_name = str(json_results["response"]["hits"][0]["result"]["title_with_featured"])
# print(json_results["response"]["hits"][0]["result"])
# genius_url = str(json_results["response"]["hits"][0]["result"]["url"])
print("Details Found!")
print("Please wait... Trying to fetch lyrics for " + full_title + "... ")

search_artist1 = main_artist.replace("&", ",").replace("vs", ",").split(",")
# print(search_artist1)

search_track2 = main_track_name.lower()

# -------------------------------------------------------
search_track = search_track2.replace("tiësto", "tisto")
if search_track2 == "i could be the one":
    search_track = "I could be the one (stranger)"
# -------------------------------------------------------

search_artist = search_artist1[0].replace("the", "").replace("The", "").replace(" ", "").replace("-", "").replace("&",
                                                                                                                  "").replace(
    ".", "").replace(",", "").replace("/", "").replace("!", "").replace("?", "").lower()
search_track1 = search_track.replace("​", "").replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace(".",
                                                                                                         "").replace(
    ",", "").replace("/", "").replace("!", "").replace("?", "").replace("'", "").replace("’", "").replace("#", "").lower()

# -----------------Correction Part-------------------------
if search_artist == "tungevaag":
    search_artist = "martintungevaag"
if search_artist == "tiësto":
    search_artist = "tiesto"
if search_artist == "axwellλingrosso":
    search_artist = "axwellingrosso"
if search_artist1[0] == "Lucas " and search_artist1[1] == " Steve":
    search_artist = "lucassteve"
if search_artist1[0] == '\u200bdeadmau5':
    search_artist = "deadmau5"
if search_artist1[0] == "VIZE" and search_artist1[1] == " Alan Walker " and search_artist1[2] == " Edward Artemyev":
    search_artist = "alanwalker"
if search_artist == "fatrat":
    search_artist = "thefatrat"
if search_artist1[0] == 'Dimitri Vegas ' and search_artist1[1] == ' Like Mike':
    search_artist = "dimitrivegaslikemike"
# -----------------Correction Part-------------------------
# print(search_artist)

# print("https://www.azlyrics.com/lyrics/" + search_artist + "/" + search_track1 + ".html")
try:
    lyrics_find_url = "https://www.azlyrics.com/lyrics/" + search_artist + "/" + search_track1 + ".html"
    # ---------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------
    lyrics_data = str(urlopen(lyrics_find_url).read())


    class ParseHTML(HTMLParser, ABC):
        def __init__(self):
            super().__init__()
            self.p = False
            self.pbuf = []

        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if tag == "div" and not attrs:
                self.p = True
                self.pbuf = []

        def handle_endtag(self, tag):
            if tag == "div" and self.p:
                self.p = False
                print("\n".join(self.pbuf), flush=1)
                self.pbuf = []

        def handle_data(self, data):
            if self.p:
                data = data.replace("\\n", "\n")
                data = data.replace("\\", "")
                data = re.sub(r'\br\b', '', data)
                self.pbuf.append(data.strip())


    print("Lyrics Found! Here you go... :)")
    print("\n\n\n\n")
    print("--------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------")
    print("[About:] ")
    print()
    print("Full Title - ", full_title)
    print("Primary Artist / s - ", main_artist)
    print("Track Name - ", main_track_name)
    print("Track Name [Featured] - ", full_track_name)
    print("\n")
    print("--------------------------------------------------------------------------")
    print("[Lyrics:] ")
    html_parser = ParseHTML().feed(lyrics_data)
    print("\n")
    print("--------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------")
    footer()
except:
    trouble()

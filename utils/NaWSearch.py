from bs4 import BeautifulSoup
from urlextract import URLExtract
from utils import FactionUpgrades

import re
import datetime
import requests

badSubstrings = ["", "Cost", "Effect", "Formula", "Mercenary Template", "Requirement", "Gem Grinder and Dragon's "
                "Breath Formula", 'Formula: ', 'Requirements', 'Challenge']


def Embedformat(lst: list, factionUpgrade=None):
    """Formats the list retrieved from BeautifulSoup"""

    # First line always return an url - we want to get the URL only for the thumbnail
    url = lst[0]
    extractor = URLExtract()
    newUrl = extractor.find_urls(url)
    lst[0] = newUrl[0]

    # We add the faction upgrade name to the list so embed can refer to this
    if factionUpgrade is not None:
        lst.insert(1, factionUpgrade)

    # For 10-12 upgrades, we want Cost to be first after Requirement, to look nice in Embed
    if lst[3].startswith('Requirement'):
        old = lst[3]
        new = lst[4]
        lst[3] = new
        lst[4] = old

    # Cleanup in case bad stuff goes through somehow
    for line in lst[3:]:
        if line in badSubstrings:
            lst.remove(line)

        # Notes are not really important for the embed
        if line.startswith("Note") or line.startswith("Tip"):
            lst.remove(line)

    # A little extra for Djinn 8 - show current UTC time and odd/even day
    if factionUpgrade == "Flashy Storm":
        utc_dt = datetime.datetime.utcnow()
        day = int(utc_dt.strftime("%d"))
        dj8 = ""
        if day % 2 == 0:
            dj8 = ", Odd-tier Day"
        elif day % 2 == 1:
            dj8 = ", Even-tier Day"

        lst.append(f'Current Time (UTC): {utc_dt.strftime("%H:%M")}' + dj8)

    # A little less for the Druid Challenges reward - remove picture from lst
    if factionUpgrade == "Primal Balance":
        lst.remove(lst[5])

    return lst


def factionUpgrade(faction):
    # Getting the Upgrade from FactionUpgrades
    factionUpgrade = FactionUpgrades.getFactionUpgradeName(faction)

    # Retrieving data using Request and converting to BeautifulSoup object
    nawLink = "http://musicfamily.org/realm/FactionUpgrades/"
    content = requests.get(nawLink)
    soup = BeautifulSoup(content.content, 'html5lib')

    # Searching tags starting with <p>, which upgrades' lines on NaW begin with
    p = soup.find_all('p')

    # Our upgrade info will be added here
    factionUpgradeEmbed = []

    # Iterating through p, finding until upgrade matches
    for tag in p:
        # space is necessary because there is always one after image
        if tag.get_text() == " " + factionUpgrade:
            # if True, adds full line so we can retrieve the image through our formatting function
            factionUpgradeEmbed.append(str(tag))

            # Since we return true, we search using find_all_next function, and then break it there since we don't
            # need to iterate anymore at the end
            for line in tag.find_all_next(['p', 'br', 'hr', 'div']):
                # Not-a-Wiki stops lines after a break, a new line, or div, so we know the upgrade info stop there
                if str(line) in ["<br/>", "<hr/>"] or str(line).startswith("<div"):
                    break
                else:
                    # Otherwise, add the lines of upgrade to the list - line.text returns the text without HTML tags
                    factionUpgradeEmbed.append(line.text)
            break

    # Then we run the list through a formatter, and that becomes our new list
    return Embedformat(factionUpgradeEmbed, factionUpgrade)


def challenge(faction):
    # Retrieving data using Request and converting to BeautifulSoup object
    nawLink = "http://musicfamily.org/realm/Challenges/"
    content = requests.get(nawLink)
    soup = BeautifulSoup(content.content, 'html5lib')

    # Searching tags starting with <area>, which challenges' lines on NaW begin with
    p = soup.find_all('area')

    # Our upgrade info will be added here
    challengeEmbed = []

    find = False
    # Iterating through p, finding until upgrade matches
    for tag in p:
        if faction in tag['href']:
            temp = tag['research'].split("</p>")
            # The following is to convert tag['research'] into a format that the format() function will work with
            temp = [re.sub("<p>|<b>|</b>|\n|\t", "", s) for s in temp]
            temp.insert(0, temp[1])
            temp.remove(temp[2])
            challengeEmbed = temp
            find = True

    if not find:
        raise Exception("Invalid Input")

    old = challengeEmbed[0]
    new = challengeEmbed[1]
    challengeEmbed[0] = new
    challengeEmbed[1] = old

    # Then we run the list through a formatter, and that becomes our new list
    challengeName = challengeEmbed[0].split("> ")
    return Embedformat(challengeEmbed, challengeName[1])


def research(research):
    # Yummy soup stuff
    nawLink = "http://musicfamily.org/realm/Researchtree/"
    content = requests.get(nawLink)
    soup = BeautifulSoup(content.content, 'html5lib')

    # Researches begin using area, so we get all of them directly here
    p = soup.find_all('area')

    for tag in p:
        # Adding a space at the end avoids jumping checks like "S1" and "S10" for example due to startswith() function
        if tag['research'].startswith(research + " "):
            # Splitting into a list. We want it to look as below:
            # <shorthand>, <for Faction>, <research Name>, <Requirements (optional)>, <Cost>, <Effect>
            researchContents = []
            for line in tag['research'].split("\n"):
                line = line.strip('\n')
                researchContents.append(line)
            break

    #special exception for these researches due to NaW's additive/multiplicative formulas
    if research in ['C5375','E5375']:
        researchContents[-2] = researchContents[-2].strip()
        researchContents[-3] = researchContents[-3].strip()
        researchContents.remove(researchContents[-4])

    # Bad strings are bad
    researchEmbed = [re.sub("|<p>|<b>|</b>|\n|\t|</p>", "", s) for s in researchContents]
    for string in badSubstrings:
        if string in researchEmbed:
            researchEmbed.remove(string)

    # Splitting contents, switching around, prettifying embeds
    original = researchEmbed[0].split(' - ')
    researchEmbed[0] = original[0]
    researchEmbed.insert(1, original[1])
    researchName = researchEmbed[2].split(": ")
    researchEmbed[2] = researchName[1]

    return researchEmbed


def lineage(faction, perk):
    # Yummy soup stuff!
    nawLink = "http://musicfamily.org/realm/Lineages/"
    content = requests.get(nawLink)
    soup = BeautifulSoup(content.content, 'html5lib')

    # Our list to send for Embeding
    lineageEmbed = []

    # Begin Soup search
    p = soup.find_all(['p'])

    # Assuming perk is none, then return base Lineage effect
    if perk is None:
        for tag in p:
            if tag.get_text() == f' {faction} Lineage':
                extractor = URLExtract()
                newUrl = extractor.find_urls(str(tag))
                lineageEmbed.append(newUrl[0])
                for line in tag.find_all_next():
                    if str(line) == '<br/>':
                        break
                    else:
                        lineageEmbed.append(line.text)
    # Otherwise, gets the Perk information
    else:
        for tag in p:
            if tag.get_text() == f' {faction} Perk {perk}':
                extractor = URLExtract()
                newUrl = extractor.find_urls(str(tag))
                lineageEmbed.append(newUrl[0])
                for line in tag.find_all_next():
                    if str(line) in ['<br/>', '<hr/>']:
                        break
                    else:
                        lineageEmbed.append(line.text)

    # Rare case, hopefully the original embed function should handle it though
    if not lineageEmbed:
        raise Exception("Invalid Input")

    for i in badSubstrings:
        for j in lineageEmbed:
            if i == j:
                lineageEmbed.remove(i)

    lineageEmbed[1] = lineageEmbed[1].strip()

    return lineageEmbed
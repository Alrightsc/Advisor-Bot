from bs4 import BeautifulSoup
from urlextract import URLExtract
from utils import FactionUpgrades

import re
import datetime
import requests

badSubstrings = ["", "Cost", 'Effect', "Formula", "Mercenary Template", "Requirement", "Gem Grinder and Dragon's "
                "Breath Formula", 'Formula: ', 'Requirements', 'Challenge', 'Note', 'Effect', 'Tier 4 Formula',
                 'Tier 7 Formula', 'A3+ Formula', 'A3+ Effect', 'Formula', 'Ascension Penalty Reduction Formula',
                 'Production Formula', 'Additive Formula', 'Multiplicative Formula']

def stringCleaner(embed: list):
    for line in embed:
        if line in badSubstrings:
            embed.remove(line)

    return embed

def getImageUrl(line: str):
    extractor = URLExtract()
    url = extractor.find_urls(line)
    return url[0]

def factionUpgrade(faction):
    # Getting the Upgrade from FactionUpgrades
    factionUpgrade = FactionUpgrades.getFactionUpgradeName(faction)

    # Retrieving data using Request and converting to BeautifulSoup object
    nawLink = "http://musicfamily.org/realm/FactionUpgrades/"
    content = requests.get(nawLink)
    soup = BeautifulSoup(content.content, 'html.parser')

    # Searching tags starting with <p>, which upgrades' lines on NaW begin with
    p = soup.find_all('p')

    # Our upgrade info will be added here
    factionUpgradeEmbed = []

    # Iterating through p, finding until upgrade matches
    for tag in p:
        # space is necessary because there is always one after image
        if tag.get_text() == " " + factionUpgrade:
            for line in tag.find_all_next():
                # Not-a-Wiki stops lines after a break, a new line, or div, so we know the upgrade info stop there
                if str(line) in ["<br/>", "<hr/>", '<br/>'] or str(line).startswith("<div"):
                    break
                else:
                    # Otherwise, add the lines of upgrade to the list - line.text returns the text without HTML tags
                    factionUpgradeEmbed.append(str(line))
            break

    # Cleaning up the tags
    factionUpgradeEmbed = [re.sub("|<p>|<b>|</b>|\n|\t|</p>", "", s) for s in factionUpgradeEmbed]
    factionUpgradeEmbed[0] = getImageUrl(factionUpgradeEmbed[0])
    factionUpgradeEmbed[1] = factionUpgrade

    if factionUpgrade == "Flashy Storm":
        utc_dt = datetime.datetime.utcnow()
        day = int(utc_dt.strftime("%d"))
        dj8 = ""
        if day % 2 == 0:
            dj8 = ", Odd-tier Day"
        elif day % 2 == 1:
            dj8 = ", Even-tier Day"

        factionUpgradeEmbed.append(f'Current Time (UTC): {utc_dt.strftime("%H:%M")}' + dj8)

    return stringCleaner(factionUpgradeEmbed)


def challenge(faction):
    # Retrieving data using Request and converting to BeautifulSoup object
    nawLink = "http://musicfamily.org/realm/Challenges/"
    content = requests.get(nawLink)
    soup = BeautifulSoup(content.content, 'html.parser')

    # Searching tags starting with <area>, which challenges' lines on NaW begin with
    p = soup.find_all('area')

    # Our upgrade info will be added here
    challengeEmbed = []

    # Iterating through p, finding until upgrade matches
    for tag in p:
        if faction in tag['href']:
            challengeEmbed = tag['research'].split("</p>")
            # The following is to convert tag['research'] into a format that the format() function will work with
            break

    # CLeaning up the list
    challengeEmbed = [re.sub("<p>|<b>|</b>|\n|\t", "", s) for s in challengeEmbed]
    challengeEmbed[0] = challengeEmbed[0] + ": " + challengeEmbed[1].split("> ")[1]
    challengeEmbed[1] = getImageUrl(challengeEmbed[1])
    challengeEmbed[0], challengeEmbed[1] = challengeEmbed[1], challengeEmbed[0]

    if faction[-1] == "R":
        challengeEmbed[1] = challengeEmbed[1].split(": ")[1]
    else:
        challengeEmbed.remove(challengeEmbed[2])

    if faction == "DruidDCR":
        challengeEmbed.remove(challengeEmbed[4])

    return stringCleaner(challengeEmbed)

def research(research):
    # Yummy soup stuff
    nawLink = "http://musicfamily.org/realm/Researchtree/"
    content = requests.get(nawLink)
    soup = BeautifulSoup(content.content, 'html.parser')

    # Researches begin using area, so we get all of them directly here
    p = soup.find_all('area')
    researchContents = []

    for tag in p:
        # Adding a space at the end avoids jumping checks like "S1" and "S10" for example due to startswith() function
        if tag['research'].startswith(research + " ") or tag['research'].startswith("<p><b>" + research):
            # Splitting into a list. We want it to look as below:
            # <shorthand>, <for Faction>, <research Name>, <Requirements (optional)>, <Cost>, <Effect>
            for line in tag['research'].split("\n"):
                line = line.strip('\n')
                researchContents.append(line)
            break

    if not researchContents:
        raise Exception("Invalid Input")

    #special exception for these researches due to NaW's additive/multiplicative formulas
    if research in ['C5375','E5375']:
        researchContents[-2] = researchContents[-2].strip()
        researchContents[-3] = researchContents[-3].strip()
        researchContents.remove(researchContents[-4])

    # Bad strings are bad
    researchEmbed = [re.sub("|<p>|<b>|</b>|\n|\t|</p>", "", s) for s in researchContents]

    # Splitting contents, switching around, prettifying embeds
    original = researchEmbed[0].split(' - ')
    researchEmbed[0] = original[0]
    researchEmbed.insert(1, original[1])
    researchName = researchEmbed[2].split(": ")
    researchEmbed[2] = researchName[1]

    return stringCleaner(researchEmbed)


def lineage(faction, perk):
    # Yummy soup stuff!
    nawLink = "http://musicfamily.org/realm/Lineages/"
    content = requests.get(nawLink)
    soup = BeautifulSoup(content.content, 'html.parser')

    # Our list to send for Embeding
    lineageEmbed = []

    # Begin Soup search
    p = soup.find_all(['p'])

    # Assuming perk is none, then return base Lineage effect
    if perk is None:
        for tag in p:
            if tag.get_text() == f' {faction} Lineage':
                lineageEmbed.append(getImageUrl(str(tag)))
                for line in tag.find_all_next():
                    if str(line) == '<br/>':
                        break
                    else:
                        lineageEmbed.append(line.text)
    # Otherwise, gets the Perk information
    else:
        for tag in p:
            if tag.get_text() == f' {faction} Perk {perk}':
                lineageEmbed.append(getImageUrl(str(tag)))
                for line in tag.find_all_next():
                    if str(line) in ['<br/>', '<hr/>']:
                        break
                    else:
                        lineageEmbed.append(line.text)

    # Rare case, hopefully the original embed function should handle it though
    if not lineageEmbed:
        raise Exception("Invalid Input")

    lineageEmbed[1] = lineageEmbed[1].strip()

    return stringCleaner(lineageEmbed)

def artifactSearch(artifact):
    artList = FactionUpgrades.fastArtifactSearch(artifact)
    if len(artList) != 1:
        return artList, False
    else:
        artifact = artList[0]

    nawLink = "http://musicfamily.org/realm/Artifacts/"
    content = requests.get(nawLink)
    soup = BeautifulSoup(content.content, 'html.parser')

    artifactContents = []
    artifactEmbed = []
    p = soup.find_all('area')

    for tag in p:
        if (artifact + "</b>") in tag['research']:
            artifactContents = tag['research'].split("\n")
            break

    artifactContents = [re.sub("|<p>|<b>|</b>|\n|\t|</p>", "", s) for s in artifactContents]
    for line in artifactContents:
        artifactEmbed.append(line.strip())

    artifactEmbed.insert(0, getImageUrl(artifactEmbed[0]))
    artifactEmbed[1] = artifactEmbed[1].split("> ")[1]

    if artifact in ['Duskstone', 'Dawnstone']:
        artifactEmbed.remove(artifactEmbed[-1])

    return stringCleaner(artifactEmbed), True

def bloodline(bloodline):
    nawLink = "http://musicfamily.org/realm/Bloodline/"
    content = requests.get(nawLink)
    soup = BeautifulSoup(content.content, 'html.parser')

    bloodlineContents = []
    p = soup.find('p', attrs={'id' : bloodline})

    bloodlineContents.append(str(p))
    for tag in p.find_all_next():
        if str(tag) in ['<hr/>', '<br/>'] or str(tag).startswith("<div"):
            break
        else:
            bloodlineContents.append(tag.get_text())

    bloodlineEmbed = [re.sub("|<p>|<b>|</b>|\n|\t|</p>", "", s) for s in bloodlineContents]
    bloodlineEmbed[0] = getImageUrl(bloodlineEmbed[0])

    return stringCleaner(bloodlineEmbed)

def artifactSet(faction):
    nawLink = "http://musicfamily.org/realm/ArtifactSet/"
    content = requests.get(nawLink)
    soup = BeautifulSoup(content.content, 'html.parser')

    setContents = []
    p = soup.find_all('area')

    for tag in p:
        if "#" + faction in tag['href']:
            setContents = tag['research'].split("</p>")

    setContents = [re.sub("|<p>|<b>|</b>|\n|\t|</p>", "", s) for s in setContents]
    setContents[0] = getImageUrl(setContents[0])
    setContents.insert(1, faction + " Set")

    return stringCleaner(setContents)
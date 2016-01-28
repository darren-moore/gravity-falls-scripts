#Generates automoderator schedule code for Gravity Falls "Sprint to Take Back the Falls"

titles = """Tourist Trapped - 1/6/16
The Legend of the Gobblewonker - 1/7/16
Headhunters - 1/8/16
The Hand That Rocks the Mabel - 1/9/16
The Inconveniencing - 1/10/16
Dipper vs. Manliness - 1/11/16
Double Dipper - 1/12/16
Irrational Treasure - 1/13/16
The Time Traveler's Pig - 1/14/16
Fight Fighters - 1/15/16
Little Dipper - 1/16/16
Summerween - 1/17/16
Boss Mabel - 1/18/16
Bottomless Pit - 1/19/16
The Deep End - 1/20/16
Carpet Diem - 1/21/16
Boyz Crazy - 1/22/16
Land Before Swine - 1/23/16
Dreamscaperers - 1/24/16
Gideon Rises - 1/25/16
Shorts! - 1/26/16
Scary-oke - 1/27/16
Into the Bunker - 1/28/16
The Golf War - 1/29/16
Sock Opera - 1/30/16
Soos and the Real Girl - 1/31/16
Little Gift Shop of Horrors - 2/1/16
Society of the Blind Eye - 2/2/16
Blendin's Game - 2/3/16
The Love God - 2/4/16
Northwest Mansion Mystery - 2/5/16
Not What He Seems - 2/6/16
A Tale of Two Stans - 2/7/16
Dungeons, Dungeons & more Dungeons - 2/8/16
The Stanchurian Candidate - 2/9/16
The Last Mabelcorn - 2/10/16
Roadside Attraction - 2/11/16
Dipper and Mabel vs. the Future - 2/12/16
Weirdmageddon Part 1 - 2/13/16
Weirdmageddon 2: Escape from Reality - 2/14/16
Weirdmageddon 3: TAKE BACK THE FALLS - 2/15/16"""

titlesList = titles.split("\n")
temp = []

for item in titlesList:
    temp.append(item.split(" - "))

titlesList = temp

#split to correct date
i = 0
while i < len(titlesList):
    date = titlesList[i][1].split("/")
    if int(date[1]) < 10:
        date[1] = "0"+date[1]
    
    titlesList[i][1] = "20"+date[2]+"-"+"0"+date[0]+"-"+date[1]
    i+=1
    
finalString = ""
for item in titlesList:
    finalString += "    first: \"" + item[1] + " 8:00 AM -05\"\n"
    finalString += "    sticky: 2\n"
    finalString += "    title: \"Sprint to Take Back the Falls: '" + item[0] + "'\"\n"
    finalString += """    text: |\n        [](#stanthink)As the finale looms ahead, /r/gravityfalls is rewatching the series! More info [here](https://www.reddit.com/r/gravityfalls/comments/3zfp7c/sprint_to_take_back_the_falls_a_rewatch_event/).
\n        Today we are taking another look at **\"""" + item[0] + """\"** Feel free to discuss anything, including spoilers for future episodes.\n
        [Here](http://invera.tumblr.com/gf_episodes) is a link to the episodes.\n
        You can find past discussion threads, when the episode first aired, [here](https://www.reddit.com/r/gravityfalls/wiki/threads).
"""

    finalString += "\n---\n\n"
print(finalString)
    

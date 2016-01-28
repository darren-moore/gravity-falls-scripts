#Generates CSS for Gravity Falls emotes

f = open('out', 'w')
horiz = 0
vert = 0
vertCtr = 0
emotes = ['mabel','mabelwat','mabelgoof', 'mabelevil', 'grumpymabel', 'partygurl','thumbdown',
          'pout', 'happymabel', 'distressmabel', 'mabelgum', 'mabelidk', 'cryofjoy',
          'mabelgross', 'mabelsquee', 'disapproval', 'dipmad', 'paperjam',
          'dipponder', 'dipcheer', 'dippergross', 'indianadipper', 'dipsad', 'airquote', 'dipawe', 'dipcry', 'dipslap',
          'pinescream', 'grunkle', 'stanwow', 'grunklemad', 'heraim', 'onedoesnot', 'eyebrowstan', 'icansellthis', 'trytosmile']
emotes = ['soos', 'toomuch', 'soosheart', 'wendy', 'wendyread', 'wearewomen', 'eyeroll', 'candy', 'grenda', 'mcg',
          'mcevil', 'waddles', 'waddleswag', 'noooo', 'gideon', 'gideonplan', 'usethem', 'budeon', 'budangry', 'robbie',
          'robbiesoso', 'trigger','bighenry', 'gnome', 'tad', 'muted', 'pacifiwhat', 'pacifisad', 'puppetmabel',
          'puppetdipper', 'puppetstan', 'bwaaa', 'kermit', 'mybrother', 'notimpressed','impressed', 'lookonhisface', 'stanthink',
          'fordmad', 'ducktective']
emotes = ['bill', 'angrybill', 'lotsofthings', 'billexpression', 'didyamissme', 'billdeal', 'bipper', 'bippermad', 'blindeyeguy'
          ,'getem', 'oooh', 'meowmeow', 'usausa', 'blendin']

for emote in emotes:
    f.write("a[href|='#" +emote+ "'], a[href|='#r"+emote+"']\n{\n")
    f.write("    background-position: "+str(horiz)+"px "+str(vert)+"px !important;\n}\n")
    horiz -= 70
    vertCtr += 1
    if vertCtr == 4:
        vertCtr = 0
        vert -= 70
        horiz = 0
f.close()
##import pprint
##emotes = ['mabel', 'mabelwat', 'mabelgoof', 'mabelevil', 'grumpymabel', 'partygurl'
##         , 'thumbdown', 'pout', 'happymabel', 'distressmabel', 'mabelgum', 'mabelidk'
##         , 'cryofjoy', 'mabelgross', 'mabelsquee', 'disapproval', 'dipmad', 'paperjam'
##         , 'dipponder', 'dipcheer', 'dippergross', 'indianadipper', 'dipsad', 'airquote'
##         , 'dipawe', 'dipcry', 'dipslap', 'pinescream', 'grunkle', 'stanwow', 'grunklemad'
##         , 'heraim', 'onedoesnot', 'eyebrowstan', 'icansellthis', 'trytosmile', 'soos'
##         , 'toomuch', 'soosheart', 'wendy', 'wendyread', 'wearewomen', 'eyeroll', 'candy'
##         , 'grenda', 'mcg', 'mcevil', 'waddles', 'waddleswag', 'noooo', 'gideon'
##         , 'gideonplan', 'usethem', 'budeon', 'budangry', 'robbie', 'robbiesoso'
##         , 'trigger','bighenry', 'gnome', 'tad', 'muted', 'pacifiwhat', 'pacifisad'
##         , 'puppetmabel', 'puppetdipper', 'puppetstan', 'bwaaa', 'kermit', 'mybrother'
##         , 'notimpressed','impressed', 'lookonhisface', 'stanthink', 'fordmad', 'ducktective'
##         , 'bill', 'angrybill', 'lotsofthings', 'billexpression', 'didyamissme', 'billdeal'
##         , 'bipper', 'bippermad', 'blindeyeguy', 'getem', 'oooh', 'meowmeow', 'usausa', 'blendin']
##pp = pprint.PrettyPrinter()
##pp.pprint(total)

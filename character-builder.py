#this was coded in python 3.9.4
'''This is the character builder, it works by creating a directory which it populates
with the character's ancestry (or in 5e language "race"), background, class, and a set
of rolled ability scores. I'm working on how it reminds of ability score increases from
ancestry, but given the derth of non +2/+1 options, we'll see how it plays out.'''

#the first part of this is the stat rolling. the randint feature simulates rolling
from random import randint

def rolling4d6dropLowest(l):  #funciton accepting argument l which will be an empty list
    for i in range(6):  #a for loop which will run 6 times, once for each final stat
        n = []  #forming empty list which randint will append d6 rolls into to simulate the four rolls
        for j in range(4):
            n.append(randint(1,6))  #rolling the four d6
        n.sort()  #sorting them low-high
        del(n[0])  #dropping the lowest
        score = sum(n[0:])  #adding up the remaining three
        l.append(score)  #adding each score to the list taken as argument for the function
    l.sort(reverse=True)  #sorting the list taken as argument for the function from high-low
    return l  #returning the list with the six scores

#ancestry uses a percentile system between common, uncommon, and rare ancestries
#rarity is based on my homebrew world, with the following percentages:
#35% human, 35% common, 20% uncommon, and 10% rare.

anc_h = ["human"]  #the first ancesty list is just human
anc_c = ["orc (VGM or ERLW or EGW)", "lizardfolk (VGM)", 'kobold (VGM)', 'hobgoblin (VGM or ERLW)',\
         'goblin (VGM or GGR or ERLW)', 'halfling (PHB or SCAG or EGW)', 'elf (PHB or MTF)', \
         'dwarf (PHB or MTF)']  #these are the common ancestires
anc_uc = ['yuan-ti pureblood (VGM)', 'triton (VGM or MOT)', 'tabaxi (VGM)', 'kenku (VGM)', 'goliath (VGM)', \
          'firbolg (VGM)', 'bugbear (VGM or ERLW)', 'tiefling (PHB or SCAG or MTF)', 'half-orc (PHB)', 'half-elf (PHB)', \
          'gnome (PHB or SCAG or MTF)', 'dragonborn (PHB)', 'dragonborn (Ravenite) (EGW)']  #these are the uncommon ancestries
anc_r = ['harengon (WBtW)', 'fairy (WBtW)', 'reborn (VRGR)', 'hexblood (VRGR)', 'dhampir (VRGR)', 'aasimar  (VGM)', \
         'custom lineage (TCE)', 'gith (githzerai) (MTF)', 'gith (githyanki) (MTF)', 'satyr (MOT)', 'minotaur (MOT or GGR)', \
         'leonin (MOT)', 'centaur (MOT or GGR)', 'vedalken (GGR)', 'simic hybrid (GGR)', 'loxodon (GGR)', 'warforged (ERLW)', \
         'shifter (ERLW)', 'kalashtar  (ERLW)', 'changeling (ERLW)', 'dragonborn (draconblood) (EGW)', 'genasi (water) (EEPC)', \
         'genasi (fire)(EEPC)', 'genasi (earth) (EEPC)', 'genasi (air) (EEPC)', 'aarakocra  (EEPC)', 'merfolk (CftD)', \
         'verdan (AI)']  #these are the rarest ancestires 

'''this next function was written to be used to pick ancestries only, hence the name; however i later incorporated it into the
background chooser, this is a lesson in scalability for sure'''
def pickInRarity(chosen_list):  #this program will help iterate within a given list and pick a random one, updated to be neutral
    y = randint(1,len(chosen_list))
    return chosen_list[y-1]  #return the item at index y-1 in the list

def choose_ancestry(char):
    x = randint(1,100)  #set x which determines the rarity of the race
    if x <= 35:  #if x is in the 1-35 range
        char["ancestry"] = pickInRarity(anc_h) #use the above function, but will return human
    elif x <= 70:  #if x is in the 36-70 range
        char["ancestry"] = pickInRarity(anc_c)
    elif x <= 90:  #if x is in the 71-90 range
        char["ancestry"] = pickInRarity(anc_uc)
    else:  #for all other situations, which is 91-100 range
        char["ancestry"] = pickInRarity(anc_r)
    return char

#classes are few, so this bit was just hammered out quickly without reference to previous code
PC_classes = ["artificer", "barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", \
              "ranger", "rogue", "sorcerer", "warlock", "wizard"]

def choose_class(char):  #there are 13 playable classes
    x = randint(0,12)  #so let's keep this part simple
    char["class"] = PC_classes[x]  #create a new item in dictionary with key "class" tied to string for the class
    return char  #return the finished new dictionary

"""backgrounds are numerous, and could vary in rarity similar to ancestries.  i considered making multiple lists like ancestries,
and may yet in the future, but for now it's just one list with the backgrounds from 5e.tools that i felt were setting-neutral enough
to work in this"""
bac_list = ['Acolyte', 'Anthropologist', 'Archaeologist', 'Charlatan', 'City Watch' 'City Watch (Investigator)', 'Clan Crafter', \
            'Cloistered Scholar', 'Courtier', 'Criminal', 'Criminal (Spy)', 'Entertainer', 'Entertainer (Gladiator)', 'Faction Agent', \
            'Far Traveler', 'Feylost', 'Fisher', 'Folk Hero', 'Guild Artisan', 'Guild Artisan (Guild Merchant)', 'Haunted One', \
            'Hermit', 'Inheritor', 'Investigator', 'Knight of the Order', 'Marine', 'Mercenary Veteran', 'Noble', 'Noble (Knight)', \
            'Outlander', 'Sage', 'Sailor', 'Sailor (Pirate)', 'Shipwright', 'Smuggler', 'Soldier', 'Tribe (Uthgardt) Member', \
            'Urban Bounty Hunter', 'Urchin', 'Capital City (Waterdhavian) Noble', 'Fey Carnival (Witchlight) Hand']

def choose_background(char):  #function to select one of the backgrounds above
    char['background'] = pickInRarity(bac_list)  #uses pickInRarity to pull a random background from the list, then drop it in at key 'background'
    return char

"""putting it all together"""
"""OLD TEXT FOR ORIGINAL INTENT: the final printed screen should look something like:
Your character's ancestry is ___, your character's background is ___, and your character's class is ___.
Your stats are [________] and from your ancestry you have [+2/+1]or[+2/+1/+1]or[+1/+1/+1] to which you may
distribute as you please. I will accomplish that by using the +2/+1 default, and then checking the few exceptions
against their string in the final directory as it prints."""

vowels = ['A','E','I','O','U','a','e','i','o','u']  #for the a/an disambiguation for backgrounds

def build_char():  #the final delivery, runs each program then prints the results to the console
    character = {"stats" : []}  #starting with almost empty dictionary for character, empty list where stats will be
    rolling4d6dropLowest(character["stats"])  #call each function to build out the character directory
    character = choose_ancestry(character)
    character = choose_class(character)
    character = choose_background(character) #done building
    #now for the final print, including a/an
    if character['ancestry'][0] in vowels:
        print("you have rolled an %s %s" % (character['ancestry'], character['class']))  #if ancestry starts with a vowel
    else:
        print("you have rolled a %s %s" % (character['ancestry'], character['class']))  #otherwise
    if character['background'][0] in vowels:  #for a/an check
        print("your character was an %s before adventuring" % (character['background']).lower())  #background list is capatalized, so lower to fix
    else:
        print("your character was a %s before adventuring" % (character['background']).lower())  #background list is capatalized, so lower to fix
    print("your ability scores are: %s" % (character['stats']))
    if character['ancestry'] == 'human':  #presuming no variant human
        print("don\'t forget your score increases: +1 to all")
    else:  #if it's not variant human
        print("don\'t forget your score increases: likely +2/+1") #after done with backgrounds, set to check human, half-elf, etc.
    print("")

#after testing, i've left it in the running thrice mode, this part can be easily modified though
print("welcome to national parks' random character generator")
print("current setting is make-three: 3 characters will be generated, have fun picking")
input("press ENTER to continue")  #just a pause really
print("")
for i in range(3):
    build_char()

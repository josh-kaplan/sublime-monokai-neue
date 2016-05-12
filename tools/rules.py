##
## https://github.com/ColibriApps/MonokaiJsonPlus
##

import itertools
import xml.dom.minidom
from itertools import permutations

# Define Colors for the 10 Levels
colors = [
    "#66D9EF", # Level 1 - Blue
    "#AE81FF", # Level 2 - Purple
    "#F92672", # Level 3 - Magenta
    "#A6E22E", # Level 4 - Green
    "#FD971F", # Level 5 - Orange
    "#E6DB74", # Level 6 - Yellow
    "#66D9EF", # Level 7 - Blue
    "#A6E22E", # Level 8 - Green
    "#E6DB74", # Level 9 - Yellow

    "#66D9EF", # Level 1 - Blue
    "#AE81FF", # Level 2 - Purple
    "#F92672", # Level 3 - Magenta
    "#A6E22E", # Level 4 - Green
    "#FD971F", # Level 5 - Orange
    "#E6DB74", # Level 6 - Yellow
    "#66D9EF", # Level 7 - Blue
    "#A6E22E", # Level 8 - Green
    "#E6DB74"  # Level 9 - Yellow

]

colors_val = [
    "#999999", # Level 1 
    "#999999", # Level 2 
    "#999999", # Level 3 
    "#999999", # Level 4
    "#999999", # Level 5 
    "#999999", # Level 6
    "#999999", # Level 7
    "#999999", # Level 8
    "#999999",
    "#999999",
    "#999999", # Level 1 
    "#999999", # Level 2 
    "#999999", # Level 3 
    "#999999", # Level 4
    "#999999", # Level 5 
    "#999999", # Level 6
    "#999999", # Level 7
    "#999999", # Level 8
    "#999999",
    "#999999"
]

# defines the placeholder values
prefix1 = "<dict><key>name</key><string>"
prefix2 = "</string><key>scope</key><string>source.json "
postfix1 = "string.quoted.double.json</string><key>settings</key><dict><key>foreground</key><string>"
postfix2 = "</string></dict></dict>"
d = "meta.structure.dictionary.json "
v = "meta.structure.dictionary.value.json "
a = "meta.structure.array.json "

# Logic to generate the required schema of dictionary key and values
def getSequenceArray(items):
    result = []
    for item in items:
        tmp_item = item[:-1]
        s = 'dv' + tmp_item.replace('d', 'dv') + item[-1:]
        result.append(s)
        if item[-1:] == 'd':
            result.append(s + 'v')
    return result

# Generate Levels
# Level 1 & 2
levels = [
    [
        "d",
        "dv"
    ],
    [
        "dvd",
        "dvdv",
        "dva"
    ]
]

# Level 3
s = set()
s.update([''.join(p) for p in permutations('dd')])
s.update([''.join(p) for p in permutations('da')])
s.update([''.join(p) for p in permutations('aa')])
levels.append(getSequenceArray(s))

# Level 4
s = set()
s.update([''.join(p) for p in permutations('ddd')])
s.update([''.join(p) for p in permutations('dda')])
s.update([''.join(p) for p in permutations('daa')])
s.update([''.join(p) for p in permutations('aaa')])
levels.append(getSequenceArray(s))

# Level 5
s = set()
s.update([''.join(p) for p in permutations('dddd')])
s.update([''.join(p) for p in permutations('ddda')])
s.update([''.join(p) for p in permutations('ddaa')])
s.update([''.join(p) for p in permutations('daaa')])
s.update([''.join(p) for p in permutations('aaaa')])
levels.append(getSequenceArray(s))

# Level 6
s = set()
s.update([''.join(p) for p in permutations('ddddd')])
s.update([''.join(p) for p in permutations('dddda')])
s.update([''.join(p) for p in permutations('dddaa')])
s.update([''.join(p) for p in permutations('ddaaa')])
s.update([''.join(p) for p in permutations('daaaa')])
s.update([''.join(p) for p in permutations('aaaaa')])
levels.append(getSequenceArray(s))

# Level 7
s = set()
s.update([''.join(p) for p in permutations('dddddd')])
s.update([''.join(p) for p in permutations('ddddda')])
s.update([''.join(p) for p in permutations('ddddaa')])
s.update([''.join(p) for p in permutations('dddaaa')])
s.update([''.join(p) for p in permutations('ddaaaa')])
s.update([''.join(p) for p in permutations('daaaaa')])
s.update([''.join(p) for p in permutations('aaaaaa')])
levels.append(getSequenceArray(s))

# Level 8
s = set()
s.update([''.join(p) for p in permutations('ddddddd')])
s.update([''.join(p) for p in permutations('dddddda')])
s.update([''.join(p) for p in permutations('dddddaa')])
s.update([''.join(p) for p in permutations('ddddaaa')])
s.update([''.join(p) for p in permutations('dddaaaa')])
s.update([''.join(p) for p in permutations('ddaaaaa')])
s.update([''.join(p) for p in permutations('daaaaaa')])
s.update([''.join(p) for p in permutations('aaaaaaa')])
levels.append(getSequenceArray(s))

# Level 9
s = set()
s.update([''.join(p) for p in permutations('dddddddd')])
s.update([''.join(p) for p in permutations('ddddddda')])
s.update([''.join(p) for p in permutations('ddddddaa')])
s.update([''.join(p) for p in permutations('dddddaaa')])
s.update([''.join(p) for p in permutations('ddddaaaa')])
s.update([''.join(p) for p in permutations('dddaaaaa')])
s.update([''.join(p) for p in permutations('ddaaaaaa')])
s.update([''.join(p) for p in permutations('daaaaaaa')])
s.update([''.join(p) for p in permutations('aaaaaaaa')])
levels.append(getSequenceArray(s))

# Level 10+
s = set()
s.update([''.join(p) for p in permutations('ddddddddd')])
s.update([''.join(p) for p in permutations('dddddddda')])
s.update([''.join(p) for p in permutations('dddddddaa')])
s.update([''.join(p) for p in permutations('ddddddaaa')])
s.update([''.join(p) for p in permutations('dddddaaaa')])
s.update([''.join(p) for p in permutations('ddddaaaaa')])
s.update([''.join(p) for p in permutations('dddaaaaaa')])
s.update([''.join(p) for p in permutations('ddaaaaaaa')])
s.update([''.join(p) for p in permutations('daaaaaaaa')])
s.update([''.join(p) for p in permutations('aaaaaaaaa')])
levels.append(getSequenceArray(s))

# Generate XML output
output = ""
for i in xrange(len(levels) - 1, -1, -1):
    level = levels[i]
    for items in level:
        result = prefix1 + "JSON - Level " + str(i + 1) + prefix2
        for item in list(items):
            if item == "d":
                result = result + d
            elif item == "v":
                result = result + v
            elif item == "a":
                result = result + a
        if item == "v" or item == "a":
            result = result + postfix1 + colors_val[i] + postfix2
        else:
            result = result + postfix1 + colors[i] + postfix2
        output = output + xml.dom.minidom.parseString(result).toprettyxml(
            indent="\t").replace("<?xml version=\"1.0\" ?>\n", "")
        
print output
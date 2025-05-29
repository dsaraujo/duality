import json
import html2text

from thefuzz import fuzz, process

data = []

with open('spells.db', 'r',encoding='utf-8') as f:
    for line in f:
        data.append(json.loads(line.strip()))


spell_durations = {
  "ArM5": {
    "label": "arm5e.sheet.source.ArM5",
    "source": "ArM5",
    "disabled": True
  },
  "moment": {
    "label": "moment",
    "dtype": "String",
    "source": "ArM5",
    "impact": 0
  },
  "conc": {
    "label": "conc",
    "dtype": "String",
    "source": "ArM5",
    "impact": 1
  },
  "diam": {
    "label": "diam",
    "dtype": "String",
    "source": "ArM5",
    "impact": 1
  },
  "sun": {
    "label": "sun",
    "dtype": "String",
    "source": "ArM5",
    "impact": 2
  },
  "ring": {
    "label": "ring",
    "dtype": "String",
    "source": "ArM5",
    "impact": 2
  },
  "moon": {
    "label": "moon",
    "dtype": "String",
    "source": "ArM5",
    "impact": 3
  },
  "year": {
    "label": "year",
    "dtype": "String",
    "source": "ArM5",
    "impact": 4
  },
  "special": {
    "label": "arm5e.spell.special",
    "dtype": "String",
    "source": "ArM5",
    "impact": 0
  },
  "faeMagic": {
    "label": "arm5e.skill.mystery.faerieMagic",
    "source": "ArM5",
    "disabled": True
  },
  "fire": {
    "label": "fire",
    "dtype": "String",
    "source": "ArM5",
    "impact": 3
  },
  "bargain": {
    "label": "bargain",
    "dtype": "String",
    "source": "ArM5",
    "impact": 3
  },
  "condition": {
    "label": "condition",
    "dtype": "String",
    "impact": 4
  },
  "year+1": {
    "label": "year+1",
    "dtype": "String",
    "source": "ArM5",
    "impact": 4
  },
  "HoH:MC": {
    "label": "arm5e.sheet.source.HoH:MC",
    "source": "HoH:MC",
    "disabled": True
  },
  "held": {
    "label": "held",
    "dtype": "String",
    "source": "HoH:MC",
    "impact": 1
  },
  "while": {
    "label": "while",
    "dtype": "String",
    "source": "HoH:MC",
    "impact": 1
  },
  "mm": {
    "label": "mm",
    "dtype": "String",
    "source": "RoP:F",
    "impact": 2
  },
  "not": {
    "label": "not",
    "dtype": "String",
    "source": "RoP:F",
    "impact": 2
  },
  "symbol": {
    "label": "symbol",
    "dtype": "String",
    "source": "RoP:F",
    "impact": 4
  },
  "hidden": {
    "label": "hidden",
    "dtype": "String",
    "source": "RoP:F",
    "impact": 4
  },
  "aura": {
    "label": "aura",
    "dtype": "String",
    "source": "RoP:F",
    "impact": 4
  },
  "RoP:D": {
    "label": "arm5e.sheet.source.RoP:D",
    "source": "RoP:D",
    "disabled": True
  },
  "recitation": {
    "label": "recitation",
    "dtype": "String",
    "source": "RoP:D",
    "impact": 1
  },
  "office": {
    "label": "office",
    "dtype": "String",
    "source": "RoP:D",
    "impact": 1
  },
  "devotion": {
    "label": "devotion",
    "dtype": "String",
    "source": "RoP:D",
    "impact": 2
  },
  "sabbath": {
    "label": "sabbath",
    "dtype": "String",
    "source": "RoP:D",
    "impact": 2
  },
  "holy40": {
    "label": "40",
    "dtype": "String",
    "source": "RoP:D",
    "impact": 3
  },
  "fast": {
    "label": "fast",
    "dtype": "String",
    "source": "RoP:D",
    "impact": 3
  },
  "grace": {
    "label": "grace",
    "dtype": "String",
    "source": "RoP:D",
    "impact": 4
  },
  "RoP:F": {
    "label": "arm5e.sheet.source.RoP:F",
    "source": "RoP:F",
    "disabled": True
  },
  "if": {
    "label": "if",
    "dtype": "String",
    "source": "RoP:F",
    "impact": 0
  },
  "focus": {
    "label": "focus",
    "dtype": "String",
    "source": "RoP:F",
    "impact": 1
  },
  "geas": {
    "label": "geas",
    "dtype": "String",
    "source": "RoP:F",
    "impact": 2
  },
  "hour+1": {
    "label": "hour+1",
    "dtype": "String",
    "source": "RoP:F",
    "impact": 2
  },
  "faerie": {
    "label": "faerie",
    "dtype": "String",
    "source": "RoP:F",
    "impact": 4
  },
  "RoP:I": {
    "label": "arm5e.sheet.source.RoP:I",
    "source": "RoP:I",
    "disabled": True
  },
  "cursed": {
    "label": "cursed",
    "dtype": "String",
    "source": "RoP:I",
    "impact": 2
  },
  "forsaken": {
    "label": "forsaken",
    "dtype": "String",
    "source": "RoP:I",
    "impact": 4
  },
  "RoP:M": {
    "label": "arm5e.sheet.source.RoP:M",
    "source": "RoP:M",
    "disabled": True
  },
  "storm": {
    "label": "storm",
    "dtype": "String",
    "source": "RoP:M",
    "impact": 1
  },
  "TMRE": {
    "label": "arm5e.sheet.source.TMRE",
    "source": "TMRE",
    "disabled": True
  },
  "perf": {
    "label": "perf",
    "dtype": "String",
    "source": "TMRE",
    "impact": 1
  },
  "dream": {
    "label": "dream",
    "dtype": "String",
    "source": "TMRE",
    "impact": 1
  },
  "minutes": {
    "label": "minutes",
    "dtype": "String",
    "source": "TMRE",
    "impact": 1
  },
  "hours": {
    "label": "hours",
    "dtype": "String",
    "source": "TMRE",
    "impact": 2
  },
  "arcr": {
    "label": "arcr",
    "dtype": "String",
    "source": "TMRE",
    "impact": 3
  },
  "days": {
    "label": "days",
    "dtype": "String",
    "source": "TMRE",
    "impact": 3
  },
  "sign": {
    "label": "sign",
    "dtype": "String",
    "source": "TMRE",
    "impact": 4
  },
  "AM": {
    "label": "arm5e.sheet.source.AnM",
    "source": "AnM",
    "disabled": True
  },
  "event": {
    "label": "event",
    "dtype": "String",
    "source": "AnM",
    "impact": 0
  },
  "rune": {
    "label": "rune",
    "dtype": "String",
    "source": "AnM",
    "impact": 3
  },
  "19year": {
    "label": "19year",
    "dtype": "String",
    "source": "AnM",
    "impact": 5
  },
  "custom": {
    "label": "arm5e.sheet.source.custom",
    "value": True,
    "edit": "disabled"
  },
  "other": {
    "label": "arm5e.sheet.other",
    "dtype": "String",
    "impact": 0
  },
  "season": {
    "label": "season",
    "dtype": "String",
    "impact": 2
  }
}

durations = {
      "moment": "Momentary",
      "conc": "Concentration",
      "diam": "Diameter",
      "perf": "Performance (Perf.)",
      "dream": "Dream (Dream)",
      "recitation": "Recitation (Holy)",
      "office": "Office (Holy)",
      "storm": "Storm (Atlantean)",
      "focus": "Focus (Faerie)",
      "minutes": "Minutes (Astrology)",
      "held": "Held (Fae)",
      "while": "While (Fae)",
      "sun": "Sun",
      "ring": "Ring",
      "cursed": "Cursed (Malef.)",
      "geas": "Geas (Faerie)",
      "hours": "Hours (Astrology)",
      "hour+1": "Hour + 1 (Faerie)",
      "mm": "Midday/night (Faerie)",
      "not": "Not (Faerie)",
      "season": "Season (Faerie)",
      "devotion": "Devotion (Holy)",
      "sabbath": "Sabbath (Holy)",
      "moon": "Moon",
      "fire": "Fire (Fae)",
      "bargain": "Bargain (Fae)",
      "arcr": "Arcane Ring (Arithm.)",
      "rune": "Rune (Runic)",
      "holy40": "40 (Holy)",
      "days": "Days (Astrology)",
      "fast": "Fast (Holy)",
      "year": "Year",
      "condition": "Condition (Fae)",
      "year+1": "Year and a day (Fae)",
      "sign": "Signs (Astrology)",
      "faerie": "Faerie (Fae)",
      "hidden": "Hidden (Fae)",
      "aura": "Aura (Fae)",
      "symbol": "Symbol (Fae)",
      "grace": "Grace (Holy)",
      "forsaken": "Forsaken (Malef.)",
      "19year": "19 Years (Hyperbo.)",
      "event": "Event (Defixio)",
      "if": "If (Faerie)",
      "special": "Special",
      "other": "Other",
    }

spell_ranges = {
  "personal": {
    "label": "personal",
    "dtype": "String",
    "source": "ArM5",
    "impact": 0
  },
  "touch": {
    "label": "touch",
    "dtype": "String",
    "source": "ArM5",
    "impact": 1
  },
  "eye": {
    "label": "eye",
    "dtype": "String",
    "source": "ArM5",
    "impact": 1
  },
  "voice": {
    "label": "voice",
    "dtype": "String",
    "source": "ArM5",
    "impact": 2
  },
  "sight": {
    "label": "sight",
    "dtype": "String",
    "source": "ArM5",
    "impact": 3
  },
  "arc": {
    "label": "arc",
    "dtype": "String",
    "source": "ArM5",
    "impact": 4
  },
  "special": {
    "label": "special",
    "dtype": "String",
    "source": "ArM5",
    "impact": 0
  },
  "road": {
    "label": "road",
    "dtype": "String",
    "source": "ArM5",
    "impact": 2
  },
  "symbol": {
    "label": "symbol",
    "dtype": "String",
    "source": "RoP:F",
    "impact": 4
  },
  "presence": {
    "label": "presence",
    "dtype": "String",
    "source": "RoP:D",
    "impact": 2
  },
  "communion": {
    "label": "communion",
    "dtype": "String",
    "source": "RoP:D",
    "impact": 4
  },
  "prop": {
    "label": "prop",
    "dtype": "String",
    "source": "RoP:F",
    "impact": 1
  },
  "cross": {
    "label": "cross",
    "dtype": "String",
    "source": "RoP:I",
    "impact": 2
  },
  "ww": {
    "label": "ww",
    "dtype": "String",
    "source": "RoP:M",
    "impact": 3
  },
  "line": {
    "label": "line",
    "dtype": "String",
    "source": "TMRE",
    "impact": 3
  },
  "network": {
    "label": "network",
    "dtype": "String",
    "source": "TMRE",
    "impact": 4
  },
  "veil": {
    "label": "veil",
    "dtype": "String",
    "source": "AnM",
    "impact": 3
  },
  "unlimited": {
    "label": "unlimited",
    "dtype": "String",
    "source": "AnM",
    "impact": 6
  },
  "ground": {
    "label": "ground",
    "dtype": "String",
    "source": "custom",
    "impact": 4
  },
  "other": {
    "label": "other",
    "dtype": "String",
    "source": "custom",
    "impact": 0
  }
}

ranges = {
    "personal": "Personal",
    "touch": "Touch",
    "eye": "Eye contact",
    "prop": "Prop (Faerie)",
    "voice": "Voice",
    "road": "Road (Fae/Mercurian)",
    "cross": "Crossroads (Fae/Malef.)",
    "presence": "Presence (Fae/Holy)",
    "sight": "Sight",
    "line": "Line (Arithmetic)",
    "veil": "Veil of Death (Canaan)",
    "ww": "Water-way (Atlantean)",
    "arc": "Arcane connection",
    "ground": "Ground (R. of the wise)",
    "symbol": "Symbol (Faerie)",
    "network": "Road Network (Mercur.)",
    "communion": "Communion (Holy)",
    "unlimited": "Unlimited (Defixio)",
    "special": "Special",
    "other": "Other",
}

spell_targets = {
  "ind": {
    "label": "ind",
    "dtype": "String",
    "source": "ArM5",
    "impact": 0
  },
  "circle": {
    "label": "circle",
    "dtype": "String",
    "source": "ArM5",
    "impact": 0
  },
  "part": {
    "label": "part",
    "dtype": "String",
    "source": "ArM5",
    "impact": 1
  },
  "group": {
    "label": "group",
    "dtype": "String",
    "source": "ArM5",
    "impact": 2
  },
  "room": {
    "label": "room",
    "dtype": "String",
    "source": "ArM5",
    "impact": 2
  },
  "struct": {
    "label": "struct",
    "dtype": "String",
    "source": "ArM5",
    "impact": 3
  },
  "bound": {
    "label": "bound",
    "dtype": "String",
    "source": "ArM5",
    "impact": 4
  },
  "special": {
    "label": "arm5e.spell.special",
    "dtype": "String",
    "source": "ArM5",
    "impact": 0
  },
  "taste": {
    "label": "taste",
    "dtype": "String",
    "source": "ArM5",
    "impact": 0
  },
  "touch": {
    "label": "touch",
    "dtype": "String",
    "source": "ArM5",
    "impact": 1
  },
  "smell": {
    "label": "smell",
    "dtype": "String",
    "source": "ArM5",
    "impact": 2
  },
  "hearing": {
    "label": "hearing",
    "dtype": "String",
    "source": "ArM5",
    "impact": 3
  },
  "sight": {
    "label": "sight",
    "dtype": "String",
    "source": "ArM5",
    "impact": 4
  },
  "bloodline": {
    "label": "bloodline",
    "dtype": "String",
    "source": "ArM5",
    "impact": 3
  },
  "flavor": {
    "label": "flavor",
    "dtype": "String",
    "source": "HoH:MC",
    "impact": 0
  },
  "texture": {
    "label": "texture",
    "dtype": "String",
    "source": "HoH:MC",
    "impact": 1
  },
  "scent": {
    "label": "scent",
    "dtype": "String",
    "source": "HoH:MC",
    "impact": 2
  },
  "sound": {
    "label": "sound",
    "dtype": "String",
    "source": "HoH:MC",
    "impact": 3
  },
  "spectacle": {
    "label": "spectacle",
    "dtype": "String",
    "source": "HoH:MC",
    "impact": 4
  },
  "symbol": {
    "label": "symbol",
    "dtype": "String",
    "source": "RoP:F",
    "impact": 4
  },
  "sin": {
    "label": "sin",
    "dtype": "String",
    "source": "RoP:D",
    "impact": 0
  },
  "faith": {
    "label": "faith",
    "dtype": "String",
    "source": "RoP:D",
    "impact": 2
  },
  "dominion": {
    "label": "dominion",
    "dtype": "String",
    "source": "RoP:D",
    "impact": 4
  },
  "community": {
    "label": "community",
    "dtype": "String",
    "source": "??",
    "impact": 4
  },
  "medium": {
    "label": "medium",
    "dtype": "String",
    "source": "RoP:F",
    "impact": 1
  },
  "passion": {
    "label": "passion",
    "dtype": "String",
    "source": "RoP:I",
    "impact": 2
  },
  "bw": {
    "label": "bw",
    "dtype": "String",
    "source": "RoP:M",
    "impact": 3
  },
  "dream": {
    "label": "dream",
    "dtype": "String",
    "source": "TMRE",
    "impact": 0
  },
  "carc": {
    "label": "carc",
    "dtype": "String",
    "source": "TMRE",
    "impact": 1
  },
  "road": {
    "label": "road",
    "dtype": "String",
    "source": "TMRE",
    "impact": 2
  },
  "network": {
    "label": "network",
    "dtype": "String",
    "source": "TMRE",
    "impact": 4
  },
  "unborn": {
    "label": "unborn",
    "dtype": "String",
    "source": "AnM",
    "impact": 0
  },
  "inscription": {
    "label": "inscription",
    "dtype": "String",
    "source": "AnM",
    "impact": 0
  },
  "other": {
    "label": "arm5e.sheet.other",
    "dtype": "String",
    "source": "custom",
    "impact": 0
  }
}

targets = {
    "ind": "Individual",
    "circle": "Circle",
    "taste": "Taste (In)",
    "unborn": "Unborn Child (Fert.)",
    "dream": "Dream (Dream)",
    "inscription": "Inscription (Runic)",
    "sin": "Sin (Holy)",
    "flavor": "Flavor (Sensory)",
    "part": "Part",
    "touch": "Touch (In)",
    "carc": "Arcane Circle (Arithm.)",
    "medium": "Medium (Faerie)",
    "texture": "Texture (Sensory)",
    "group": "Group",
    "room": "Room",
    "smell": "Smell (In)",
    "passion": "Passion (Fae/Malef.)",
    "faith": "Faith (Holy)",
    "road": "Road (Mercurian)",
    "scent": "Scent (Sensory)",
    "struct": "Structure",
    "hearing": "Hearing (In)",
    "bloodline": "Bloodline (Fae)",
    "bw": "Body-of-Water (Atlant)",
    "sound": "Sound (Sensory)",
    "bound": "Boundary",
    "sight": "Vision (In)",
    "network": "Road Network (Mercu)",
    "symbol": "Symbol (Faerie)",
    "spectacle": "Spectacle (Sensory)",
    "community": "Community (RotW)",
    "dominion": "Dominion (Faerie)",
    "special": "Special",
    "other": "Other",
}

# <:emoji_name:emoji_id>
def get_emoji(tech, form, iswhite=True):
  msg = ''  
  if iswhite:
    match tech:
      case 'cr':
        msg = msg + '<:crw:1307920982282862632>'
      case 'in':
        msg = msg + '<:inw:1307921033826799646>'
      case 're':
        msg = msg + '<:rew:1307921090928181268>'
      case 'mu':
        msg = msg + '<:muw:1307921061328715836>'
      case 'pe':
        msg = msg + '<:pew:1307921072943005696>'
    match form:
      case 'au':
        msg = msg + '<:auw:1307920948359331922>'
      case 'an':
        msg = msg + '<:anw:1307920923839434762>'
      case 'aq':
        msg = msg + '<:aqw:1307920936841904200>'
      case 'co':
        msg = msg + '<:cow:1307920968941043752>'
      case 'he':
        msg = msg + '<:hew:1307920995595583548>'
      case 'ig':
        msg = msg + '<:igw:1307921009004908565>'
      case 'im':
        msg = msg + '<:imw:1307921022472683553>'
      case 'me':
        msg = msg + '<:mew:1307921048372514838>'
      case 'te':
        msg = msg + '<:tew:1307921104932831262>'
      case 'vi':
        msg = msg + '<:viw:1307921118975234180>'
  else:
    match tech:
      case 'cr':
        msg = msg + '<:cr:1307505148729233508>'
      case 'in':
        msg = msg + '<:in:1307505212755546205>'
      case 're':
        msg = msg + '<:re:1307505352224411700>'
      case 'mu':
        msg = msg + '<:mu:1307505317273407560>'
      case 'pe':
        msg = msg + '<:pe:1307505333010169977>'
    match form:
      case 'au':
        msg = msg + '<:au:1307505116378566808>'
      case 'an':
        msg = msg + '<:an:1307505052075950140>'
      case 'aq':
        msg = msg + '<:aq:1307505098313826395>'
      case 'co':
        msg = msg + '<:co:1307505132367384728>'
      case 'he':
        msg = msg + '<:he:1307505165217169498>'
      case 'ig':
        msg = msg + '<:ig:1307505181704982590>'
      case 'im':
        msg = msg + '<:im:1307505197299400845>'
      case 'me':
        msg = msg + '<:me:1307505238760230932>'
      case 'te':
        msg = msg + '<:te:1307505366388441168>'
      case 'vi':
        msg = msg + '<:vi:1307505387045523497>'
  return msg

def getValue(spell_data, label):
    return spell_data[label]["impact"]

def search_spell(query):

    if query == '': return ''    

    names = []
    for i in data:
        names.append(i['name'])

    result, score = process.extractOne(query, names, scorer=fuzz.token_set_ratio)

    spell = next((i for i in data if i['name'] == result), None)
    if spell is None:
        return ''

    #print(f"Top match: {result}, Score: {score}, Index: {line}")
    #print(process.extract(query, names))
    #print(json.dumps(spell, indent=4, sort_keys=True))

    name = spell['name']
    description = spell['system']['description']
    spell_base = spell['system']['baseLevel']
    spell_range = spell['system']['range']['value']
    spell_duration = spell['system']['duration']['value']
    spell_target = spell['system']['target']['value']
    spell_complexity = spell['system']['complexity']
    spell_size = spell['system']['targetSize']
    spell_source = spell['system']['source']
    spell_source_page = spell['system']['page']

    emojis = get_emoji(spell['system']['technique']['value'], spell['system']['form']['value'])

    technique = spell['system']['technique']['value'].capitalize()
    form = spell['system']['form']['value'].capitalize()

    level = calculate_level(spell_base, spell_range, spell_duration, spell_target, spell_size, spell_complexity)

    spell_level = emojis + " " + technique + form + " " + str(level)

    text_maker = html2text.HTML2Text()
    text_maker.body_width = 0
    description = text_maker.handle(description).strip()

    #if len(description) > 1500:
    #    description = description[:1500] + " (...)"

    msg = ''
    msg = msg + "**" + name + "** (" + spell_level +")\n"
    msg = msg + "**R**: " + ranges[spell_range]
    msg = msg + " **D**: " + durations[spell_duration]
    msg = msg + " **T**: " + targets[spell_target] + "\n"
    msg = msg + description + "\n(Base " + str(spell_base)
    msg = msg + ", +" + str(spell_ranges[spell_range]['impact']) + " " + ranges[spell_range] 
    msg = msg + ", +" + str(spell_durations[spell_duration]['impact']) + " " + durations[spell_duration]
    msg = msg + ", +" + str(spell_targets[spell_target]['impact']) + " " + targets[spell_target]
    if spell_size > 0: msg = msg + ", +" + str(spell_size) + " Size"
    if spell_complexity > 0: msg = msg + ", +" + str(spell_complexity) + " Complexity"
    msg = msg + ")"
    msg = msg + " *Src: " + spell_source + " p." + str(spell_source_page) + "*"

    return msg

def add_spell_magnitude(base, num):
    # Convert to an integer if it's a string
    base = int(base)

    if num == 0:
        return base

    if num > 0:
        if base + num <= 5:
            return base + num
        else:
            res = base
            while num > 0:
                if res < 5:
                    res += 1
                else:
                    res += 5
                num -= 1
            return res

    else:  # num < 0
        if base + num <= 1:
            return base + num
        else:
            res = base
            while num < 0:
                if res <= 5:
                    res -= 1
                else:
                    res -= 5
                num += 1
            return res

def calculate_level(b, r, d, t, s, c):
    r = int(getValue(spell_ranges, r))
    d = int(getValue(spell_durations, d))
    t = int(getValue(spell_targets, t))
    return add_spell_magnitude(b, r + d + t + s + c)

def get_spell_base_size(form):
    form = form.lower()
    if len(form) > 2: form = form[:2]
    if form == 'an': return form.capitalize() + ": Size +1 animal (small pony)"
    if form == 'aq': return form.capitalize() + ": 5 paces across, 2 paces deep"
    if form == 'au': return form.capitalize() + ": Area one hundred paces across"
    if form == 'co': return form.capitalize() + ": Adult human being, up to Size +1"
    if form == 'he': return form.capitalize() + ": Plant roughly one pace in each direction"
    if form == 'ig': return form.capitalize() + ": Large campfire or the fire in the hearth of a great hall"
    if form == 'im': return form.capitalize() + ": Adult human being capabilities (size, noise,...)"
    if form == 'me': return form.capitalize() + ": A mind is a mind, no size"
    if form == 'te': return form.capitalize() + ": Depend on material, from 10 cubic paces (sand, dirt) to 1 cubic inch (gem)"
    if form == 'vi': return form.capitalize() + ": A spell or depend on the effect"
    return ""

def get_mag_list(data, labels):
    d = []
    for k,v in data.items():
        if 'impact' in v.keys():
            d.append((labels[k],v['impact']))
    d = sorted(d, key=lambda mod: mod[1])
    return d

def get_formated_mag_list(mag_list):
    msg = ''
    for x,y in mag_list:
        msg = msg + x + " +" + str(y) + "\n"
    return msg

def get_durations():
    d = get_mag_list(spell_durations, durations)
    return get_formated_mag_list(d)

def get_ranges():
    d = get_mag_list(spell_ranges, ranges)
    return get_formated_mag_list(d)

def get_targets():
    d = get_mag_list(spell_targets, targets)
    return get_formated_mag_list(d)


#print(search_spell(sys.argv[1]))
#print(get_durations())
#print(get_ranges())
#print(get_targets())
#print(get_spell_base_size(sys.argv[1]))
#print(json.dumps(data, indent=4, sort_keys=True))
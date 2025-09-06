# Independent vowels
SINHALA_VOWELS = {
    "අ": "a", "ආ": "aa", "ඇ": "ae", "ඈ": "aae",
    "ඉ": "i", "ඊ": "ii", "උ": "u", "ඌ": "uu",
    "ඍ": "ru", "ඎ": "rū", "ඏ": "lu", "ඐ": "lū",
    "එ": "e", "ඒ": "ee", "ඓ": "ai", "ඔ": "o",
    "ඕ": "oo", "ඖ": "au",
}

SINHALA_CONSONANTS = {
    "ක": "k", "ඛ": "kh", "ග": "g", "ඝ": "gh",
    "ඞ": "nga", "ච": "ch", "ඡ": "chh", "ජ": "j", "ඣ": "jh",
    "ට": "t", "ඨ": "th", "ඩ": "d", "ඪ": "dh", "ණ": "n",
    "ත": "t", "ථ": "thh", "ද": "d", "ධ": "dh", "න": "n",
    "ප": "p", "ඵ": "ph", "බ": "b", "භ": "bh", "ම": "m",
    "ය": "y", "ර": "r", "ල": "l", "ව": "v", "ශ": "sh",
    "ෂ": "ss", "ස": "s", "හ": "h", "ළ": "l", "ෆ": "f",
}

PHONETIC_MAP = {
    "අ": "a", "ආ": "a",  # long a → short a
    "ඇ": "ae", "ඈ": "ae",
    "ඉ": "i", "ඊ": "i",
    "උ": "u", "ඌ": "u",
    "ක": "k", "ග": "g", "ච": "ch", "ජ": "j",
    "ට": "t", "ඩ": "d", "ත": "t", "ද": "d",
    "ප": "p", "බ": "b", "ම": "m", "ය": "y",
    "ර": "r", "ල": "l", "ව": "v", "ශ": "sh",
    "ෂ": "sh", "ස": "s", "හ": "h", "ළ": "l",
}
COMMON_NAMES = {
    "සු": "su", "දු": "du", "හා": "ha",
    "නේ": "ne", "මි": "mi", "රූ": "ru",
    "ච්චි": "chchi", "ක්‍ර": "kra", "සූ": "su",
    "ආ": "a", "අ": "a"
}

SINHALA_MODIFIERS = {
    "ා": "aa", "ැ": "ae", "ෑ": "aae",
    "ි": "i", "ී": "ii", "ු": "u", "ූ": "uu",
    "ෘ": "ru", "ෲ": "rū",
    "ෙ": "e", "ේ": "ee", "ෛ": "ai",
    "ො": "o", "ෝ": "oo", "ෞ": "au",
    "්": "",  # Virama (hal kirīma)
}

SINHALA_CONSONANTS = {
    "ක": "k", "ඛ": "kh", "ග": "g", "ඝ": "gh",
    "ඞ": "nga", "ච": "ch", "ඡ": "chh", "ජ": "j", "ඣ": "jh",
    "ට": "t", "ඨ": "th", "ඩ": "d", "ඪ": "dh", "ණ": "n",
    "ත": "t", "ථ": "thh", "ද": "d", "ධ": "dh", "න": "n",
    "ප": "p", "ඵ": "ph", "බ": "b", "භ": "bh", "ම": "m",
    "ය": "y", "ර": "r", "ල": "l", "ව": "v", "ශ": "sh",
    "ෂ": "ss", "ස": "s", "හ": "h", "ළ": "l", "ෆ": "f",
}

SINHALA_COMBOS = {
    "කා": "ka", "කී": "kii", "කූ": "kuu",
    "ගා": "ga", "ගී": "gii", "ගූ": "guu",
    "චා": "cha", "ජා": "ja", "ජී": "jii",
    "ටා": "ta", "ඩා": "da", "නා": "na",
    "පා": "pa", "බා": "ba", "මා": "ma",
    "යා": "ya", "රා": "ra", "ලා": "la",
    "වා": "va", "ශා": "sha", "ෂා": "ssa",
    "සා": "sa", "හා": "ha", "ළා": "la",
    "ෆා": "fa",
}


SINHALA_NAME_SYLLABLES = {
    "සු": "su", "දු": "du", "හා": "ha", "මි": "mi",
    "නේ": "ne", "ර": "ra", "ද": "da", "ශි": "shi",
    "රූ": "ru", "ජය": "jaya", "වි": "vi", "ක්‍ර": "kra",
    "ම": "ma", "සූ": "suu", "රිය": "riya", "ආ": "aa",
    "අ": "a", "න": "na", "ද": "da", "ච්චි": "chchi",
    "ඉ": "i", "උ": "u", "ඇ": "ae",
}


# Final map
SINHALA_MAP = {}
SINHALA_MAP.update(SINHALA_VOWELS)
SINHALA_MAP.update(PHONETIC_MAP)
SINHALA_MAP.update(COMMON_NAMES)
SINHALA_MAP.update(SINHALA_CONSONANTS)
SINHALA_MAP.update(SINHALA_COMBOS)
SINHALA_MAP.update(SINHALA_NAME_SYLLABLES)
SINHALA_MAP.update(SINHALA_MODIFIERS)
SINHALA_MAP[" "] = " "  # Keep spaces



def transliterate(text: str) -> str:
    result = ""
    i = 0
    while i < len(text):
        match_found = False
        # Try longest first
        for length in [4,3,2,1]:  # increase length for longer combos
            part = text[i:i+length]
            if part in SINHALA_MAP:
                result += SINHALA_MAP[part]
                i += length
                match_found = True
                break
        if not match_found:
            result += text[i]
            i += 1
    return result



def transliterate_list(names: list) -> list:
    return [transliterate(name) for name in names]

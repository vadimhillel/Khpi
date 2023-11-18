def vowel_count(string):
    return f"Amount of vowels: {len([ch for ch in string if ch in 'aeiouAEIOU'])}"

assert(vowel_count("VolodymyrOleksandrovichZelenskyi"))
print(vowel_count("VolodymyrOleksandrovichZelenskyi"))
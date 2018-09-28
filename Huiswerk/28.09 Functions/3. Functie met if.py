length = float(input("Voer hier je lengte in cm in: "))

def lang_genoeg(length):
    if length == 120 or length > 120:
        return "Je bent lang genoeg voor de attractie!"
    return "Sorry, je bent niet lang genoeg!"

print(lang_genoeg(length))
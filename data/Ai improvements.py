import csv
import random
import os


fortunes = {
    "Aries": [
        "Take the first step today; momentum will follow.",
        "A bold decision will lead to exciting opportunities.",
        "Your enthusiasm will inspire someone around you."
    ],
    "Taurus": [
        "A small act of patience will bring a big reward.",
        "Comfort and success go hand in hand today.",
        "Someone will appreciate your dependable nature."
    ],
    "Gemini": [
        "A meaningful conversation will open new doors.",
        "Your curiosity will lead to an unexpected discovery.",
        "Flexibility will help you overcome a challenge."
    ],
    "Cancer": [
        "Your compassion will strengthen an important relationship.",
        "A peaceful moment will help you gain clarity.",
        "Home is where you'll find today's greatest comfort."
    ],
    "Leo": [
        "Your confidence will attract positive attention.",
        "An opportunity to shine is closer than you think.",
        "Your generosity will be remembered."
    ],
    "Virgo": [
        "Careful planning will make your day easier.",
        "A new skill will prove useful sooner than expected.",
        "Your attention to detail will be recognized."
    ],
    "Libra": [
        "A thoughtful compromise will create harmony.",
        "Beauty can be found in unexpected places today.",
        "Your fairness will earn someone's trust."
    ],
    "Scorpio": [
        "A mystery will soon reveal its answer.",
        "Your determination will help you achieve a personal goal.",
        "Trust your intuition when making an important choice."
    ],
    "Sagittarius": [
        "A spontaneous adventure will create a lasting memory.",
        "Optimism will help you overcome today's obstacles.",
        "An exciting idea is worth pursuing."
    ],
    "Capricorn": [
        "Steady progress is better than rushing ahead.",
        "Your discipline will bring long-term rewards.",
        "Someone admires your dedication more than you realize."
    ],
    "Aquarius": [
        "Your originality will spark inspiration in others.",
        "An unexpected idea will solve an old problem.",
        "Embrace change—it will work in your favor."
    ],
    "Pisces": [
        "A kind gesture will come back to you unexpectedly.",
        "Your imagination will guide you toward success.",
        "Today is a good day to trust your dreams."
    ]
}

# Determines zodiac sign
def zodiac(month, day):

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"

    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"

    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"

    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"

    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"

    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"

    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"

    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"

    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"

    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"

    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"

    else:
        return "Pisces"

# Save results
def save_history(name, sign, fortune, feedback):

    file_exists = os.path.exists("history.csv")

    with open("history.csv", "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Name","Sign","Fortune","Feedback"])

        writer.writerow([name, sign, fortune, feedback])

# Main program
print("Welcome to the Astrology Calendar!")

name = input("Enter your name: ")

month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day: "))

sign = zodiac(month, day)

fortune = random.choice(fortunes[sign])

print("\nYour Zodiac Sign:", sign)
print("Today's Fortune:")
print(fortune)

choice = input("\nWould you like this fortune rephrased? (yes/no): ")

if choice.lower() == "yes":
    print("Simplified:")
    print("This fortune means that something positive may happen if you stay confident.")

feedback = input("\nDid this fortune match your day? (yes/no): ")

save_history(name, sign, fortune, feedback)

print("\nYour results have been saved.")
print("Thank you for using the Astrology Calendar!")
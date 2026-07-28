print("Welcome to your Astrology calender")
month = int(input("What is your Birth Month")) 
day = int(input("What is Your Birth Day"))
import random

if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        zodiac_sign = "Aries"
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac_sign ="Taurus"
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac_sign = "Gemini"
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac_sign = "Cancer"
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac_sign = "Leo"
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac_sign = "Virgo"
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        zodiac_sign = "Libra"
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        zodiac_sign = "Scorpio"
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac_sign = "Sagittarius"
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        zodiac_sign = "Capricorn"
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        zodiac_sign = "Aquarius"
elif(month == 2 and day >= 19) or (month == 3 and day <= 20):
        zodiac_sign = "Pisces"
else:
    print("Not an option")

print("you are a", zodiac_sign)
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
fortune = random.choice(fortunes[zodiac_sign])
print("Todays Fortune is")
print(fortune)
again = "yes"

while again == "yes":
    fortune = random.choice(fortunes[zodiac_sign])
    print("\Heres another fortune")
    print(fortune)
    again = input("\nWould you like another fortune? (yes/no): ").lower()

print("Hope This fortune is what you needed today")


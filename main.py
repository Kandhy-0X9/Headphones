import os

def clearTerminal():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

clearTerminal()
# class headphone
class Headphone:
    def __init__(self, brand, name, color, volumeII=0, speakers=2):
        self.brand = brand
        self.name = name
        self.color = color
        self._volume = volumeII
        self.speakers = speakers

    def volume(self, value):
        if value < 0:
            value = 0
        elif value > 20:
            value = 20
        self._volume = value
        return self._volume

    def volumeUp(self, amount):
        self._volume += amount
        return self._volume

    def volumeDown(self, amount):
        self._volume -= amount
        return self._volume
    
    def __str__(self):
        return f"Brand: {self.brand} \nType: {self.name}\nColor: {self.color}\nVolume: {self.volume}\nSpeakers: {self.speakers}"

# create headphone objects
Beats = Headphone("Beats", "Beats Studio Pro", "Blue", 0, 2)
Bose = Headphone("Bose", "Bose QuiteComfort", "Black", 0, 2)
Sony = Headphone("Sony", "Sony WH-CH720N", "Maroon", 0, 2)

headPhones = [Beats, Bose, Sony]

print("Available headphones:")
for headphone in headPhones:
    print(f"{headphone.name} by {headphone.brand}")
print()

# ask user question
selected_headphone = None
while selected_headphone is None:
    question1 = input("what headphone do you want to use? (Beats, Bose, Sony) ").strip().lower()

    for headphone in headPhones:
        if question1 == headphone.name.lower() or question1 == headphone.brand.lower():
            selected_headphone = headphone
            break
    if selected_headphone is None:
        print("Invalid input. Please try again.\n")
    else:
        print(f"{selected_headphone} selected.")

question2 = input("Do you want to increase or decrease the volume? (increase/decrease) "
"").strip().lower()
if question2 == "increase":
    amount = int(input("By how much? "))
    selected_headphone.volumeUp(amount)
    print(f"{selected_headphone} increased by {amount}")
    print(f"{selected_headphone} has a volume of {selected_headphone._volume}")

elif question2 == "decrease":
    amount = int(input("By how much? "))
    selected_headphone.volumeDown(amount)
    print(f"{selected_headphone} decreased by {amount}")
    print(f"{selected_headphone} has a volume of {selected_headphone._volume}")
else:
    print("No volume change applied.")
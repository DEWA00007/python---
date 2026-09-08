# Typing speed test 

import time
import random

sentences = [
    "Python is fun to learn",
    "Practice makes you better at coding.",
    "I am learning Python one project at a time.",
    "Programming is fun when you build cool things.",
    "Never stop learning new skills.",
    "The quick brown fox jumps over the lazy dog."
             ]
sentence = random.choice(sentences)
print("=" * 50)
print("          🧑‍💻 TYPING SPEED TEST")
print("=" * 50)
print("\nType the following sentence as fast as you can:\n")
print()

print(sentence)
input("Press ENTER when you're ready...")

start = time.time()
typed = input("\nYou: ")
end = time.time()

seconds = end - start
minutes = seconds / 60

words = len(typed.split())
wpm = words / minutes if minutes > 0 else 0

correct = 0


for i in range(min(len(sentence), len(typed))):
    if sentence[i] == typed[i]:
        correct += 1

accuracy = (correct / len(sentence)) * 100          

mistakes = len(sentence) - correct

print("\n" + "=" * 50)
print("               📊 RESULTS")
print("=" * 50)

print(f"⏱️ Time:      {seconds:.2f} seconds")
print(f"⚡ Speed:     {wpm:.2f} WPM")
print(f"🎯 Accuracy:  {accuracy:.2f}%")
print(f"❌ Mistakes:  {mistakes}")

if wpm >= 60:
    print("\n🔥 Excellent typing speed!")
elif wpm >= 40:
    print("\n😎 Good job!")
else:
    print("\n💪 Keep practicing!")

print("=" * 50)
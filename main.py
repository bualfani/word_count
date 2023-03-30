import keyboard
import collections

# Initialize a dictionary to keep track of the word count
word_count = collections.defaultdict(int)

def key_release(event):
    # Check if the pressed key is a letter or a space
    if event.event_type == "down" and (event.name.isalpha() or event.name.isspace()):
        # Append the pressed key to the current word
        current_word = getattr(key_release, "current_word", "") + event.name
        setattr(key_release, "current_word", current_word)
        # If the pressed key is a space, count the completed word
        if event.name.isspace():
            word_count[current_word.strip()] += 1
            setattr(key_release, "current_word", "")


keyboard.on_release(key_release)

keyboard.wait()

# Print the top 10 most typed words
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"{word}: {count}")


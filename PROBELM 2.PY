import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("""Hello there! This is a demonstration of the Python text to speech engine. 
I can read out long passages, narrate stories, or even explain programming concepts. 
For example, did you know that Python was named after Monty Python’s Flying Circus, 
and not after the snake? Interesting, isn’t it? 
With pyttsx3, your computer can literally speak your mind, 
whether it is a bedtime story, a motivational speech, 
or even a terrible programmer joke. 
Here’s one: Why do Java developers wear glasses? 
Because they don’t C sharp! 
Alright, that’s enough for now. 
Goodbye, and happy coding!""")
engine.runAndWait()



import pyttsx3
import pygame

# Step 1: pyttsx3 se audio banao aur save karo
engine = pyttsx3.init()
engine.save_to_file("Hello! Welcome to my Pygame demo. This is text to speech in action.", "speech.mp3")
engine.runAndWait()

# Step 2: Pygame initialize karo
pygame.init()
pygame.mixer.init()

# Step 3: Saved audio load karo
pygame.mixer.music.load("speech.mp3")

# Step 4: Play the audio
pygame.mixer.music.play()

# Step 5: Wait until audio finishes
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()


#  Import any module and use it ......

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("This Text will be spoken by your system , you can enter any text")
engine.runAndWait()


# Porblem solved

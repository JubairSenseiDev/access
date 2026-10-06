import os as jubair
import time as zzz

#  Colors
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
RESET = "\033[0m"


def typing(text, color, speed=0.045):
    for char in text:
        print(color + char + RESET, end="", flush=True)
        zzz.sleep(speed)
    print()


def salam_typing(speed=0.09):
    # Assalamu = Cyan
    for char in "Assalamu":
        print(CYAN + char + RESET, end="", flush=True)
        zzz.sleep(speed)

    print(" ", end="", flush=True)
    zzz.sleep(speed)

    # Alaikum = Yellow
    for char in "Alaikum.":
        print(YELLOW + char + RESET, end="", flush=True)
        zzz.sleep(speed)

    print()


# Clear terminal
jubair.system("cls" if jubair.name == "nt" else "clear")


# 👋 Intro
typing("hey 👋", MAGENTA, 0.10)
typing("I am Jubair Ahmad", CYAN, 0.08)

print()

# 🕌 Salam
salam_typing(0.10)

# 💬 Main message
typing(
    "I just wanted to let everyone in this community know that",
    GREEN,
    0.035
)

typing(
    "I need to take a little break and stay offline for a while.",
    GREEN,
    0.035
)

typing(
    "Due to some physical and mental health issues,",
    GREEN,
    0.035
)

typing(
    "I may not be active here for the next few days.",
    GREEN,
    0.035
)

print()

# 🤲 Dua section — SAME COLOR
DUA_COLOR = YELLOW

typing(
    "Please remember me in your prayers.",
    DUA_COLOR,
    0.045
)

typing(
    "Pray that Allah grants me complete shifa,",
    DUA_COLOR,
    0.045
)

typing(
    "gives me strength, peace, and patience,",
    DUA_COLOR,
    0.045
)

typing(
    "and helps me return to you all soon.",
    DUA_COLOR,
    0.045
)

typing(
    "Your prayers and kind words truly mean a lot to me.",
    DUA_COLOR,
    0.045
)

print()

# ❤️ Closing
typing(
    "Take care of yourselves and keep smiling.",
    BLUE,
    0.045
)

typing(
    "I hope to be back among you very soon, In Sha Allah. 🤍",
    MAGENTA,
    0.045
)

print()
typing("— Jubair Ahmad", CYAN, 0.08)

print(RESET)

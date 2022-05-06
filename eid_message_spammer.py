# IMPORT PACKAGES
import random
import pyautogui as pg
import time

# TEXT TO WRITE
text = ('Eid Mubarak!',  'Taqabbala Allahu minna wa minkum', \
        'Eid Saeed!', 'May every year find you in good health!', \
        'May Allah accept from us, and from you 🤲🏾')

# DELAY EXECUTION BY 2 SECONDS
time.sleep(2)

# REPEAT SENDING THE MESSAGE AT RANDOM 9 TIMES (because index is 10)
for i in range(10):
    t = random.choice(text)
    pg.write(t + '\n')
    pg.press('enter')
    time.sleep(2)
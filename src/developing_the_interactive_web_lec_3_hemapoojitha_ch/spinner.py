from halo import Halo
from time import sleep
spinner = Halo(text='Loading', spinner='dots')
spinner.start()
sleep(60)
spinner.stop()
import pygame
import glob

sampleList = glob.glob("samples/*.wav");
pygame.mixer.init()

soundList = []
for sample in sampleList:
    print sample
    soundList.append(pygame.mixer.Sound(sample))

for sound in soundList:
    sound.play()
    #while pygame.mixer.get_busy() == True:
        #continue
print "end"

import pygame
APO_SOLO_PATH_MP3 = 'utils/music/apo_solo.mp3'


class Music():
    def __init__(self, track):
        self.track = track

    def play(self):
        pygame.mixer_music.load(self.track)
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.25)

    def setVolume(self, volume):
        pygame.mixer_music.set_volume(volume)

music = Music(APO_SOLO_PATH_MP3)

__all__ = ['music']

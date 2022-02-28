"""
Imagine that you have a video that you want to play. You have audioplayer (only able to play the audio without showing
the video) and videoplayer (only able to display the video without sound). Create classes video (with attributes video,
audio, adapter and player, as well as other attributes and methods of your choice), player interface, audioplayer and
videoplayers of type player (these should have a method play which should play the media file in case it is in the
right format and print some other message otherwise), adapters for modifying the media files according to the player
used. Feel free to implement the logic however you imagine, using adapter design pattern. Also have examples of the
usage of your class structure.
"""

"""
adapters for modifying the media files according to the player
used. Feel free to implement the logic however you imagine, using adapter design pattern. Also have examples of the
usage of your class structure.
"""
from abc import ABC, abstractmethod
import os


class Media(ABC):
    def __init__(self, path):
        self.path = path
        self.format = os.path.splitext(self.path)[1]


class Player(ABC):
    def __init__(self):
        self._supported_formats = []

    @abstractmethod
    def play(self, media: Media):
        pass

    def validate_format(self, media: Media):
        is_valid = media.format in self._supported_formats
        if not is_valid:
            print(f"Unable to play {media.path}. "
                  f"Please provide one of {', '.join(self._supported_formats)} formats.")
        return is_valid


class Video(Media):
    def __init__(self, path, video_stream, audio_stream):
        super().__init__(path)
        self.video = video_stream['frames']
        self.audio = audio_stream['stream']
        self.duration = audio_stream['duration']


class Audio(Media):
    def __init__(self, path, audio_stream):
        super().__init__(path)
        self.audio = audio_stream['stream']
        self.duration = audio_stream['duration']


class AudioPlayer(Player):
    def __init__(self):
        super().__init__()
        self._supported_formats = ['.mp3', '.wav']

    def play(self, audio: Audio):
        if self.validate_format(audio):
            print(f"Playing audio at {audio.path}")


class VideoPlayer(Player):
    def __init__(self):
        super().__init__()
        self._supported_formats = ['.mp4', '.avi']

    def play(self, video: Video):
        if self.validate_format(video):
            print(f"Playing video at {video.path}")


class VideoAdapter(Video):
    def __init__(self, audio: Audio):
        blank_video_stream = self.generate_black_screen(audio.duration)
        tmp_path = os.path.splitext(audio.path)[0]+'.mp4'
        audio_stream = {'stream': audio.audio, 'duration': audio.duration}
        super().__init__(tmp_path, blank_video_stream, audio_stream)

    def generate_black_screen(self, duration):
        return {'frames': [0]*duration}


class AudioAdapter(Audio):
    def __init__(self, video: Video):
        tmp_path = os.path.splitext(video.path)[0] + '.wav'
        audio_stream = {'stream': video.audio, 'duration': video.duration}
        super().__init__(tmp_path, audio_stream)


def main():
    audio_player = AudioPlayer()
    video_player = VideoPlayer()

    video1 = Video(
        path='~/user/videos/video1.mp4',
        video_stream={'frames': list(range(10))},
        audio_stream={'stream': list(range(10)), 'duration': 10}
    )

    audio1 = Audio(
        path='~/user/audios/audio1.wav',
        audio_stream={'stream': list(range(20)), 'duration': 20}
    )

    audio_player.play(audio1)
    audio_player.play(video1)
    audio_player.play(AudioAdapter(video1))

    video_player.play(video1)
    video_player.play(audio1)
    video_player.play(VideoAdapter(audio1))


if __name__ == '__main__':
    main()

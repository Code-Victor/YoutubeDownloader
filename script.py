from pytube import YouTube,Playlist,extract
from youtube_transcript_api import YouTubeTranscriptApi as ytTrans
from youtube_transcript_api.formatters import WebVTTFormatter
from pytube.cli import on_progress
from docx import Document
import os


class getyoutubevideo:
    def __init__(self,url,destinaiton=r"C:\users\oluwa\tutorials",audio=False,resolution='480p',Transcript=True,language=['en']):
        self.url=url
        self.destination=destinaiton
        self.transcript=Transcript
        self.resolution=resolution
        self.audio=audio
        self.transcript_language=language
        self.videoId=extract.video_id(self.url)
        self.yt=YouTube(self.url)
        self.name=self.yt.title
        for word, initial in {'?':'.','<':'.','>':'.','|':'.','*':'.'}.items():
            self.name = self.name.replace(word.lower(), initial)
        




    def getTranscript(self):
        transcript=ytTrans.get_transcript(self.videoId,languages=self.transcript_language)
        webvtt_formatter=WebVTTFormatter()
        webvtt_formatted=webvtt_formatter.format_transcript(transcript=transcript)
        with open('{}.vtt'.format(self.name), 'w', encoding='utf-8') as webvtt_file:
            webvtt_file.write(webvtt_formatted)

    def _getDescription(self):
        document=Document()
        description=self.yt.description
        document.add_heading(self.name,0)
        document.add_paragraph(description)
        document.save('{}.docx'.format(self.name))
        stream=self.yt.streams.filter(res=self.resolution)
         
        

    def getVideo(self):
        if self.audio==True:
            if self.audio_quality:
                try:
                    for stream in self.yt.streams.filter(only_audio=True):
                        if stream.abr == self.audio_quality:
                            stream.download()
                except:
                    self.yt.streams.filter(only_audio=True).first().download()
            else:
                stream=self.yt.streams.filter(only_audio=True).order_by("abr")[-1]
                stream.download()
        elif self.audio==False:
            stream=self.yt.streams.filter(res=self.resolution)  
            stream.download()
    def alltogether(self):
        self.getTranscript()
        self._getDescription()
        self.getVideo()
    

# youtube=getyoutubevideo(url="https://www.youtube.com/watch?v=VEQaH4LruUo")
# youtube.alltogether()
youtube=getyoutubevideo(url="https://youtu.be/_YPScrckx28")
# youtube.alltogether()

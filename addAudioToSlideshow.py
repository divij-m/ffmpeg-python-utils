import glob, os
import subprocess
from datetime import datetime

dirPath = input("Add Audio to Slideshow :: Enter Dir path with Files: ")
os.chdir(dirPath)

#addAudio = input("Do you want to add audio to this slideshow? [Y/N]")
try:
	audioFile = glob.glob('*.mp3')[0]
	ssFileName = glob.glob('*.mp4')[0]
except:
	print("No source files in Directory")
	

try:
	outFileName = "vid_" + ssFileName.split("slideShow_")[1] + ".mp4"
except:
	outFileName = "vid_" + ssFileName.split(".mp4")[0] + "_AV.mp4"

ffmpegAudioCmd = "ffmpeg -stream_loop 1 -i "+ os.path.join(dirPath,audioFile) + " -i "+ ssFileName + " -c:a copy -c:v copy -shortest " + outFileName
	
retValue = subprocess.call(ffmpegAudioCmd, shell=True)
print(retValue)

####################################################################

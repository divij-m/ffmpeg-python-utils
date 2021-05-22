import glob, os
import subprocess
from datetime import datetime

dirPath = input("Begin to Make Slideshow :: Enter Dir path with Files: ")
os.chdir(dirPath)
fileList = "fMerge.txt"
outputFmt = ".mp4"
fstr = ""
try:
    username = dirPath.split("Insta\\")[1]
    username = username.replace('.','-')
    if '\\' in username:
        username = username.split("\\")[0]
    ssFileName = "slideShow_" + username + "_" + datetime.now().strftime("%d-%b-%H%M") + outputFmt
except:
    ssFileName = "slideShow_" + datetime.now().strftime("%d-%b-%H%M") + outputFmt

outHandler = open(fileList, "wt")
for file in glob.glob("*.jpg"):
    fstr = "file '" + os.path.join(dirPath,file) + "'\n"
    outHandler.write(fstr)
outHandler.close()

# to change duration -r = 1/3 // means 3 seconds per image => change to 1/5 for 5 secs/image

ffmpegCmd = "ffmpeg -f concat -safe 0 -r 1/3 -i " + os.path.join(dirPath,fileList) + " -c:v libx264 -r 30 -vf scale=-2:1080 -pix_fmt yuv420p " + ssFileName

retValue = subprocess.call(ffmpegCmd, shell=True)
print(retValue)

####################################################################
addAudio = input("Do you want to add audio to this slideshow? [Y/N]")
if addAudio is 'y' or 'Y':
    try:
        audioFile = glob.glob('*.mp3')[0]
        outFileName = "vid_" + ssFileName.split("slideShow_")[1]
        ffmpegAudioCmd = "ffmpeg -stream_loop 1 -i "+ os.path.join(dirPath,audioFile) + " -i "+ ssFileName + " -c:a copy -c:v copy -shortest " + outFileName
        print('Audio added successfully.')
    except:
        print('Failed to add Audio.')
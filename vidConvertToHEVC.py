import glob, os
import subprocess

dirPath = input("Enter Dir path where target Video File is located: ")
os.chdir(dirPath)

fileName = input("Enter FileName: ")
bitRate = input("Enter video bitRate [0: for default, 1M, 1500K etc] : ")
ultraFast = input("Enable Ultrafast? [y/n] : ")
outFileName = fileName + "_conv.mp4"
fileName = fileName + ".mp4"

if ultraFast is 'y' or 'Y':
    ultraFastStr = " -preset ultrafast "
else:
    ultraFastStr = " "

if bitRate is not '0':
    ffmpegCmd = "ffmpeg -i " + fileName + " -c:v libx265 -b:v " + bitRate + " -c:a copy" + ultraFastStr + outFileName
else:
    ffmpegCmd = "ffmpeg -i " + fileName + " -c:v libx265 -c:a copy" + ultraFastStr + outFileName

retValue = subprocess.call(ffmpegCmd, shell=True)
print(retValue)

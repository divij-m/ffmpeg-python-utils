import glob, os
import subprocess

dirPath = input("Enter Dir path where target Video File is located: ")
os.chdir(dirPath)

fileName = input("Enter FileName: ")
bitRateOp = input("Enter video bitRate [0: for default, 1M, 1500K etc] : ")
ultraFast = input("Enable Ultrafast? [y/n] : ")
scale960p = input("Scale video to 960x540 size? [y/n] : ")
outFileName = fileName + "_conv.mp4"
fileName = fileName + ".mp4"
scale960pVal = ""
ultraFastStr = "-profile:v main -preset slow "

if bitRateOp is not '0':
    bitRate = "-b:v " + bitRateOp + " "

if (ultraFast is 'y') or (ultraFast is 'Y'):
    ultraFastStr = "-preset ultrafast "

if (scale960p is 'y') or (scale960p is 'Y'):
    scale960pVal = "-vf scale=960:540 "

if bitRateOp is not '0':
    ffmpegCmd = "ffmpeg -i " + fileName + " -c:v libx264 " + ultraFastStr + scale960pVal + bitRate + "-c:a copy " + outFileName
else:
    ffmpegCmd = "ffmpeg -i " + fileName + " -c:v libx264 " + ultraFastStr + scale960pVal + "-c:a copy " + outFileName

print(ffmpegCmd)
retValue = subprocess.call(ffmpegCmd, shell=True)
print(retValue)

import glob, os
import subprocess
from datetime import datetime

dirPath = input("Enter Dir path to merge Vid files: ")
os.chdir(dirPath)
fileList = "fMerge.txt"
try:
    username = dirPath.split("Insta\\")[1]
    if '\\' in username:
        username = username.split("\\")[0]
    outFileName = username + "_" + datetime.now().strftime("%d_%b")
except:
    outFileName = "output_" + datetime.now().strftime("%d_%b")

outHandler = open(fileList, "wt")
for file in glob.glob("*.mp4"):
    fstr = "file '" + os.path.join(dirPath,file) + "'\n"
    outHandler.write(fstr)
outHandler.close()

ffmpegCmd = "ffmpeg -f concat -safe 0 -i " + os.path.join(dirPath,fileList) + " -c copy " + outFileName + ".mp4"
retValue = subprocess.call(ffmpegCmd, shell=True)
print(retValue)

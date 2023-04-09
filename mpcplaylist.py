
import os
from os import path
from os.path import join, getsize
# import sys
# import glob
# import shutil
# import zipfile
# import re
# import requests
# ===========================================================================
# Notes: This is a learning project for me. It will not be the optimal way to
# do thing, and it might not be optimized in any way, but it should be a
# semi-functional project when done. I might re-visit it in the future to
# optimize and include new skills.
#
# Goal: To create video-playlist for each directory and include subtitles.
#
# Approach: Walk directory structure starting from working directory.
# for each directory check for video files. Sort them and add to playlist.
# for each added video file also check for matching subtitle, and add if exist.
# ===========================================================================
Files_Audio = ['.aac', '.mp3', '.ogg', '.flac', '.wav']
Files_Video = ['.mp4', '.mvk', '.mpg', '.mpeg', '.avi']
Files_Subtitle = ['.vtt', '.sub', '.ass', '.srt']
# ===========================================================================
# Create this:
# MPCPLAYLIST
# 1,type,0
# 1,filename,001 Introduction to If Else.mp4
# 1,subtitle,001 Introduction to If Else.vtt
# 2,type,0
# 2,filename,002 IF Else - Some Examples.mp4
# 2,subtitle,002 IF Else - Some Examples.vtt
# ===========================================================================
wd = 'C:\\tmp'
os.chdir(wd)
cwd = os.getcwd()
print(cwd)
if wd != cwd:  # Exit if not in the correct directory
    exit(404)
# ===========================================================================
overwrite = 1  # set true if you want to replace existing playlists
workdir = []
print('[OK]')
print('\n')
print('Found the following directories:')
print('=' * 78)
for root, dirs, files in os.walk(wd, topdown=True):
    for name in files:
        pass
        # print(os.path.join(root, name))
    for name in dirs:
        d = os.path.join(root, name)
        workdir.append(d)
        print(d)

# print(workdir)
print('=' * 78)
print('\n')
for folder in workdir:
    filelist = []
    print('-' * 78)
    print(folder)
    print('-' * 78)
    wf = os.listdir(folder)
    wf.sort()
    total_files = len(wf)
    print("Files found:", total_files)
    for f in wf:
        if os.path.isdir(os.path.join(folder, f)):
            pass  # os.path.join(keyfiles_path, '*.key'
        elif os.path.isfile(os.path.join(folder, f)):
            # (dir_name, filename) = os.path.split(f)
            (n, x) = os.path.splitext(f)
            x.lower()
            # print(x)
            if x in Files_Video:
                filelist.append(f)
                print(f)
    if len(filelist) > 0:
        print(filelist)
        pln = os.path.join(folder, '_playlist.mpcpl')
        print(pln)
        if os.path.isfile(pln) and overwrite == 0:
            print('_playlist already exist!')
        elif not path.isfile(pln) or overwrite == 1:
            print('*** overwrite! ***')
            try:  # ###[ save list as text playlist ]####################################
                with open(pln, 'wt', encoding='utf-8', newline='\n') as pw:
                    pw.write('MPCPLAYLIST\n')
                    for count, line in enumerate(filelist):
                        tmp_txt = []
                        (subN, lineX) = os.path.splitext(line)
                        count += 1
                        # print(count, line)
                        pva = str(count) + ',type,0\n'
                        pw.write(pva)
                        pva = str(count) + ',filename,' + line + '\n'
                        pw.write(pva)
                        for xtx in Files_Subtitle:
                            testname = subN + xtx
                            sub = os.path.join(folder, testname)
                            # print('test: ' + sub)
                            if os.path.isfile(sub):
                                print('Found file: ' + sub)
                                pva = str(count) + ',subtitle,' + testname + '\n'
                                pw.write(pva)
            except Exception as err:
                print('There was some error in the file operations.')
                print(err)
                print(type(err).__name__)
# exit()

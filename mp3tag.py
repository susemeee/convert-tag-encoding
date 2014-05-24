# -*- coding: utf-8 -*-
from mutagen._id3util import ID3NoHeaderError
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import os

def convert(string):
    try:
        # determine if unicode string or not
        string.encode('latin-1').decode('utf-8')
    except (UnicodeDecodeError, UnicodeEncodeError):
        try:
            string = string.encode('latin-1').decode('cp949')
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass
    return string

if __name__ == "__main__":
    try:
        filepath = sys.argv[1]
    except KeyError:
        print "{0} [filepath]".format(sys.argv[0])
        exit(0)

for d in os.listdir(filepath):
    path = os.path.join(filepath,d)
    if os.path.isfile(path) and path.endswith('mp3'):
        print d
        try:
            mp3 = EasyID3(path)
            mp3['artist'] = convert(mp3['artist'][0])
            mp3['title'] = convert(mp3['title'][0])
            mp3['album'] = convert(mp3['album'][0])

            mp3.save()
        except (ID3NoHeaderError, KeyError):
            print "(No ID3 tag present in this MP3 file)"

# print EasyID3.valid_keys.keys()

# from mutagen.easyid3 import EasyID3
# filepath = "/Users/Susemi/Desktop"
# import os
# mp3 = EasyID3(os.path.join(filepath, "들었다 놨다.mp3"))
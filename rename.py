import os

print("Begin")

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)
    os.rename(f, f.replace("[SPOTIFY-DOWNLOADER.COM]", ""))
    
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)

print("End")

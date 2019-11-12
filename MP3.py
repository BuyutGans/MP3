import os
def jalan():
  biru = "33[0;36m"
  hijau = ""
  print (20*biru + "=")
  print('+Tools Download Mp3+')
  print('+Sederhana         +')
  print('+Autho:Buyut       +')
  print(20*biru + '=')
  l = input('Link Youtubenya: ')
  os.system("youtube-dl --extract-audio --audio-format mp3 " + l)

print("Install Bahan? Y/T")
c = input("")
if c == Y | c == y:
  os.system("pkg install python2")
  os.system("pip2 install youtube-dl")
  jalan()
else:
  jalan()

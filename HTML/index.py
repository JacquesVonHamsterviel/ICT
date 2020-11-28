import time
date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
file=open("cache.html", "r")
cache=file.read()
file.close()
new=cache+"\n<br><a href\""+date+".HTML \" target= \"_blank\" class=\"mnav c-font-normal c-color-t\">"+date+"</a><br>"
print(new)

index=new+"\n</body>\n</html>"
file=open("cache.html", "r")
file.write(new)
file.close()
with open("index.html", "r")as f2:
    f2.write(index)


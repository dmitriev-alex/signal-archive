def convert(enc):
    buf = bytearray()
    idx = 10
    while idx < len(enc):
        b = 0
        if enc[idx] == "?":
            break
        elif enc[idx] == "=":
            b = int(enc[idx+1:idx+3], 16)
            idx = idx + 3
        else:
            b = ord(enc[idx])
            idx = idx + 1
        buf.append(b)
    return str(buf, "utf-8")
        
    
lines = list()
with open("headers.txt", "r") as f:
    s = f.readline()
    while s:
        if s[:9] == "Subject: ":
            s2 = f.readline()
            line = "\"" + convert(s[9:]) + "\"," + s2[47:57] + "\n"
            lines.append(line)
        s = f.readline()

with open("links.csv", "w") as f:
    f.writelines("title,id\n")
    f.writelines(reversed(lines))

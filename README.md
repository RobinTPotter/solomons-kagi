# New Running Instructions

```
# docker run -p 3000:3000 --rm  -d lscr.io/linuxserver/webtop:ubuntu-icewm
# and visit http://localhost:3000
# open a terminal

sudo apt update && sudo apt upgrade && sudo apt install git python3-opengl python3-pygame
git clone https://github.com/robintpotter/solomons-kagi
cd solomons-kagi/SolomonsKey
python3 SolomonsKey.py

# keys QAOPM
```



# Past Advice for Windows Users 
## (Now you're stuffed)

```
OpenGL.error.NullFunctionError: Attempt to call an undefined function glutInit,
check for bool(glutInit) before calling
```

can be solved using the [unofficial binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

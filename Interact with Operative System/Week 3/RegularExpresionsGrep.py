#usaremos grep

#para ver si la string está presente

from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "./loren.txt")

# @itorlou ➜ /workspaces/CourseraPython/Interact with Operative System/Week 3 (main) $ grep at loren.txt

# exercitation
# consequat
# voluptate
# fugiat
# pariatur
# occaecat
# cupidatat

# para que no sea case sensitive podemos usar -i 

# buscamos patrones con el .

# @itorlou ➜ /workspaces/CourseraPython/Interact with Operative System/Week 3 (main) $ grep n.m loren.txt 
# enim
# minim
# anim

# ^indica el inicio 
# 
# @itorlou ➜ /workspaces/CourseraPython/Interact with Operative System/Week 3 (main) $ grep ^s  loren.txt 
# sit
# sed
# sint
# sunt


# $ indica el final

# @itorlou ➜ /workspaces/CourseraPython/Interact with Operative System/Week 3 (main) $ grep m$ loren.txt 
# Lorem
# ipsum
# enim
# minim
# veniam
# cillum
# anim
# laborum
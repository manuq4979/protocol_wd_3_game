import time, os

PS2 = "protocol@watch_dog~#: "
s1 = "\033[34m{}".format("┌──")
s2 = "\033[32m{}".format("protocol")
s3 = "\033[34m{}".format("@")
s4 = "\033[31m{}".format("watch_dog")
s5 = "\033[34m{}".format("~")
s6 = "\033[32m{}".format(":")
s7 = "\n"
s8 = "\033[34m{}".format("└╼")
s9 = "\033[31m{}".format("#")
s10 = "\033[37m{}".format(" ")
PS1=s1+s2+s3+s4+s5+s6+s7+s8+s9+s10

path = "\033[34m{}".format(os.getcwd())
s2_1 = "\033[32m{}".format("shell")
PS3=s1+s2_1+s3+s4+s6+path+s5+s6+s7+s8+s9+s10

def set_path_PS3(cwd):
	global path, PS3
	path = "\033[34m{}".format(cwd)
	PS3=s1+s2_1+s3+s4+s6+path+s5+s6+s7+s8+s9+s10

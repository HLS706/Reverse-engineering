# -*- coding: UTF-8 -*-
#DECOMPILE BY HAMAYON KHAN
# Github   : https://github.com/HLS706
#FOR MORE INFO CONTACT ME +93744040422

import os, base64, sys, time
import marshal, zlib, binascii, lzma, bz2, gzip
from pprint import pformat

# ... (Emoji list, colors, snippets, logo, and printer function)
# Emoji unicode list
alphabet = [
    "\U0001f600",  # ð
    "\U0001f603",  # ð
    "\U0001f604",  # ð
    "\U0001f601",  # ð
    "\U0001f605",  # ð
    "\U0001f923",  # ð¤£
    "\U0001f602",  # ð
    "\U0001f609",  # ð
    "\U0001f60A",  # ð
    "\U0001f61b",  # ð
    "\U0001F5FF",  # ð¿ (Emoji Batu)
]

MAX_STR_LEN = 70
OFFSET = 10

# Basic colors
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
white="\033[0;37m"

# Snippets
ask = green + '\n[' + white + '?' + green + '] '+ yellow
success = green + '\n[' + white + 'â' + green + '] '
error = red + '\n[' + white + '!' + red + '] '
info= yellow + '\n[' + white + '+' + yellow + '] '+ cyan

# Current Directory
pwd=os.getcwd()

# Logo of Enc-Moji
logo = f"""
{white}ââ     â³â³â  â¢â¢
{green}â£ ââââââââââââ
{yellow}âââââ  â âââââ
{red}            â {white}[By Ferly Afriliyan]
"""

# Normal slowly printer
def sprint(sentence, second=0.05):
    for word in sentence + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(second)


# About section of script
def about():
    os.system("clear")
    sprint(logo, 0.01)
    print(f"{cyan}[ToolName]  {purple} :[Quantum]")
    print(f"{cyan}[Version]   {purple} :[1.4]")
    print(f"{cyan}[Developer] {purple} :[Ferly Afriliyan]")
    print(f"{cyan}[Github]    {purple} :[https://github.com/ferlyafriliyan]")
    print(f"{cyan}[Email]     {purple} :[ferlyafrliyn@gmail.com]\n")
    ret=input(ask+"1 for main menu, 0 for exit  > "+green)
    if ret=="1":
        main()
    else:
        exit()

# Custom path chooser
def mover(out_file):
    move= input(ask+"Move to a custom path?(y/n) > "+green)
    if move=="y":
        mpath=input(ask+"Enter the path > "+ green)
        if os.path.exists(mpath):
            os.system(f'''mv -f "{out_file}" "{mpath}" ''')
            sprint(f"{success}{out_file} moved to {mpath}\n")
        else:
            sprint(error+"Path do not exist!\n")
    else:
        print("\n")
    exit()

# Base64 encoder function
def obfuscate(VARIABLE_NAME, file_content):
    b64_content = base64.b64encode(file_content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(eval(eval(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode(eval("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38")))))'
    return code

def chunk_string(in_s, n):
    """Chunk string to max length of n"""
    return "\n".join(
        "{}\\".format(in_s[i : i + n]) for i in range(0, len(in_s), n)
    ).rstrip("\\")

# ...

# Encrypting python file into emoji
def encryptem():
    in_file = input(ask + "Input File  > " + cyan)
    if not os.path.isfile(in_file):
        print(error + ' File not found')
        os.system("sleep 2")
        encryptem()

    out_file = input(ask + "Output File  > " + green)
    with open(in_file, 'rb') as in_f, open(out_file, "w", encoding="utf-8") as out_f:
        out_f.write("# Encrypted By : Quantum\n# Github : https://github.com/ferlyafriliyan\n")
        out_f.write(encode_string(in_f.read(), alphabet))
    sprint(f"{success}{out_file} saved in {pwd}")
    mover(out_file)

# ...

def encode_string(in_s, alphabet):
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    in_s = marshal.dumps(in_s)
    in_s = zlib.compress(in_s)
    in_s = binascii.hexlify(in_s).decode()
    in_s = lzma.compress(in_s.encode())
    in_s = bz2.compress(in_s)
    in_s = gzip.compress(in_s)
    return (
        'eval(exec(eval("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
        '"{}"\n.split("  ")]))))))\n'.format(
            pformat(d2),
            chunk_string(
                "  ".join(" ".join(d1[int(i)] for i in str(i)) for i in in_s),
                MAX_STR_LEN,
            ),
        )
    )

# ...

# Encrypting python file into emoji
def encryptem():
    in_file = input(ask + "Input File  > " + cyan)
    if not os.path.isfile(in_file):
        print(error + ' File not found')
        os.system("sleep 2")
        encryptem()

    out_file = input(ask + "Output File  > " + green)
    with open(in_file, 'rb') as in_f, open(out_file, "w", encoding="utf-8") as out_f:
        out_f.write("# Encrypted By : Quantum\n# Github : https://github.com/ferlyafriliyan\n")
        out_f.write(encode_string(in_f.read(), alphabet))
    sprint(f"{success}{out_file} saved in {pwd}")
    mover(out_file)

# ...

def encode_string(in_s, alphabet):
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    return (
        'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
        '"{}"\n.split("  ")])))\n'.format(
            pformat(d2),
            chunk_string(
                "  ".join(" ".join(d1[int(i)] for i in str(i)) for i in in_s),
                MAX_STR_LEN,
            ),
        )
    )

# ...


def encode_string(in_s, alphabet):
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    return (
        'eval(exec(eval("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
        '"{}"\n.split("  ")])))))\n'.format(
            pformat(d2),
            chunk_string(
                "  ".join(" ".join(d1[int(i)] for i in str(i)) for i in in_s),
                MAX_STR_LEN,
            ),
        )
    )


# ...

def encode_string(in_s, alphabet):
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    return (
        'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
        '"{}"\n.split("  ")])))\n'.format(
            pformat(d2),
            chunk_string(
                "  ".join(" ".join(d1[int(i)] for i in str(i)) for i in in_s),
                MAX_STR_LEN,
            ),
        )
    )

# ...

# Encrypting python file into base64 variable, easily decryptable
def encryptvar():
    var = input(ask + "Variable to be used(Must Required)  > " + green)
    if var == "":
        sprint(error + " No variable")
        os.system("sleep 3")
        encryptvar()
    if var.find(" ") != -1:
        sprint(error + " Only one word!")
        os.system("sleep 3")
        encryptvar()
    iteration = input(ask + "Iteration count for variable  > " + green)
    try:
        iteration = int(iteration)
    except Exception:
        iteration = 50
    VARIABLE_NAME = var * iteration
    in_file = input(ask + "Input file  > " + cyan)
    if not os.path.isfile(in_file):
        print(error + ' File not found')
        os.system("sleep 2")
        encryptvar()
    out_file = input(ask + "Output file  > " + green)
    with open(in_file, 'r', encoding='utf-8', errors='ignore') as in_f, open(out_file, 'w') as out_f:
        file_content = in_f.read()
        obfuscated_content = obfuscate(VARIABLE_NAME, file_content)
        out_f.write("# Encrypted By : Ferly Afriliyan\n# Github : https://github.com/ferlyafriliyan\n" + obfuscated_content)
    sprint(f"{success}{out_file} saved in {pwd}")
    mover(out_file)

# ...



# Main function
def main():
    os.system("clear")
    sprint(logo, 0.01)
    print(f"{green}[1]{yellow} Encrypt{cyan} Python into Variable")
    print(f"{green}[2]{yellow} Encrypt{cyan} Python into Emoji")
    print(f"{green}[3]{yellow} About Me")
    print(f"{green}[0]{yellow} Exit")

    while True:
        choose = input(f"{ask}{blue}Choose an option : {cyan}")

        if choose == "1" or choose == "01":
            encryptvar()
        elif choose == "2" or choose == "02":
            encryptem()
        elif choose == "0":
            exit()
        else:
            sprint(error + 'Wrong input!')
            exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sprint(info + "Thanks for using. Have a good day!")
        exit()
    except Exception as e:
        sprint(error + str(e))
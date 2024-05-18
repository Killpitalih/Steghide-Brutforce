import subprocess
import sys


class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'


def extrackdata(commands):
    with open(commands["wordlist"], "r", encoding="latin-1") as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()

        result = subprocess.run(
            ["steghide", "extract", "-sf", commands["file"], "-p", password],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if result.returncode == 0:
            print(bcolors.OKGREEN, f"Password found and file extracted: {password}", bcolors.ENDC)
            return
        else:
            if commands["vision"]:
                print(bcolors.BOLD, bcolors.FAIL, f"Incorrect: {password}", bcolors.ENDC)


commands = {
    "wordlist": None,
    "file": None,
    "vision": False
}
arguments = sys.argv
if len(arguments) > 1:
    for i in arguments[1:]:
        command = i.split("=")
        if command[0] == "-w":
            commands["wordlist"] = command[1]
        elif command[0] == "-f":
            commands["file"] = command[1]
        elif command[0] == "-v":
            commands["vision"] = True

extrackdata(commands)

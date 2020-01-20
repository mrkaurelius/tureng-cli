import subprocess
from shlex import split


def choose_word():
    path = "" # bunu kullan
    command = "cat"
    wordlist = "eng_tur.txt"
    to_stdout = command + " " + wordlist

    cat_process = subprocess.Popen(split(to_stdout), stdout=subprocess.PIPE)
    fzf_process = subprocess.Popen(split("fzf"), stdin=cat_process.stdout,
            stdout=subprocess.PIPE)

    out, err = fzf_process.communicate(timeout=15)


    if err is not None:
        print("hata olustu")
    else:
        return out.decode("utf-8")

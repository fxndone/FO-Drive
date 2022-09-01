from core import *

import getpass
import shutil
import os

def main():
    print_banner()
    print()
    print()
    print("[+] Welcome to FO - Drive !")
    print("[+] This tool let you save all your datas in a remote place, without needing a hard setup !")
    print()

    print("[+] Credentials found :")
    print(f"\tUser name        : {USER}")
    print(f"\tURL              : {URL}")
    print(f"\tOutput directory : {DIR}")
    print()

    PASS = getpass.getpass("[?] Please enter the password you configured on your server : ")

    connection = DriveClient(PASS)

    print("[+] Connection established !")
    print()
    print(f"[+] Extracting server drive onto {DIR}, please wait...")

    output = connection.get_file()

    print(f"[+] Extracting {output} on {DIR}...")

    delet_directory(DIR)
    os.mkdir(DIR)

    extract_zip(output, DIR)

    print("[+] Done !")
    print(f"[+] You can now edit all files in {DIR}, and once finished, press enter on that program.")

    try:
        input(">> ")
    except KeyboardInterrupt:
        pass
    except EOFError:
        pass

    print("[+] Uploading back files, please wait...")

    output = make_zip("output", DIR)

    if not output:
        print("[!] Could not create zip !")
        print("[!] PLease save your files another way !")
        full_exit()

    connection.send_file(output)

    print("[+] Files upload sucess !")
    print("[+] Deleting temp dirs...")

    clear_dirs()
    delet_directory(DIR)

    print("[+] Directories delet sucessfull !")
    print("[+] Thanks for using !")

    full_exit()

if __name__ == "__main__":
    main()

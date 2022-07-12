from . import *
from requests.auth import HTTPBasicAuth

import requests
import os

class DriveClient:
    def __init__(self, password):
        self.url = URL
        self.auth = HTTPBasicAuth(USER, password)
        if not self.test_connection():
            print(f"[!] Could not connect to {self.url} !")
            full_exit()

    def get_base_url(self):
        return '/'.join(self.url.split('/')[:3]) + '/'

    def test_connection(self):
        try:
            requests.get(self.get_base_url(), auth=self.auth)
            return True
        except requests.ConnectionError:
            return False

    def get_file(self):
        if not self.test_connection():
            print("[!] Could not perform request !")
            return False
        response = requests.get(self.url, stream=True, auth=self.auth)
        output = extract_filename(response.headers)
        if not output:
            print("[!] Could not extract file from this URL !")
            print("[!] Please verify your URL !")
            full_exit()
        print_length = 50
        temp_dir = generate_temp_dir()
        with open(os.path.join(temp_dir, output), "wb+") as f:
            print(f"[+] Downloading {output}...")
            total_length = response.headers.get('content-length')

            if total_length is None:
                f.write(response.content)
                print(f"[+] {output} [{'=' * print_length}] 100 %")
                print("[+] Done !")
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(print_length * dl / total_length)
                    percent = int(round(dl * 100 / total_length))
                    if not done:
                        done = 1
                    print(
                        f"[+] {output} [{'=' * (done - 1)}{'>' if done != print_length else '='}{' ' * (print_length - done)}] {percent} %",
                        end='\r'
                    )
                print()
                print("[+] Done !")
        return os.path.join(temp_dir, output)

    def send_file(self, filepath):
        files = {'file': open(filepath, 'rb')}

        output = requests.post(self.url, files=files, auth=self.auth)

        return output.ok
import threading
import time

def download_file(filename):
    print(f"Starting download of {filename}")
    time.sleep(2)  # Simulando o tempo de download
    print(f"Download of {filename} complete!")

if __name__ == "__main__":
    threads = []
    files = ["file1.txt", "file2.txt", "file3.txt"]

    for file in files:
        thread = threading.Thread(target=download_file, args=(file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
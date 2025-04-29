import pyperclip
import time

pyperclip.copy("")

def cut_url(url):
    base_url = url.split("/products")[0]
    return base_url

def log_clipboard():
    prev_clip = ""
    urls = []  # Initialize the list outside the loop
    print("Clipboard logger activated. Ctrl+C to stop")
    
    try:
        while True:
            cur_clip = pyperclip.paste()
            if cur_clip != prev_clip and cur_clip.strip():
                urls = cur_clip.splitlines()
                prev_clip = cur_clip
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Script stopped. Cutting URLs...")
        return urls  # Return the collected URLs

if __name__ == "__main__":
    captured_urls = log_clipboard()  # Capture the returned URLs
    if captured_urls:  # Only proceed if URLs were captured
        cut_urls = [cut_url(url) for url in captured_urls]
        
        with open("cut_urls.txt", "w") as f:
            f.write("\n".join(cut_urls))
        
        print(f"{len(cut_urls)} URLs are cut and saved to cut_urls.txt.")
    else:
        print("No URLs were captured.")

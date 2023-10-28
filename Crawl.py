#Web crawler
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import webbrowser

def crawl():
    # URLs are now split by newline
    start_urls = start_url_entry.get().split('\n')  # Change here for enter-separated URLs
    max_pages_per_url = int(max_pages_entry.get())
    max_urls_to_crawl = int(max_urls_entry.get())
    visited_urls = set()
    crawled_urls = 0

    def open_url(event):
        """Open a URL in the default web browser."""
        webbrowser.open(event.widget.tag_names(tk.CURRENT)[0])

    def recursive_crawl(url, max_pages):
        nonlocal crawled_urls

        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            for link in soup.find_all("a"):
                href = link.get("href")
                if href and href.startswith("http"):
                    output_text.insert(tk.END, href + '\n', href)
                    output_text.tag_bind(href, "<Double-Button-1>", open_url)
                    output_text.tag_configure(href, foreground="blue", underline=True)

            visited_urls.add(url)
            crawled_pages = 1

            for link in soup.find_all("a"):
                href = link.get("href")
                if href and href.startswith("http") and href not in visited_urls and crawled_pages < max_pages:
                    recursive_crawl(href, max_pages - crawled_pages)
                    crawled_pages += 1

            crawled_urls += 1
            if crawled_urls >= max_urls_to_crawl:
                output_text.insert(tk.END, f"Reached the maximum of {max_urls_to_crawl} URLs. Stopping.\n")
                return

        except requests.exceptions.RequestException as e:
            error_message = f"Error crawling {url}: {str(e)}"
            output_text.insert(tk.END, error_message + '\n')
            messagebox.showerror("Crawling Error", error_message)

    output_text.delete(1.0, "end")

    for url in start_urls:
        if crawled_urls >= max_urls_to_crawl:
            output_text.insert(tk.END, f"Reached the maximum of {max_urls_to_crawl} URLs. Stopping.\n")
            break
        recursive_crawl(url, max_pages_per_url)

def start_crawl():
    global output_text
    output_win = tk.Toplevel(root)
    output_win.title("Crawler Output")
    output_win.geometry("500x400")
    output_win.configure(bg="#e6e6fa")

    output_text = tk.Text(output_win, height=15, width=50, bg="#f5f5f5")
    output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    output_text.insert(tk.END, "Loading...\n")

    crawl_thread = threading.Thread(target=crawl)
    crawl_thread.start()

    root.after(100, check_crawl_status, crawl_thread)

def check_crawl_status(crawl_thread):
    if crawl_thread.is_alive():
        root.after(100, check_crawl_status, crawl_thread)
    else:
        pass

root = tk.Tk()
root.title("Web Crawler")
root.minsize(400, 400)
root.configure(bg="#e6e6fa")

style = ttk.Style()
style.configure("TButton", padding=5, relief="flat", background="#0073e6", foreground="black", font=("Arial", 12, "bold"))
style.configure("TEntry", padding=5, relief="flat", font=("Arial", 12))
style.configure("TLabel", foreground="black", font=("Arial", 12, "bold"), background="#e6e6fa")

start_url_label = ttk.Label(root, text="Enter starting URLs:")  # Updated text
start_url_label.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

start_url_entry = ttk.Entry(root, width=50)
start_url_entry.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

max_pages_label = ttk.Label(root, text="Enter maximum pages to crawl for each URL:")
max_pages_label.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

max_pages_entry = ttk.Entry(root)
max_pages_entry.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

max_urls_label = ttk.Label(root, text="Enter maximum number of URLs to crawl:")
max_urls_label.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

max_urls_entry = ttk.Entry(root)
max_urls_entry.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

crawl_button = ttk.Button(root, text="Crawl", command=start_crawl)
crawl_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

root.mainloop()

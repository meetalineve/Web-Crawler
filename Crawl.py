#Web Crawler 
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

def create_output_window():
    output_window = tk.Toplevel(root)
    output_window.title("Crawling Output")

    output_text = tk.Text(output_window, height=15, width=50)
    output_text.pack(fill=tk.BOTH, expand=True)

    return output_text

def crawl():
    start_urls = start_url_entry.get().split(',')
    max_pages_per_url = int(max_pages_entry.get())
    max_urls_to_crawl = int(max_urls_entry.get())

    visited_urls = set()
    crawled_urls = 0

    def recursive_crawl(url, max_pages):
        nonlocal crawled_urls

        try:
            response = requests.get(url)
            if response.status_code != 200:
                return

            soup = BeautifulSoup(response.text, "html.parser")

            # Extract and print links
            for link in soup.find_all("a"):
                href = link.get("href")
                if href and href.startswith("http"):
                    output_text.insert(tk.END, href + '\n')

            visited_urls.add(url)
            crawled_pages = 1

            # Recursively crawl linked URLs
            for link in soup.find_all("a"):
                href = link.get("href")
                if href and href.startswith("http") and href not in visited_urls and crawled_pages < max_pages:
                    recursive_crawl(href, max_pages - crawled_pages)
                    crawled_pages += 1

            crawled_urls += 1
            if crawled_urls >= max_urls_to_crawl:
                output_text.insert(tk.END, f"Reached the maximum of {max_urls_to_crawl} URLs. Stopping.\n")
                return

        except Exception as e:
            output_text.insert(tk.END, f"Error crawling {url}: {str(e)}\n")

    # Clear the text widget before crawling
    output_text.delete(1.0, "end")

    # Crawl each of the specified URLs
    for url in start_urls:
        if crawled_urls >= max_urls_to_crawl:
            output_text.insert(tk.END, f"Reached the maximum of {max_urls_to_crawl} URLs. Stopping.\n")
            break
        recursive_crawl(url, max_pages_per_url)

# Create the main window
root = tk.Tk()
root.title("Web Crawler")

# Set minimum size for the window
root.minsize(400, 400)

# Create and configure GUI elements for the main window
style = ttk.Style()
style.configure("TButton", padding=5, relief="flat", background="#008CBA", font=("Arial", 12, "bold"))
style.configure("TEntry", padding=5, relief="flat", font=("Arial", 12))
style.configure("TLabel", foreground="black", font=("Arial", 12, "bold"))

start_url_label = ttk.Label(root, text="Enter starting URLs separated by commas:")
start_url_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

start_url_entry = ttk.Entry(root)
start_url_entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

max_pages_label = ttk.Label(root, text="Enter maximum pages to crawl for each URL:")
max_pages_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

max_pages_entry = ttk.Entry(root)
max_pages_entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

max_urls_label = ttk.Label(root, text="Enter maximum number of URLs to crawl:")
max_urls_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

max_urls_entry = ttk.Entry(root)
max_urls_entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Create a "Crawl" button
crawl_button = ttk.Button(root, text="Crawl", command=crawl)
crawl_button.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create an "Open Output Window" button
def open_output():
    global output_text
    output_text = create_output_window()
open_output_button = ttk.Button(root, text="Open Output Window", command=open_output)
open_output_button.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Configure grid weights to allow resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

root.mainloop()

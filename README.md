# Web-Crawler
A web crawler, in short, is a software program that automatically navigates the internet, visiting web pages and collecting information, such as links and content, for various purposes like indexing, data retrieval, or analysis.
In the code for a web crawler with a GUI interface, several functionalities are implemented or studied. Here's a brief description of each:
User Input of URLs: Implemented - Users can input one or more starting URLs separated by commas.
User Input of Maximum Pages to Crawl: Implemented - Users can specify the maximum number of pages to crawl for each URL.
User Input of Maximum URLs to Crawl: Implemented - Users can specify the maximum number of URLs to crawl in total.
Crawling Logic: Implemented - The code includes the core logic for crawling web pages, extracting links, and recursively crawling linked URLs up to the specified depth.
Displaying Crawling Output: Implemented - The code opens a new window to display the crawling output in a text area.
Styling and Aesthetics: Implemented - The GUI is styled using the ttk theme and proper font attributes to enhance aesthetics.
Button Actions: Implemented - Buttons for "Crawl" and "Open Output Window" have associated actions to trigger the crawling and display of the output window.
Error Handling: Implemented - The code includes basic error handling to catch exceptions while crawling.
Proper Structure and Organization: Implemented - The code is organized into functions for readability and maintainability.
Window Resizing: Implemented - The main window is resizable, and elements adapt to window resizing.

In the web crawling application, several data structures are used to manage and process data efficiently:

Lists and Sets:
Lists are used to store the starting URLs provided by the user and manage the order in which URLs are crawled.
Sets (specifically, visited_urls) are used to keep track of visited URLs to avoid revisiting the same URL.

Text Area (Output Display):
A text widget (a data structure provided by the GUI library) is used to display the collected web links. This widget stores and manages the text data that is displayed in the output window.

Dictionary (Style Configuration):
Dictionaries are not explicitly shown in the code, but they are likely used internally by the ttk.Style object to store style configurations for different GUI elements (e.g., buttons, labels).

Exception Handling:
Exception objects are used to capture and handle errors during the crawling process. While not a typical data structure, it's a fundamental part of error management in the code.

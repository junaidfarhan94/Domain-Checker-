Domain Reachability Checker

Overview
Domain Reachability Checker is a powerful Python tool designed to quickly and efficiently verify the reachability of domains. This tool is optimized for speed and provides a stylish and user-friendly interface, making it an ideal choice for network administrators, security professionals, and anyone who needs to perform domain checks on a regular basis.

Features
Multi-Method Reachability Check: Verifies domains using DNS resolution, ICMP ping, and HTTP/HTTPS requests to ensure comprehensive reachability analysis.
Fast and Efficient: Utilizes multi-threading to check multiple domains simultaneously, significantly reducing check time.
Stylish Interface: Displays a visually appealing opening screen with ASCII art and custom colors for output, making the tool both functional and aesthetically pleasing.
Customizable Output: Reachable domains are saved to reachable.txt, while the terminal output is color-coded for easy interpretation.
User-Friendly: Simple command-line interface with clear instructions and informative error messages.


Installation
To get started with the Domain Reachability Checker, you'll need to have Python 3 installed along with a few Python libraries. Install the required libraries using pip:

pip3 install requests pyfiglet termcolor

Usage
Prepare Your Domain List: Create a domains.txt file in the same directory as the script. List each domain on a new line, e.g.:

www.google.com
www.example.com
www.github.com



Run the Script: Execute the script using Python:

python3 check_domains.py

Review Results:

Reachable domains will be listed in reachable.txt.
The terminal will display color-coded results indicating which domains are reachable or not.
Example Output

  ____                        _   _             _             
 |  _ \  ___  _ __ ___   __ _| | | | __ _ _ __ | | _____ _ __ 
 | | | |/ _ \| '_ ` _ \ / _` | |_| |/ _` | '_ \| |/ / _ \ '__|
 | |_| | (_) | | | | | | (_| |  _  | (_| | | | |   <  __/ |   
 |____/ \___/|_| |_| |_|\__,_|_| |_|\__,_|_| |_|_|\_\___|_|   

                        By Junaid Farhan
            https://www.instagram.com/jdf_000/
============================================================

www.google.com is reachable.
www.nonexistentdomain.com is not fully reachable.

Check complete! Reachable domains saved to reachable.txt

Future Enhancements
Smart GUI Integration: Plans to incorporate a graphical user interface (GUI) using Tkinter or PyQt for a more interactive experience.
Customizable Themes: Potential to allow users to select different color schemes and fonts for terminal output.
Extended Protocol Support: Future updates may include checks for additional protocols such as FTP and SSH.
Logging and Reporting: Adding logging functionality to keep a detailed history of domain checks.
Credits
Created by Junaid Farhan
(https://www.instagram.com/jdf_000/)

License
This project is licensed under the MIT License. See the LICENSE file for details.

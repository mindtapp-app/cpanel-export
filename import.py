import re
import os
import glob
import subprocess
from urllib.parse import unquote

regex = '"https://mindtapp\\.com/[^# ]+"'
files_to_check = ['index.html']
files_to_check.extend(glob.glob(os.path.join('**', 'index.html'), recursive=True))

found_matches = False
for filepath in files_to_check:
    if os.path.exists(filepath) and os.path.isfile(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                matches = re.findall(regex, content)
                if matches:
                    for match in matches:
                        url = unquote(match[1:-1]) # remove trailing and leading "
                        if "gallery" in url: print(url)
                        # split up string so it doesn't get caught in Find/Replace operations
                        filepath = re.sub("\\?.*", "", url.replace("https://"+"mindtapp.com/", ""))
                        subprocess.run(['curl', '-k', url, '-o', filepath, '--create-dirs'])
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

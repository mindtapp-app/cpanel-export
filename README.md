# cpanel export

Afterwards, need to run Find Replace in Files (regex)
```
Find:     https://Z?mindtapp.com/(Our-Clients|Contacts|Privacy-Policy|About-Us)
Replace:  /cpanel-export/$1
```

Then run `import.py`

Then run Find Replace in Files
```
Find:    https://Z?mindtapp.com/
Replace: /cpanel-export/
```


alternatively use `refresh.bat` then find replace
```
/[A-Za-z ]+_filesZ?/
/index_files/
```

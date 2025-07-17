# cpanel export

Afterwards, need to run Find Replace in Files (regex)
```
Find:     https://Z?mindtapp.com/(Our-Clients|Contacts|Privacy-Policy|About-Us)
Replace:  ./$1
```

Then run `import.py`

Then run Find Replace in Files
```
Find:    https://Z?mindtapp.com/
Replace: ./
```


alternatively use `refresh.bat` then find replace
```
/.+_filesZ?/
./index_files/
```

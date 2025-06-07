# url2katana
simple python tool to convert urls.txt into katana.jsonl
To run
```
python3 katanaconvert.py
```

or use this codeline (one line command)
```
awk '{print "{\"request\":{\"url\":\"" $0 "\"}}"}' urls.txt > katana.jsonl

```

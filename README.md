# Profanity-Checker
This is a small upgrade to the already existing PyPI package "profanity-filter"...

#  Usage and Installation: 

### For Linux:
```bash
$ git clone https://github.com/AakashSundarS/Profanity-Checker.git
$ chmod +x requirements.sh
$ ./requirements.sh
$ cd Profanity-Checker/
$ python ./profanityChecker.py
```

### For Windows and Mac:
```bash
$ pip install profanity-filter
$ python -m spacy download en
$ git clone https://github.com/AakashSundarS/Profanity-Checker.git
$ cd Profanity-Checker/
$ python ./profanityChecker.py
```


## Example Program:
```python    
from profanityChecker import isProfane
    
raw_para = input('Type a message: ')
if isProfane(raw_para):
    print("Warning!... Profanity Detected!...")
    para = advCensor(raw_para)
    print(para)
else:
    print(para)
```

# Profanity-Checker
    This is a small upgrade to the already existing PyPI package "profanity-filter"...

# Installation: 

### For Linux:
    1.First run the "requirements.sh" script in your bash terminal:
```bash
$ chmod +x requirements.sh
$ ./requirements.sh
$ git clone https://github.com/AakashSundarS/Profanity-Checker.git
```

### For Windows and Mac:
    Run the following commands:
```bash
$ pip install profanity-filter
$ python -m spacy download en
$ git clone https://github.com/AakashSundarS/Profanity-Checker.git
```

# Usage:
    First change your directory into the folder...
```bash
$ cd Profanity-Checker/
$ python ./profanityChecker.py
```

### Example Program:
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

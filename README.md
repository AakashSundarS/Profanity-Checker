# Profanity-Checker
    This is a small upgrade to the already existing PyPI package "profanity-filter"...

# Dependencies: 
    1.First run the "requirements.sh" script in your bash terminal like this:
```bash
        $ ./requirements.sh
```
###                                or
    Run the following commands:
```bash
        $ pip install profanity-filter
        $ python -m spacy download en
```

# Usage:
    First change your directory into the folder...
```bash
        $ cd Profanity-Checker/
```

### Example Program:
```python    
    from profanityChecker import isProfane
    
    para = input("Enter any string: ")
    print(isProfane(para))
    # Output: True
```

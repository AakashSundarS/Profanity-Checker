# Profanity-Checker
    This is a small upgrade to the already existing PyPI package "profanity-filter"...

# Dependencies: 
    1.First run the "requirements.sh" script in your bash terminal like this:
        $ ./requirements.sh
                                or
    Run the following commands:
        $ pip install profanity-filter
        $ python -m spacy download en

# Usage:
    from profanityChecker import isProfane
    
    para = input("Enter any string: ")
    print(isProfane(para))
    # Output: True

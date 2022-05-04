# Testing

## Code validators

[PEP8 Validator Results](docs/img/PEP8_results.jpg): 

All errors were fixed using PEP8 except for two lines of code:
- Code E501 (line too long > 79 characters)
    - These lines of code are in a if statment which if idented crashes the program from running. I tried varies ways to make the identation work in order for it to clear PEP8 validation but had no success. In order to avoid crashing the program it was best to keep the errors. 

## PROBLEMS

[run.py file problems](docs/img/problems_image.jpg):

Within the terminal in the problems column I currently have 27 problems, which are as follows:
- 13 total: pylint(no-member) [pylint(no-member)](https://www.lesinskis.com/pylint-false-positives.html)
    - ***However since Python is so dynamic there's a whole bunch of ways in which you can dynamically define members of a class, and Pylint won't always catch these.***
    - For this reason I decided to ignore pylint due to the many changes I would have to make to my code which could result in it crashing.

- 5 total: pylint(arguments-renamed)
    - I avoided this problem after reading how complicated it would be to fix it to my understanding.
    - [Example of W0237](https://pylint.pycqa.org/en/latest/messages/warning/arguments-renamed.html)

- 4 total: Missing function or method docstring ***pylint(missing-function-docstring)***
    - A docstring was issued above these 4 functions in it's parent Laser class which is line 36.

- 5 total: Argument name "x" doesn't conform to snake_case naming style ***pylint(invalid-name)***
    - At the time of writing it was more difficult to change the code to meet this standard so I left it as is. 
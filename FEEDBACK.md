

- [PA 4 Feedback](#pa-4-feedback)
  - [Comments](#comments)
  - [Format / Design](#format--design)
  - [Correctness / Completeness](#correctness--completeness)
  - [Usability](#usability)
  - [Supporting Documents](#supporting-documents)
  - [Comments on the grading](#comments-on-the-grading)
  - [Grade:](#grade)
  - [Participation Grade:](#participation-grade)


## PA 4 Feedback


### Comments
| Result   | Description                                   |
|----------|-----------------------------------------------|
| **YES-NO**   | Intro comments complete/clear                 |
| **YES-NO**   | Function comments complete for each function  |
| **YES-NO**   | Appropriate in-line commentary                |

### Format / Design
| Result   | Description                                                                                            |
|----------|--------------------------------------------------------------------------------------------------------|
| **YES-NO**   | Proper use of upper/lowercase                                                                          |
| **YES-NO**   | Correct use of whitespace                                                                              |
| **YES-NO**   | Appropriate variable names                                                                             |
| **YES-NO**   | A function for reading in file name until it exists. Uses `os.ispath.file` in Boolean expression       |
| **YES-NO**   | A function for reading file into a list of strings. Returns list.                                      |
| **YES-NO**   | Reading file function uses try/except correctly                                                        |
| **YES-NO**   | A function for user menu and error checking that valid value given                                     |
| **YES-NO**   | A function for each analysis task (4 total functions)                                                  |
| **YES-NO**   | Uses read file function and file name input function that already exist for option to read in new file |
| **YES-NO**   | File is only read at start or when new file is requested; all analysis is on list.                     |
| **YES-NO**   | No spaghetti code (inappropriate use of break, exit, etc)                                              |

### Correctness / Completeness
| Result   | Description                                                                                                |
|----------|------------------------------------------------------------------------------------------------------------|
| **YES-NO**   | Menu provided to user for choice with 5 expected choices only                                              |
| **YES-NO**   | Program continues running until user chooses to quit                                                       |
| **YES-NO**   | User chooses name of input file, which can be any file that exists (not just the ones originally provided) |
| **YES-NO**   | Reads in input file to create a list of strings                                                            |
| **YES-NO**   | Input file is closed before file reading function returns                                                  |
| **YES-NO**   | Correctly determines how many headlines have a particular word in it, and outputs to user                  |
| **YES-NO**   | Correctly determines headlines with a particular word                                                      |
| **YES-NO**   | User chooses name of output file for outputting headlines                                                  |
| **YES-NO**   | Correct headlines written to file, one headline per line                                                   |
| **YES-NO**   | Output file is closed when writing is complete                                                             |
| **YES-NO**   | Correctly determines average number of characters per headline and outputs to user                         |
| **YES-NO**   | Correctly determines either shortest or longest headline, and outputs headline                             |
| **YES-NO**   | If user chooses to analyze a new file, the list of data is overwritten with the new data                   |
| **YES-NO**   | Code follows final algorithm                                                                               |
| **YES-NO**   | No other logic errors                                                                                      |

### Usability
| Result   | Description                                               |
|----------|-----------------------------------------------------------|
| **YES-NO**   | Outputs purpose of program at start                       |
| **YES-NO**   | Menu is easy to read                                      |
| **YES-NO**   | It is clear what to type in when making choice from menu  |
| **YES-NO**   | Prompts for input are clear                               |
| **YES-NO**   | Output is well formatted                                  |

### Supporting Documents
| Result   | Description                                               |
|----------|-----------------------------------------------------------|
| **-NO**   | Algorithm                                                 |
| **YES-**   | Reflection                                                |


### Comments on the grading
- There are so many LLM codes that I find it to grade

```python
# Purpose: Reads a file and returns a list of lines stripped of whitespace.
# Parameters: filename
# Return: A list of strings that each represent a line from the file.
def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Purpose: Counts the number of headlines that contain a specific word.
# Parameters: headlines
# Return: The count of headlines containing the specified word.
def count_word(headlines, word):
    return sum(1 for headline in headlines if word.lower() in headline.lower())

# Purpose:  Writes headlines that contain a specific word to a new file.
# Parameters: headlines, word, output_file
# Return: None
def write_headlines_with_word(headlines, word, output_file):
    with open(output_file, 'w') as file:
        for headline in headlines:
            if word.lower() in headline.lower():
                file.write(headline + '\n')

# Purpose: Calculates the average number of characters per headline.
# Parameters: headlines
# Return: The average number of characters per headline.
def average_characters(headlines):
    return sum(len(headline) for headline in headlines) / len(headlines)

# Purpose: Finds the longest and shortest headlines.
# Parameters: headlines
# Return: The longest headline and the shortest headline.
def longest_shortest_headline(headlines):
    longest = max(headlines, key=len)
    shortest = min(headlines, key=len)
    return longest, shortest


```
- 
- 

### Grade: R

### Participation Grade: U
 - If participation grade is unsatisfactory check the `NO` in the documents sections
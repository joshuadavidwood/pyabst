# PyAbst


PyAbst is a library developed to summarise text. The PyAbst algorithm ranks words according by word frequency. Each sentence is scored through summing associated word frequencies across the sentence. PyAbs allows users to amplify or suppress the weighting for specific target words. If the target word weighting is defined sufficiantly high (or low), sentences containing the target words will always be present (or absent). An interactive An interactive web-application is currently being developed and will be available shortly at [www.pyabst.com](www.pyabst.com).
<br>

### Contact Details
[pyaugment@gmail.com](pyaugment@gmail.com)

### Installation
You can install, upgrade, uninstall PyAbst using these commands:

1. `$ sudo pip install pyabst`
2. `$ sudo pip install --upgrade pyabst`
3. `$ sudo pip uninstall pyabst`

### Example Usage
<i>The value of the number pi has been calculated to a new world record length of 31 trillion digits, far past the previous record of 22 trillion. Emma Haruka Iwao, a Google employee from Japan, found the new digits with the help of the companys cloud computing service.<br>

Pi is the number you get when you divide a circles circumference by its diameter. The first digits, 3.14, are well known but the number is infinitely long. Extending the known sequence of digits in pi is very difficult because the number follows no set pattern.<br>

Pi is used in engineering, physics, supercomputing and space exploration - because its value can be used in calculations for waves, circles and cylinders. The pursuit of longer versions of pi is a long-standing pastime among mathematicians. And Ms Iwao said she had been fascinated by the number since she had been a child.<br>

The calculation required 170TB of data (for comparison, 200,000 music tracks take up 1TB) and took 25 virtual machines 121 days to complete.</i><br>
<br>
<i>Source: https://www.bbc.co.uk/news/technology-47524760</i>

#### Example 1: Default Arguments
Output: <br>

<i>The value of the number pi has been calculated to a new world record length of 31 trillion digits, far past the previous record of 22 trillion. Extending the known sequence of digits in pi is very difficult because the number follows no set pattern. Pi is used in engineering, physics, supercomputing and space exploration - because its value can be used in calculations for waves, circles and cylinders. The calculation required 170TB of data (for comparison, 200,000 music tracks take up 1TB) and took 25 virtual machines 121 days to complete.</i><br>

#### Example 2: target_words = 'Japan', word_weighting = 1000000 
Output: <br>

<i>The value of the number pi has been calculated to a new world record length of 31 trillion digits, far past the previous record of 22 trillion. Emma Haruka Iwao, a Google employee from Japan, found the new digits with the help of the companys cloud computing service. Extending the known sequence of digits in pi is very difficult because the number follows no set pattern. Pi is used in engineering, physics, supercomputing and space exploration - because its value can be used in calculations for waves, circles and cylinders.</i><br>

#### Example 3: target_words = 'number', word_weighting = -1000000 
Output: <br>

<i>Emma Haruka Iwao, a Google employee from Japan, found the new digits with the help of the companys cloud computing service. Pi is used in engineering, physics, supercomputing and space exploration - because its value can be used in calculations for waves, circles and cylinders. The pursuit of longer versions of pi is a long-standing pastime among mathematicians. The calculation required 170TB of data (for comparison, 200,000 music tracks take up 1TB) and took 25 virtual machines 121 days to complete.</i><br>

#### Smmry Comparison
When you ingest the same text into Smmry ([www.smmry.com](www.smmry.com)). with select a 5 sentence argument we find the results to match Example 3. However, PyAbs replaces <i>'The first digits, 3.14, are well known but the number is infinitely long.'</i> with <i>'And Ms Iwao said she had been fascinated by the number since she had been a child.'</i>.<br>

<i>The value of the number pi has been calculated to a new world record length of 31 trillion digits, far past the previous record of 22 trillion. Pi is the number you get when you divide a circles circumference by its diameter. The first digits, 3.14, are well known but the number is infinitely long. Extending the known sequence of digits in pi is very difficult because the number follows no set pattern.</i><br>

#### Frequently Asked Questions
Work in progress.

#### Troubleshooting
Work in progress.

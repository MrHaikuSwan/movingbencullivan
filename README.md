# MovingBenCullivan
This is a repository containing all the code I used to help my teacher move nearly 2,000 practice AP Economics test questions from a legacy website to Google Forms. First, I used Python to scrape all necessary information from the legacy website, and then I used Google Apps Script (Google's development platform derived from JavaScript built to interface with Google Apps) to convert and save that information to Google Forms.

## Downloading the Quizzes
The first thing I did was to download the raw HTML containing the data that I would need directly from the website. The website's test questions were split among many quizzes, and so I used Selenium to download the raw HTML and Pillow to download any images on the page, and stored that information in a local folder for each quiz, using a folder tree mimicking the website's design to effectively mirror the website to a local copy of it containing the things I needed. While downloading the pages was not strictly necessary, it made parsing them (in the next step) nearly instantaneous and made fixing errors that much faster. However, the folder tree was very unnecessary, and I removed it in the next step.

## Parsing and Saving the Quizzes
To interact with the raw quiz HTML in a meaningful way, I used lxml (an HTML parsing library) to extract necessary information (question text, answer choices, correct answer, correct answer explanation, etc.) and then saved each quiz in JSON format, meaning that each quiz I downloaded previously now had a new JSON file corresponding to it with exactly the same information at a fraction of the size! This size advantage would marginally speed up operations done on it, but much more important was that Google Apps Script could now understand the JSON files directly.

## Creating Google Forms
Finally, with no small amount of documentation, I learned Google Apps Script just well enough to parse my uploaded JSON files and create the Google Forms for each quiz from the data in the JSON files in an organized folder structure (runtime was about 20 minutes). Interestingly, Google Apps Script isn't actually capable of doing everything a user can, which I unfortunately learned when trying to add images to the quiz questions. 

Since many of the quiz questions required a graph or table to understand the question, this was a massive problem: however, I was able to get around it by adding the <img> tag's "src" attribute value (which was handily available in the HTML I had thought to download locally in the beginning) to the question's subtext, leaving a link the user could click on to see the picture while the legacy website was still up (and also giving my teacher an easy way to locate the corresponind pictures before the legacy website went down).

## Results
This was a massively successful endeavor to leverage programming to reduce the amount of work we have to manually do. All in all, the JSON files contained around 1,900 test questions. The development process took about 3 days from start to finish, and the time the programs needed to complete the task was about 45 minutes for all of the questions. To put that into perspective, I would conservatively estimate the time it would copy down the information for one question manually would be around 30 seconds to 1 minute. This yields a range of about 16-32 **hours** of cumulative work at peak efficiency to complete the task. On the other hand, a computer doing the same thing would operate at an average speed of ~1.5 seconds per question.

# Publishable Resources
I've uploaded all of the JSON files I used containing question data (and I have emphatically not uploaded the raw website files, as it amounts to about 22 MB) to the PublishableResources/ folder. There are two folders for two sets of quizzes: TestBanks/ is for unit-specific AP practice questions, while ReviewBanks/ is for real past AP tests to practice on at the end of the year. Since it's very difficult for a human to read the data in raw form, if you would like to see the actual quizzes stored, follow these steps:

1. Pick any .json file, open it, select all of the text, and copy it.
    * You can easily select all of the text by triple-clicking on the text.
2. Open [jsonviewer.stack.hu]
3. Paste the text from the .json file into the text box.
4. Click "Format" at the top of the page to arrange the text into a more readable format.
    * Alternatively, you can click on the Viewer tab at the very top of the page to open an unfolding tree diagram you can use to view the entire document.

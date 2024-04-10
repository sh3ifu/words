# Words

This program allows you to learn foreign words by writing and consolidating them, ensuring the expansion of vocabulary.

## Main features
- **Learning through writing**: The difference of the program is that the study of words takes place through their active writing, which allows users to fix and remember words more effectively.
- **Learning modes**: The program offers several modes, including learning a word in one language and writing a translation in another language, as well as random output of words in both languages for more variety in the learning process.
- **Manage categories and words**: User can create/delete custom categories and add/delete words in them for convenient organized learning. There is also an option to combine categories and separate words that need to be repeated.
- **Built-in translator**: The program has a built-in translator that allows you to receive translations for English-Ukrainian words to facilitate the learning process.
- **Voiceover**: There is an option to turn on voiceover for English words, allowing users to practice pronunciation and listening for words.
## Installation
1. Copy the repository to a local directory on the computer.
2. Install all necessary dependencies for the project.
3. In the root directory of the project, create a subdirectory named **_words_**. Create a **_words.json_** file in this directory. Add opening and closing curly braces _{}_ to it.
## Using
1. In order to start working with the program, you first need to create at least one category and add words to it. So, you need to run the program ```python3 words.py```, write the command ```add category``` and enter a name for the new category.
2. Next, write the command ```add words```, enter the name of the category to which you want to add words (a list of all existing categories can be displayed using ```list categories```) and enter the number of words to be added (if you want to stop adding words, enter the command ```!stop```).
3. To start learning words, enter the ```start default``` command in the program's main menu. Next, enter the name of the category and select the mode. There are **3** modes:
   - **Word - translation** - i.e. words in the language he is learning are accidentally displayed to the user, and he needs to write a translation.
   - **Translation - word** - the same only in reverse.
   - **Mixed mode** - all words are displayed. The user will need to write both words and translations.
4. You can start the translator with the ```start translator``` command. Exit with ```!stop``` command.
> To see a list of all commands, type ```help``` in the main menu of the program.

> Since the user will have to type a lot on the keyboard while learning words, it may not be convenient to constantly switch between different layouts. Therefore, the program does it on its own.
## Bugs
- The program runs on Linux. Changing the keyboard layout will not work on Windows, so the program will simply not start.

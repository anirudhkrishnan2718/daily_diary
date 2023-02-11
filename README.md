# daily_diary
latex based daily diary usable for leisure or research

## Pre-requisites
- A Latex installation and compiler which will be used to compile `main.tex`
- A Python installation to run the folder structure generation `generate_yearly_diary.py`

## Usage
1. Run the `generate_yearly_diary.py` script suppylying the `year` variable to create the top level folder `Diary_{year}` and the structure within.
2. Hardcode the document details such as `title`, `author`, `year` in the `main.tex` file and compile it.
3. Content and style have been separated in the spirit of HTML/CSS and the `Diary_{year}` folder contains only content and no style information.
4. Open the `work.tex` or `leisure.tex` files inside a given day to start adding content
5. There is a switch inside `main.tex` to pull work or leisure or both entries from each day of the year to create a collated yearly journal.

### Collating selected months or days of the month
- Finer control of which months to collate is possible by commenting out the relevant lines in `work_journal`, `leisure_journal.tex` or `combined_journal.tex` respectively.
- For even finer control at the day level, look at the files `work_summary.tex`, `leisure_summary.tex` or `full_summary.tex` located inside `./Diary_{year}/{month}`. Comment out the days you want to exclude from the collating process.

### Optional day and month level summarization
- Provide a summary for the month's activities by making entries in the above month level files.
- Provide a summary for each day's activities by making entries in the sections corresponding to each day within the above month level files.
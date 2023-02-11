"""Generate a folder structure for a given year
for use with the latex daily journal repository"""

import calendar
import os
import shutil

# Set the year for whici to generate the diary data folder
year                                        = 2023
if os.path.exists(f'./Diary_{year}'):
    shutil.rmtree(f'./Diary_{year}')
os.mkdir(f'./Diary_{year}')

# Main loop to generate the monthly summary tex files
for month in range(1, 13):
    os.mkdir(f'./Diary_{year}/{calendar.month_name[month]}')

    with open(f'./Diary_{year}/{calendar.month_name[month]}/full_summary.tex', 'w') as f2:

        f2.write(f'\chapter{{{calendar.month_name[month]}}}\n')
        for day in range(1, calendar.monthrange(year, month)[1] + 1):

            day_folder_name                     = f'./Diary_{year}/{calendar.month_name[month]}/{calendar.month_name[month]}_{day:02d}'
            os.mkdir(day_folder_name)

            f2.write(f'\t\section{{{calendar.day_abbr[calendar.weekday(year, month, day)]}, {calendar.month_abbr[month]} {day:02d}}}\n')
            f2.write(f'\t\t\input{{{day_folder_name}/work.tex}}\n')
            f2.write(f'\t\t\input{{{day_folder_name}/leisure.tex}}\n')

    with open(f'./Diary_{year}/{calendar.month_name[month]}/work_summary.tex', 'w') as f4:

        f4.write(f'\chapter{{{calendar.month_name[month]}}}\n')
        for day in range(1, calendar.monthrange(year, month)[1] + 1):

            day_folder_name                     = f'./Diary_{year}/{calendar.month_name[month]}/{calendar.month_name[month]}_{day:02d}'

            f4.write(f'\t\section{{{calendar.day_abbr[calendar.weekday(year, month, day)]}, {calendar.month_abbr[month]} {day:02d}}}\n')
            f4.write(f'\t\t\input{{{day_folder_name}/work.tex}}\n')

    with open(f'./Diary_{year}/{calendar.month_name[month]}/leisure_summary.tex', 'w') as f5:

        f5.write(f'\chapter{{{calendar.month_name[month]}}}\n')
        for day in range(1, calendar.monthrange(year, month)[1] + 1):

            day_folder_name                     = f'./Diary_{year}/{calendar.month_name[month]}/{calendar.month_name[month]}_{day:02d}'

            f5.write(f'\t\section{{{calendar.day_abbr[calendar.weekday(year, month, day)]}, {calendar.month_abbr[month]} {day:02d}}}\n')
            f5.write(f'\t\t\input{{{day_folder_name}/leisure.tex}}\n')




# Loop to generate the daily entry files which are input into the monthly summary tex files
for month in range(1, 13):
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        day_folder_name                     = f'./Diary_{year}/{calendar.month_name[month]}/{calendar.month_name[month]}_{day:02d}'

        with open(day_folder_name+'/work.tex', 'w') as f1:
            f1.write('\subsection{Meeting}\n')
        with open(day_folder_name+'/leisure.tex', 'w') as f3:
            f3.write('\subsection{Reading}\n')



    # print(f"\IfFileExists{{./Diary_{year}/{calendar.month_name[month]}/full_summary.tex}}{{\include{{./Diary_{year}/{calendar.month_name[month]}/full_summary.}}}}{{}}")
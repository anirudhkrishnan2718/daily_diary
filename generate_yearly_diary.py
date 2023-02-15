"""Generate a folder structure for a given year
for use with the latex daily journal repository"""

######################## IMPORT MODULES ############################

import calendar
import os
import shutil

######################### SET PARAMETERS ###########################

year_input = 2023
titlepage_dict = {
    "author": "Anirudh Krishnan",
    "document_title": "Daily Journal",
    "document_subtitle": f"Calendar Year {year_input}",
    "organization": "XYZ University",
    "place": "Mars",
}

sectioning_format_dict = {
    "chapter": {
        "face": r"\normalfont",
        "size": r"\Huge",
        "color": "Gray",
        "background_color": r"Black!20",
        "family": r"\sffamily",
        "colorured_text": True,
    },
    "section": {
        "face": r"\bfseries",
        "size": r"",
        "color": "Brown",
        "background_color": r"Red!20",
        "family": r"\sffamily",
        "colorured_text": True,
    },
    "subsection": {
        "face": r"\bfseries",
        "size": r"",
        "color": "OliveGreen",
        "background_color": r"Green!20",
        "family": r"\sffamily",
        "colorured_text": True,
    },
    "subsubsection": {
        "face": r"\bfseries",
        "size": r"",
        "color": "MidnightBlue",
        "background_color": r"Blue!20",
        "family": r"",
        "colorured_text": True,
    },
}


####################### CUSTOM FUNCTIONS ###########################


def create_fresh_diary_structure(year):
    """Create a blank folder structure for a yearly journal

    Args:
        year (int): year for which the journal is to be created
    """
    work_subsection_default = "Meeting"
    leisure_subsection_default = "Reading"
    placeholder_text = False

    if os.path.exists(f"./Diary_{year}"):
        shutil.rmtree(f"./Diary_{year}")
    os.mkdir(f"./Diary_{year}")

    # Main loop to generate the monthly summary tex files
    for month in range(1, 13):
        os.mkdir(f"./Diary_{year}/{calendar.month_name[month]}")

        with open(
            f"./Diary_{year}/{calendar.month_name[month]}/full_summary.tex", "w"
        ) as f2:

            f2.write(f"\chapter{{{calendar.month_name[month]}}}\n")
            for day in range(1, calendar.monthrange(year, month)[1] + 1):

                day_folder_name = f"./Diary_{year}/{calendar.month_name[month]}/{calendar.month_name[month]}_{day:02d}"
                os.mkdir(day_folder_name)
                f2.write("\t" + r"\Needspace{10\baselineskip}" + "\n")
                f2.write(
                    f"\t\fakesection{{{calendar.day_abbr[calendar.weekday(year, month, day)]}, {calendar.month_abbr[month]} {day:02d}}}\n"
                )
                f2.write(f"\t\t\input{{{day_folder_name}/work.tex}}\n")
                f2.write(f"\t\t\input{{{day_folder_name}/leisure.tex}}\n")

        with open(
            f"./Diary_{year}/{calendar.month_name[month]}/work_summary.tex", "w"
        ) as f4:

            f4.write(f"\chapter{{{calendar.month_name[month]}}}\n")
            for day in range(1, calendar.monthrange(year, month)[1] + 1):

                day_folder_name = f"./Diary_{year}/{calendar.month_name[month]}/{calendar.month_name[month]}_{day:02d}"
                f4.write("\t" + r"\Needspace{10\baselineskip}" + "\n")
                f4.write(
                    f"\t\fakesection{{{calendar.day_abbr[calendar.weekday(year, month, day)]}, {calendar.month_abbr[month]} {day:02d}}}\n"
                )
                f4.write(f"\t\t\input{{{day_folder_name}/work.tex}}\n")

        with open(
            f"./Diary_{year}/{calendar.month_name[month]}/leisure_summary.tex", "w"
        ) as f5:

            f5.write(f"\chapter{{{calendar.month_name[month]}}}\n")
            for day in range(1, calendar.monthrange(year, month)[1] + 1):

                day_folder_name = f"./Diary_{year}/{calendar.month_name[month]}/{calendar.month_name[month]}_{day:02d}"
                f5.write("\t" + r"\Needspace{10\baselineskip}" + "\n")
                f5.write(
                    f"\t\fakesection{{{calendar.day_abbr[calendar.weekday(year, month, day)]}, {calendar.month_abbr[month]} {day:02d}}}\n"
                )
                f5.write(f"\t\t\input{{{day_folder_name}/leisure.tex}}\n")

    # Loop to generate the daily entry files which are input into the monthly summary tex files
    for month in range(1, 13):
        for day in range(1, calendar.monthrange(year, month)[1] + 1):
            day_folder_name = f"./Diary_{year}/{calendar.month_name[month]}/{calendar.month_name[month]}_{day:02d}"

            with open(day_folder_name + "/work.tex", "w") as f1:
                f1.write(f"\fakesubsection{{{work_subsection_default}}}\n")
                if placeholder_text:
                    f1.write("\lipsum[1-2]\n")
            with open(day_folder_name + "/leisure.tex", "w") as f3:
                f3.write(f"\fakesubsection{{{leisure_subsection_default}}}\n")
                if placeholder_text:
                    f3.write("\lipsum[3-4]\n")


def create_custom_titlepage(dict_input):
    with open("./custom_titlepage_auto.tex", "w") as f6:
        f6.write(r"\begin{titlepage}" + "\n")
        f6.write(r"\centering" + "\n")
        f6.write(
            "\t" + r"\settowidth{\unitlength}{\LARGE THE BOOK OF CONUNDRUMS}" + "\n"
        )
        f6.write("\t" + r"\vspace*{\baselineskip}" + "\n")
        f6.write(
            "\t"
            + r"{\large\scshape "
            + f'{dict_input["author"]}'
            + r"}\\[\baselineskip]"
            + "\n"
        )
        f6.write(
            "\t"
            + r"\rule{\unitlength}{1.6pt}\vspace*{-\baselineskip}\vspace*{2pt}"
            + "\n"
        )
        f6.write("\t" + r"\rule{\unitlength}{0.4pt}\\[\baselineskip]" + "\n")
        f6.write(
            "\t"
            + r"{\LARGE "
            + f'{dict_input["document_title"]}'
            + r"}\\[\baselineskip]"
            + "\n"
        )
        f6.write(
            "\t"
            + r"{\itshape "
            + f'{dict_input["document_subtitle"]}'
            + r"}\\[0.2\baselineskip]"
            + "\n"
        )
        f6.write(
            "\t"
            + r"\rule{\unitlength}{0.4pt}\vspace*{-\baselineskip}\vspace{3.2pt}"
            + "\n"
        )
        f6.write("\t" + r"\rule{\unitlength}{1.6pt}\\[\baselineskip]" + "\n")
        f6.write("\t" + r"\par" + "\n")
        f6.write("\t" + r"\vfill" + "\n")
        f6.write(
            "\t"
            + r"{\large\scshape "
            + f'{dict_input["organization"]}'
            + r"}\\[\baselineskip]"
            + "\n"
        )
        f6.write(
            "\t" + r"{\small\scshape " + f'{dict_input["place"]}' + r"}\par" + "\n"
        )
        f6.write("\t" + r"\vspace*{0.1\textheight}" + "\n")
        f6.write(r"\end{titlepage}" + "\n")


########################## CODE EXECUTION ##########################

# Uncomment to delete existing diary folder and create a new one
# WARNING : deletes existing data failes for each day's journal entry
# create_fresh_diary_structure(year_input)

# Uncomment to create the fancy titlepage
create_custom_titlepage(titlepage_dict)

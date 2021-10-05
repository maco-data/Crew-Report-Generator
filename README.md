# Crew Report Generator v1.0
A small tool to automate the extraction of a crew duty report. The information is in many tables inside a pdf with several pages which make it tedious to work with.

### About the project

• I was a cabin crew for 10 years and accrued more than 9000 flying hours during this time! When I resigned, I received my crew duty report and although I was recording my flights on my own a MySQL database, the thought of making a project with this data had me so excited! So here is my attempt to extract the data, wrangle it and visualize it in several ways.

• I made a couple of visualizations from the data but I will later on use Tableau to create dashboard base on the data.

• My mind was overflowing with ideas to add to this project but I had to start focusing in other projects therefore I will keep those ideas pending. Some of the features I would like to add in a future would be:
  - Using Camelot for area selection instead of having to manually add the area measurements which by the way are (235, 35, 790, 590) in that order once you get the prompts.
  - A color picker for the visualizations.
  - Narrate the whole process, although it takes a few seconds for the whole program to run, this would make it feel more entertaining.
  - Build a GUI for those who are not adept using terminal or IDEs to run the program

### Goals Accomplished:

• Finding a tool to extract tables from pdf files.
  - Tabula saved my life on this one, especially as I manage to automate the process of copying and pasting every single table on the file.

• Use Pandas to wrangle and manage the data.
  - Interacted with the information extracted to create several records i.e.: Aircraft Flown Records, Ground Duty Records (Leave, Days Off, Sick days, etc.), Cleaned the remaining data to create a coherent Logbook.
    
• Using Matplotlib and Seaborn for Visualization.
  - My end goal was always to extract the tables and work with them in Tableau, but I am happy that I tried using this two packages. I was lazy by just using bar charts but I had in mind using histograms, scatter plot, horizontal bar chart and pie charts.

### Packages Used:

• At the Time of creating this project this are the packages versions used, their dependencies got installed automatically as I use miniconda on my setup:
  - Tabula      2.2.0
  - Pandas      1.3.3
  - Matplotlib  3.4.3
  - Seaborn     0.11.2

• I had Python 3.8 in my computer.

### DISCLAIMER: I UPALOADED THE FILE I GOT FROM MY PREVIOUS COMPANY, DELETED SENSITIVE DATA AND MODIFIED IT. IT IS OVBVIOUS WHICH COMPANY IT WAS BUT I BELIEVE AS THIS IS PAST DATA IT CANNOT BE USE FOR HARM IN ANY POSSIBLE WAY.!

![banana_airline](https://user-images.githubusercontent.com/85826647/136093439-53e4595d-1497-4b5c-befd-801a836bf1f9.png)

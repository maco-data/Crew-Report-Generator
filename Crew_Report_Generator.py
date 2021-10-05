import tabula
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def file_finder():
    """Welcomes the user and sets the name of the pdf file to be use"""
    welcome_msg = """\nHello!!! This program will help you get the information from your CREW DUTY REPORT.\n\nThere will be a few prompts which you need to input properly without mistakes\nso everything work out fine. Now let’s begging!\n"""
    print(welcome_msg)
    filename = input("\nPlease type in the file name: ")
    pdfpath = filename
    return pdfpath


def area_data():
    """This funciton collects the measurement of area to be use"""
    measurements = []
    max_m_list = 4
    while len(measurements) < max_m_list:
        top = input("\nWhat is the top measurement?: ")
        measurements.append(int(top))

        left = input("\nNow, what is the left measurement?: ")
        measurements.append(int(left))

        area_w = input("\nWhat is the area width?: ")
        measurements.append(int(area_w))

        area_l = input("\nAnd last, what is the area length?: ")
        measurements.append(int(area_l))

    return measurements


def area_info():
    """Provides information in how the area of the table is measure. (235, 35, 790, 590)"""
    area_msg = """\nNow let's measure the area of the tables. It's easy to do.\n\nThe area is measure in points so it is advice you use a program such as:\n\n\tAcrobat Reader\n\tAcrobat PDF\n\tAdobe Illustrator\n\tAdobe Photoshop\n\tor anything that can read "points"\n\nThe area has to be input as: (Top, Left, Area Width, Area Length):\n\n\tTop = A\n\tLeft = B\n\tArea Width = C (The table width)\n\tArea Length = D (The table lenght)\n\nAfter we get the measurements in "points" we’ll replace the letters from the values as:\n\n\t(A, B, A+D, B+C)\n"""

    print(area_msg)
    while input("Have you measure the area? y/n >> ") != "y":
        print("\nPlease measure the area.\n")


def addxlabels(x, y):
    """Adding labels in bar charts"""
    for bar in plots.patches:
        plots.annotate(
            bar.get_height(),
            (bar.get_x() + bar.get_width() / 2, bar.get_height()),
            ha="center",
            va="center",
            size=8,
            xytext=(0, 8),
            textcoords="offset points",
        )


def dash_remover(dataset, column1, column2, direction):
    """Selects the string on either side of the hyphen"""
    if direction == 0:  # select everything to the left of '-'
        before_symbol = dataset[column1].str.split("-").str[0]
        # convert the column data into strings
        before_symbol.str.split()
        dataset[column2] = before_symbol

    else:
        before_symbol = dataset[column1].str.split("-").str[1]
        # select everything to the left of '-'
        before_symbol.str.split()
        dataset[column2] = before_symbol

    return before_symbol


def backslash_remover(dataset, column1, column2, direction):
    """Selects the string on either side of the backlash"""
    if direction == 0:  # select everything to the left of '/'
        before_symbol = dataset[column1].str.split("/").str[0]
        # convert the column data into strings
        before_symbol.str.split()
        dataset[column2] = before_symbol

    else:
        before_symbol = dataset[column1].str.split("/").str[1]
        # select everything to the right of '-'
        before_symbol.str.split()
        dataset[column2] = before_symbol

    return before_symbol


def code_sepator(dataset, column1, column2, direction):
    """Select a string on either side as indicated and creates a new column"""
    if direction == 0:  # Selects first 3 letter
        iso_code = dataset[column1].str.slice(stop=3)
        # convert the column data into strings
        iso_code.str.split()
        dataset[column2] = iso_code
    else:
        iso_code = dataset[column1].str.slice(start=-3)  # Selects the last 3
        # convert the column data into strings
        iso_code.str.split()
        dataset[column2] = iso_code


def busy_msg():
    print("\nWorking on your flight data...")


def done_msg():
    print("\nDone! Your data has all been extracted and formated!\n")


# output the report into a csv file
file_path = file_finder()
area_info()
table_area = area_data()  # the area is (235, 35, 790, 590)
busy_msg()
tabula.convert_into(
    file_path,
    "logbook.csv",
    output_format="csv",
    area=table_area,
    guess=False,
    pages="all",
)

# convert the csv into a dataframe
logbook = pd.read_csv("logbook.csv", header=None)

# re-add the headers names
logbook.columns = ["flight_date", "duty", "grade", "dep_date", "arr_date", "block"]

# create a dataframe for the aircraft records and reset index
ac_records = logbook.iloc[-10:].copy()
ac_records.reset_index(drop=True, inplace=True)

# remove the three last column as they will not be needed on this record
ac_records.drop(columns=["dep_date", "arr_date", "block"], inplace=True)

# rename the columns for the record accordingly
ac_records.rename(
    columns={"flight_date": "Aircraft", "duty": "Type", "grade": "Hours"}, inplace=True
)

# Remove the thousand separator comma from the strings to be able to convert them into numbers
ac_comma_separator = [i.replace(",", "") for i in ac_records["Hours"].iloc[:-2]]
ac_records["Hours"].iloc[:-2] = ac_comma_separator
ac_records["Hours"].iloc[:-2] = pd.to_numeric(ac_records["Hours"].iloc[:-2])

# Fixing the Aircrafts Labels
ac_records["Aircraft"].loc[3:7] = [
    "A380-800",
    "777-200",
    "777-300",
    "777-200LR",
    "777-300ER",
]

# output the aircraft records to a csv file
ac_records.to_csv("ac_records.csv", na_rep="NA", index=False)

# open the aircraft records csv to be plot only loading 8 rows (total flight not needed)
ac_records_graph = pd.read_csv(
    "ac_records.csv",
    sep=",",
    usecols=["Aircraft", "Type", "Hours"],
    encoding="utf-8",
    nrows=8,
)

# plot the records in a bar graph
fig = plt.figure(figsize=(8, 4), tight_layout=True)

# values and color to be use
ac_model = ac_records_graph["Aircraft"]
ac_hours = ac_records_graph["Hours"]
record_color = sns.color_palette("deep")[6]
plots = sns.barplot(
    x=ac_model,
    y=ac_hours,
    data=ac_records_graph,
    color=record_color,
    label="From 2011 to 2020",
)

# set labels
plt.xlabel("Aircraft Type", size=15)
plt.ylabel("Hours Flown", size=15)
plt.yticks(range(500, 6500, 500))
plt.title("Aircraft Records", size=20)
plt.legend(loc="upper right")
addxlabels(ac_model, ac_hours)
plt.savefig("Aircraft_Records.png")

# drop last 20 rows
logbook.drop(index=logbook.index[-20:], axis=0, inplace=True)

# change columns 1, 3, 4 and 5  to the right format to the right format
# logbook[['flight_date', 'dep_date', 'arr_date']] = pd.to_datetime(logbook[['flight_date','dep_date', 'arr_date']], yearfirst = True);
logbook["flight_date"] = pd.to_datetime(logbook["flight_date"], yearfirst=True)
logbook["dep_date"] = pd.to_datetime(logbook["dep_date"], yearfirst=True)
logbook["arr_date"] = pd.to_datetime(logbook["arr_date"], yearfirst=True)

# FIX FIX FIX
logbook["block"] = pd.to_datetime(logbook["block"], format="%H:%M", errors="ignore")

# create the dataset for ground duties
gd_records = logbook.copy()

# drop the columns we do not need
gd_records.drop(columns=["grade", "dep_date", "arr_date", "block"], inplace=True)

# find rows in 'duty' which contain "-" and leave the flights out (lazy smart way)
gd_records = gd_records[gd_records["duty"].str.contains(r"-(?!$)")]

# separate the duty categories from the duty types
dash_remover(gd_records, "duty", "duty_cat", 0)
dash_remover(gd_records, "duty", "duty_type", 1)
gd_records.drop(columns=["duty"], inplace=True)
gd_records.rename(columns={"flight_date": "duty_date"}, inplace=True)

# output the ground duty records to a csv file
gd_records.to_csv(
    "gd_records.csv",
    na_rep="NA",
    header=["Duty Date", "Duty Category", "Duty Type"],
    index=False,
)

grouped_gd = gd_records.groupby(["duty_cat"], sort=False)["duty_type"].unique()

# second plot with ground duties
fig = plt.figure(figsize=(8, 4), tight_layout=True)

# plot settings
gdcat_names = []

for gdcat, gdtype in grouped_gd.items():
    gdcat_names.append(gdcat)

plots = sns.barplot(
    x=gdcat_names,
    y=gd_records["duty_cat"].value_counts(),
    data=gd_records,
    color=record_color,
    label="From 2011 to 2020",
)

# set labels and yticks
plt.xlabel("Categories", size=15)
plt.ylabel("Total", size=15)
plt.yticks(range(250, 1750, 250))

# setting the title for the graph
plt.title("Ground Duty Records", size=20)
plt.legend(loc="upper right")
addxlabels(gdcat_names, gd_records["duty_cat"].value_counts())
plt.savefig("Ground_Duties.png")

# creat new dataframe for the Flight Records
no_gd = logbook[logbook["grade"].notna()]
flight_logbook = no_gd.copy()

# creating 3 new columns from column "duty"
# first the flight numbers
backslash_remover(flight_logbook, "duty", "flight_num", 0)

# the rest of the string will be put in a temporary column
backslash_remover(flight_logbook, "duty", "temp_flight_dep", 1)

# second the flight departures
code_sepator(flight_logbook, "temp_flight_dep", "flight_dep", 0)

# third the flight arrivals
code_sepator(flight_logbook, "temp_flight_dep", "flight_arr", 1)

# drop unnecessary columns "duty", "temp_flight_dep"
flight_logbook.drop(columns=["duty", "temp_flight_dep"], inplace=True)

# change the flight time column to display as yyyy-mm-dd only
flight_logbook["flight_date"] = flight_logbook["flight_date"].dt.date

# changes the columns order
flight_logbook = flight_logbook.loc[
    :,
    [
        "flight_date",
        "flight_num",
        "flight_dep",
        "flight_arr",
        "grade",
        "dep_date",
        "arr_date",
        "block",
    ],
]

# output the Flight Records to a csv file
flight_logbook.to_csv(
    "flight_records.csv",
    na_rep="NA",
    header=[
        "Flight Date",
        "Flight Number",
        "Flight Departure",
        "Flight Arrival",
        "Grade",
        "Departure Date",
        "Arrival Date",
        "Flight Time",
    ],
    index=False,
)

done_msg()

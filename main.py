import pandas as pd
import logging

logging.basicConfig(
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO,
    force=True,
    # filename='out/app.log', # uncomment for mod log file
    # filemode='w'
)

df_titanic = pd.read_csv("./data/titanic.csv")


def print_section_title(title: str):
    logging.info("---------------------------------------------------------------")
    logging.info("---------------------------------------------------------------")
    logging.info(title.upper())
    logging.info("---------------------------------------------------------------")
    logging.info("---------------------------------------------------------------")


def print_dataframe_info(df: pd.DataFrame, title: str):
    print_section_title(title)

    rows = df.shape[0]
    columns = df.shape[1]
    num_values = rows * columns

    column_types = df_titanic.dtypes

    first_rows = df_titanic.head(10)
    last_rows = df_titanic.tail(10)

    logging.info(
        "Dataframe has %d rows, %d columns and has %d data.",
        rows,
        columns,
        num_values,
    )

    logging.info("Dataframe columns are: \n%s", column_types)

    logging.info("Dataframe first 10 rows: \n%s", first_rows)
    logging.info("dataframe last 10 rows: \n%s", last_rows)


def print_passanger_info(df: pd.DataFrame, passanger_id: int, title: str):
    print_section_title(title)

    passanger_info = df.loc[df_titanic["PassengerId"] == passanger_id]

    logging.info("Info of passanger with id 148: \n%s", passanger_info)


def print_even_rows(df: pd.DataFrame, title: str):
    print_section_title(title)

    even_rows = df.iloc[::2]

    logging.info("Even rows of dataframe: \n %s", even_rows)


def print_first_class(df: pd.DataFrame, title: str):
    print_section_title(title)

    first_class = df[df["Pclass"] == 1]
    sorted_first_class = first_class.sort_values(by="Name", ascending=True)
    names = sorted_first_class["Name"]

    logging.info("Sorted names of the passangers in first class: \n%s", names)


def print_survivors(df: pd.DataFrame, title: str):
    print_section_title(title)

    survivor = df[df['Survived'] == 1]
    percentage = survivor.shape[0] / df.shape[0]

    logging.info("%.2f%% survived.", percentage * 100)
    logging.info("%.2f%% didn't survived.", 100 - (percentage * 100))

def print_survivors_per_class(df: pd.DataFrame, title: str):
    print_section_title(title)

    survivors_per_class = pd.pivot_table(df, values='Survived', index='Pclass', aggfunc="mean")
    survivors_per_class["Survived"] = survivors_per_class['Survived'] * 100

    survivors_per_class.reset_index(inplace=True)

    format_mapping = '{Survived:.2f}% survived in class {Pclass:.0f}.'.format

    survivors_per_class.apply(lambda x: logging.info(format_mapping(**x)), 1)
    

def delete_unknown_age(df: pd.DataFrame, title: str):
    print_section_title(title)

    prev_size = df.shape[0]
    df = df.dropna(subset=['Age'])
    new_size = df.shape[0]

    logging.info("New dataframe has %d rows. %d were deleted.", new_size, prev_size - new_size)


def print_median_age(df: pd.DataFrame, title: str):
    print_section_title(title)

    female_passangers = df[df["Sex"] == "female"]

    average_age_per_class = pd.pivot_table(female_passangers, values='Age', index='Pclass', aggfunc='mean')

    average_age_per_class.reset_index(inplace=True)

    format_mapping = 'The mean woman age in class {Pclass:.0f} is: {Age:.1f}.'.format

    average_age_per_class.apply(lambda x: logging.info(format_mapping(**x)), 1)


def add_underage_column(df: pd.DataFrame, title: str):
    print_section_title(title)

    df["Underage"] = df["Age"] < 18

    logging.info("Added new column Underage: \n %s", df)


def print_age_survivors(df: pd.DataFrame, title: str):
    print_section_title(title)

    average_underage_per_class = pd.pivot_table(df, values='Survived', index=["Pclass", "Underage"], aggfunc='mean')
    average_underage_per_class["Survived"] = average_underage_per_class['Survived'] * 100
    
    average_underage_per_class.reset_index(inplace=True)

    average_underage_per_class["Underage"] = average_underage_per_class["Underage"].apply(lambda isUnderage: "underages" if isUnderage else "majors")

    format_mapping = '{Survived:.2f}% of {Underage} in class {Pclass} survived.'.format

    average_underage_per_class.apply(lambda x: logging.info(format_mapping(**x)), 1)
  


print_dataframe_info(df_titanic, "dataframe general info")
print_passanger_info(df_titanic, 148, "passanger 148 info")
print_even_rows(df_titanic, "even rows")
print_first_class(df_titanic, "sorted names of first class passangers")
print_survivors(df_titanic, "percentage of survivors")
print_survivors_per_class(df_titanic, "percentage of class survivors per class")
delete_unknown_age(df_titanic, "delete unknown age")
print_median_age(df_titanic, "average age of women per class")
add_underage_column(df_titanic, "add underage column")
print_age_survivors(df_titanic, "percentage underage survivor per class")
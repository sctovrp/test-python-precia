import pandas as pd
import logging

logging.basicConfig(
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO,
    force=True,
)

df_titanic = pd.read_csv('./data/titanic.csv')

logging.info('Dataframe has %d rows, %d columns and has %d data. \n ', df_titanic.shape[0], df_titanic.shape[1], df_titanic.shape[0] * df_titanic.shape[1])
logging.info('Dataframe columns are: \n %s', df_titanic.dtypes)
logging.info('Dataframe first 10 rows: \n %s', df_titanic.head(10))
logging.info('dataframe last 10 rows: \n %s', df_titanic.tail(10))

logging.info('Info of passanger with id=148: \n %s', df_titanic.loc[df_titanic['PassengerId']==148])

logging.info('Even rows of dataframe: \n %s', df_titanic.iloc[::2])
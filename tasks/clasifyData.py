import pandas as pd

def  groupClients(df):
    try:
        df["month"] = pd.to_datetime(df["shipping_date"]).dt.month
        df["year"] = pd.to_datetime(df["shipping_date"]).dt.year
        dfGrouped = df.groupby(["order_vendor_dbname", "month", "year"]).size().reset_index(name='count')
        usersFiltered = dfGrouped[dfGrouped['count']>=3]
        return df, usersFiltered
    except Exception as e:
        print("Error al procesar los datos: ",e)
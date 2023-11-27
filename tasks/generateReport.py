import os

def generateReport(originalDf,usersFiltered):

    # Crear un reporte en un archivo de texto
    report_file_name = os.path.join('.','sources', f'reporte.txt')
    os.makedirs(os.path.dirname(report_file_name), exist_ok=True)

    with open(report_file_name, 'w') as f:
        f.write("Reporte de Usuarios clasificados por mes y año:\n\n")
        
        yearsUnique =  usersFiltered['year'].unique()
        for year in yearsUnique:
            f.write(f"Año: {year}\n\n")
            monthFilter = usersFiltered[usersFiltered['year'] == year]
            monthUnique = monthFilter['month'].unique()
            for month in monthUnique:
                f.write(f"Mes: {month}\n\n")
                usersPerMonth = usersFiltered[usersFiltered['month'] == month]
                for user in usersPerMonth['order_vendor_dbname']:
                    f.write(f"Usuario: {user}\n")
                    f.write(f"Envios:\n")
                    tempDF = originalDf[originalDf['year'] == year]
                    tempDF = tempDF[tempDF['month'] == month]
                    tempDF = tempDF[tempDF['order_vendor_dbname'] == user]
                    f.write(f"- {tempDF['shipping_id']}\n")
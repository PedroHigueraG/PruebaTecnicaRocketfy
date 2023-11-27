from tasks import readDB, clasifyData, generateReport

try:
    queryDataFrame = readDB.readData()
    originalDf, usersFiltered = clasifyData.groupClients(queryDataFrame)
    generateReport.generateReport(originalDf,usersFiltered)
except Exception as e:
    print("Error al ejecutar el programa: ",e)
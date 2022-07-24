
import datetime
from pickle import FALSE, TRUE



class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self,name):
        self.name = name

    def get_data(self):

        data_temp = []
        data = []

        # Exception 1: File reading control
        try:
            my_file = open(self.name,'r')
            my_file.readline()
        except:
            raise ExamException("Impossibile aprire il file")
    
        my_file = open(self.name,"r")
    
        for line in my_file:
            element = line.split(",")

            element[-1] = element[-1].strip()
            #print(element)

            if element[0] != "date":
                #print("Elemento", element)
                data_temp.append(element)
        
        my_file.close()

        # Exception 2: Check empty file
        if len(data_temp) == 0:
            raise ExamException("File vuoto")

        for i in range(len(data_temp)):
            try:

                data_var = (data_temp[i][0])
                data_var = int(data_var.replace("-",""))

                passenger_var = int(data_temp[i][1])

                list_temp = (data_var,passenger_var)

                data.append(list_temp)
            except:
                print("Eccezione")
                pass

        for i in range(len(data)-1):
            if data[i][0] >= data[i+1][0]:
                raise ExamException("Dati non ordinati o duplicati")


        return(data)

years = (1949,1950)

def detect_similar_monthly_variations(time_series, years):

    year_1 = []
    year_2 = []

    i = 0
    j = 0
    trovato = FALSE

    while i < len(time_series) and trovato == FALSE:

        if int(float(time_series[i][0])/100) == years[0]:  

            j = i 

            while j < len(time_series) and int(float(time_series[j][0])/100) == years[0]:

                list_temp = (int(float(time_series[j][0])/100),time_series[j][0] % 100, time_series[j][1])
                year_1.append(list_temp)
                j += 1

            trovato = TRUE

        i += 1
        
    if(trovato == FALSE):
        raise ExamException("Anno", years[0],"non trovato nel dataset")
        
    
    i = 0
    j = 0
    trovato = FALSE

    while i < len(time_series) and trovato == FALSE:

        if int(float(time_series[i][0])/100) == years[1]:         
            
            j = i 

            while j < len(time_series) and int(float(time_series[j][0])/100) == years[1]:

                list_temp = (int(float(time_series[j][0])/100),time_series[j][0] % 100, time_series[j][1])
                year_2.append(list_temp)
                j += 1

            trovato = TRUE

        i += 1

    if(trovato == FALSE):
        raise ExamException("Anno", years[1],"non trovato nel dataset")
        

    for item in year_1:
        #print(item)
        None

    #print("*******************")

    for item in year_2:
        #print(item)
        None
    
    #print('Len year:',len(year_1))
    #print('Len year:',len(year_2))

    values = []

    for i in range(len(year_1)-1):

        j = 0
        res = "False"

        while j < len(year_2)-1:
            if year_1[i][1] == year_2[j][1] and year_1[i+1][1] == year_2[j+1][1]:

                tmp_1 = abs(year_1[i][2] - year_1[i+1][2])

                tmp_2 = abs(year_2[j][2] - year_2[j+1][2])

                if abs(tmp_1 - tmp_2) <= 2:
                    res = "True"

            j += 1

        #print("Res:", res)
        #print("")
        values.append(res)
    
    return(values)

    print("")

    #print("Lunghezza di Values:", len(values))

    print("")

    for item in values:
        #print(item)
        None

    #print(year_1[1][2])



    

    
    

time_series_file = CSVTimeSeriesFile("data_2.csv")
time_series = time_series_file.get_data()

risultato = detect_similar_monthly_variations(time_series,years)

for item in risultato:
    print(item)
    None


import pandas as pd
import datetime as dt

from pathlib import Path

import os
import time

######################################### WRANGLING ICD10 TABLE DATA #########################################
V3_data_folder = Path("C:/Users/Jesus/Desktop/Master/TFM/Datos/")

#V3_icd10_codes_dict_2018 = V3_data_folder / "icd10_codes_dict_2018.csv"
V3_icd10_codes_dict_2021 = V3_data_folder / "icd10cm_order_2021.txt"

### V3 COVID_DSL_06 - Data wrangling: removing lines exceeding fields number (7)
data = []

try: # open file in read mode
    #fp = open(V3_icd10_codes_dict_2018, "r", newline="\n", encoding = "latin-1")
   fp = open(V3_icd10_codes_dict_2021, "r", newline="\n", encoding = "latin-1")

   for line in fp:
        #data.append(line)

        order_number = line[0:5]
        blank1 = line[5]
        icd_10_cm_code = line[6:13]
        blank2 = line[13]
        header = line[14]
        blank3 = line[15]
        short_description = line[16:77]
        blank4 = line[77]
        long_description = line[77:]
        
        new_line = order_number + "|" + icd_10_cm_code.rstrip() + "|" + header + "|" + short_description.rstrip() + "|" + long_description.rstrip() + "\n"

        """     stripped_line = []
        new_line = ''

        stripped_line = line.split("\"")
        stripped_line[1] = stripped_line[1].replace(",",":")
        stripped_line[3] = stripped_line[3].replace(",",":")
        stripped_line[5] = stripped_line[5].replace(",",":")
        
        new_line = ''.join(stripped_line)
        #new_line = ''.join(stripped_line[i] for i in [0,1,2,3,4,5]) + "\n" #Only six first fields"""

        data.append(new_line) 
        #print(new_line)

except IOError as e:
   print("I/O error({0}): {1}".format(e.errno, e.strerror))
finally:
    fp.close()

try: # open file in writing mode
    f = open(V3_icd10_codes_dict_2021, "w", newline="\n", encoding = "latin-1")
    
    for line in data :
        f.write(line)

except IOError as e:
   print("I/O error({0}): {1}".format(e.errno, e.strerror))
finally:
    f.close()
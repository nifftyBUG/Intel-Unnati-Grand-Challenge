import pandas as pd
full_data = pd.read_csv('/content/sample_data/Intel unnati/unnati_phase1_data_revised.csv')
full_data.head()




full_data.info()



import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
data = pd.read_csv("/content/sample_data/Intel unnati/unnati_phase1_data_revised.csv")
missing_data = data.isnull()
msno.matrix(data)
plt.show()





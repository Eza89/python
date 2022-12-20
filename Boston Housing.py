mydf1 = pd.read_csv('/content/BostonHousing.csv')
# importing sweetviz
import sweetviz as sw

#analyzing the dataset
myreport = sw.analyze(mydf1)

#display the report
myreport.show_html('BostonH.html')
myreport.show_notebook()

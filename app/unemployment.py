

print("UNEMPLOYMENT REPORT...")


import os
import json
from dotenv import load_dotenv
import requests

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

# docs: https://www.alphavantage.co/documentation/#unemployment
url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(url)
parsed_response = json.loads(response.text)
#print(parsed_response)

data = parsed_response["data"]
latest = data[0]
print(latest) #> {'date': '2022-02-01', 'value': '3.8'}


##
## DATA AND CHARTING
##
#
#from pandas import DataFrame
#from plotly.express import bar
#
#
#df = DataFrame(data)
#print(df.head())
#
#fig = bar(df, x="date", y="value", title="Unemployment Rates")
##fig.show()
#
##breakpoint()
## https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html
#
## https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.to_image
## fig.to_image(format="png")
#
## https://plotly.com/python/static-image-export/
#img_filepath = os.path.join(os.path.dirname(__file__), "..", "figures", "unemployment.png")
#
## Image export using the "kaleido" engine requires the kaleido package,
##which can be installed using pip:
##    $ pip install -U kaleido
#fig.write_image(img_filepath)
#

#
# DATA (2)
#

from pandas import DataFrame

df = DataFrame(data)
print(df.head())

#breakpoint()
# type(df["value"][0]) #> str
df["unemployment_rate"] = df["value"].astype(float)


#
# CHARTING (2)
#

from plotly.express import bar

#fig = bar(df, x="date", y="value", title="Unemployment Rates")
fig = bar(df, x="date", y="unemployment_rate", title="Unemployment Rates")

# CHART (3)
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_yaxes
# https://plotly.com/python/reference/layout/yaxis/
# https://plotly.com/python/reference/layout/yaxis/#layout-yaxis-ticksuffix
fig.update_yaxes(
    #tickprefix="$",
    ticksuffix="%",
    showgrid=True
)
#fig.show()

print("DATAVIZ EXPORT...")
img_filepath = os.path.join(os.path.dirname(__file__), "..", "figures", "unemployment.png")
fig.write_image(img_filepath)




#
# EXPORTING (2)
#

print("CSV EXPORT...")
df.drop(columns=["value"], inplace=True) # remove column to clean before exporting
csv_filepath = os.path.join(os.path.dirname(__file__), "..", "reports", "unemployment.csv")
df.to_csv(csv_filepath, index=False)

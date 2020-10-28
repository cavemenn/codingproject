'''
Learning webscrapping
This file basically scrapes data from yahoo finance and uses pandas to make the data look better when outputed
learning selenium and phantomJS right now to improve my webscrapping skills (if theres any better libraries please recommend haha
Disclaimer: i didn't use beautifulsoup because i am abit slow in understanding it so i used split function to really see how my data are being divided
'''
import requests
import pandas as pd
wikiurl = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

wikiresponse = requests.get(wikiurl)

data = {'Company':[]}

wikiFirstParse = wikiresponse.text.split('0001555280')[0]
wikiDataTable = wikiFirstParse.split('S&amp;P 500 component stocks')[3]
hyperLinkSplitWiki = wikiDataTable.split('href=')
start=4
tracker=0
for position in range(len(hyperLinkSplitWiki)):
    if position > start:
        tracker = (position - (start+1))%4
        if 'nyse' in hyperLinkSplitWiki[position]:
            if 'quote' in hyperLinkSplitWiki[position]:
                tempData = hyperLinkSplitWiki[position].split('">')[1].split('</')[0]
                data['Company'].append(tempData)
        elif 'nasdaq' in hyperLinkSplitWiki[position]:
            if 'symbol' in hyperLinkSplitWiki[position]:
                tempData = hyperLinkSplitWiki[position].split('">')[1].split('</')[0]
                data['Company'].append(tempData)

print(len(data['Company']))
for number in range(0,501):
    data['Company'].pop()
print(len(data['Company']))
indicators = {"Previous Close": [],
              "Open": [],
              "Bid": [],
              "Ask": [],
              "Day&#x27;s Range": [],
              "52 Week Range": [],
              "Volume": [],
              "Avg. Volume": [],
              "Market Cap": [],
              "Beta (5Y Monthly)": [],
              "PE Ratio (TTM)": [],
              "EPS (TTM)": [],
              "Earnings Date": [],
              "Forward Dividend &amp; Yield": [],
              "Ex-Dividend Date": [],
              "1y Target Est": []
              }

counter = 0
for company in data['Company']:
    url = "https://finance.yahoo.com/quote/"+company+"?p="+company
    response = requests.get(url)
    htmlText = response.text

    for indicator in indicators:
        try:
            splitList = htmlText.split(indicator)
            afterFirstSplit = splitList[1].split('">')[2]
            afterSecondSplit = afterFirstSplit.split("</span></td>")
            if indicator == 'Day&#x27;s Range' or indicator == '52 Week Range' or indicator == 'Forward Dividend &amp; Yield'\
                    or indicator == 'Ask' or indicator == 'Bid':
                afterFirstSplit = splitList[1].split('">')[1]
                afterSecondSplit = afterFirstSplit.split("</td>")

            if indicator == 'Earnings Date':
                afterSecondSplit = afterFirstSplit.split("</")[0]
                dataValue = afterSecondSplit
                indicators[indicator].append((dataValue))
                continue

            dataValue = afterSecondSplit[0]
            indicators[indicator].append((dataValue))

        except:
            indicators[indicator].append('N/A')

data.update(indicators)

df = pd.DataFrame(data)

#print(data)
print(df.head)
'''print(indicators)
print(len(indicators['Ex-Dividend Date']))

'''

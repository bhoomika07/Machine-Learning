import csv
fname=input('Enter the name of csv file with extension: ')
with open(fname) as csv_file:
    csv_reader=csv.DictReader(csv_file)
    
    count=list()
    count1=list()
    date=list()
    stockReturns=dict()
    x=list()

    for row in csv_reader:
        count.append(row['Adj Close'])
        count1.append(row['Open'])
        date.append(row['Date'])
    zip_obj=zip(count,count1)
    for i,j in zip_obj:
        x.append((float(i)-float(j))/float(i)*100)
    for key in date:
        for value in x:
            stockReturns[key]=value
    #print(stockReturns)
    print(date)
    print(x)
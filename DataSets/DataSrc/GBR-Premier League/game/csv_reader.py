import csv



years = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015',
        '2015-2016', '2016-2017', '2017-2018']
for year in years:
   print(year)
   input_file = csv.reader(open('./premierleague-'+ year +'-game.csv' , 'r', encoding='utf-8'))
   
   with open('./process/premierleague-'+ year +'-game.csv' , 'w' , encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile,dialect='excel')
        for _index, data in enumerate(input_file):
            writer.writerow([data[0], data[1],data[2], data[3],data[4],data[5],data[6],
                            data[7], data[8], data[9],data[11], data[12], data[13], data[14] ,
                            data[15], data[16], data[17], data[18],data[19], data[20], data[21],data[22]])









# read specific column
# column = [row[2] for row in reader]
import urllib3
http = urllib3.PoolManager()

kats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

for kat in kats:
    for year in years:
        if year % 4 == 0:
            months_dict = {'01': '31', '02': '29', '03': '31', '04': '30',
                           '05': '31', '06': '30', '07': '31', '08': '31',
                           '09': '30', '10': '31', '11': '30', '12': '31'}
        else:
            months_dict = {'01': '31', '02': '28', '03': '31', '04': '30',
                           '05': '31', '06': '30', '07': '31', '08': '31',
                           '09': '30', '10': '31', '11': '30', '12': '31'}
        for month in months_dict:
            link = f'http://old.torgi.gov.ru/opendata/7710349494-torgi/data-{str(kat)}-{str(year)}{month}01T0000-{str(year)}{month}{months_dict[month]}T0000-structure-20130401T0000.xml'
            try:
                resp = http.request('GET', link)
                r = resp.data.decode('ascii')
                myfile = open(f'{str(kat)}_{str(year)}_{month}.xml', 'w')
                print(4)
                myfile.write(r)
            except:
                print('Eror1')

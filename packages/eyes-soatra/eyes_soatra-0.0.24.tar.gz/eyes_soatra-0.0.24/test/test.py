#!python3
from threading import Thread
from eyes_soatra import eyes
from eyes_soatra.constant.depends.app_date.start import depends as __starts
from eyes_soatra.constant.depends.app_date.end import depends as __ends
from eyes_soatra.constant.depends.app_date.period import depends as __periods
import pandas
import json
import argparse

read_from = 'test/data/active-1.csv'
records = pandas.read_csv(read_from).values

starts = []
ends = []
periods = []

def save_file(write_to):
    obj = {
        'starts': starts,
        'ends': ends,
        'periods': periods
    }
    for key in obj:
        each = obj[key]
        f = open(f'{write_to}{key}.json', "w")
        
        try:
            json_data = json.dumps(
                each,
                ensure_ascii=False,
                indent=4
            )
        except:
            json_data = None
            
        f.write(json_data if json_data else str(each))
        f.close()
        
        print(f'\n--- done ({key}) ---\n')
        print('length = ', len(each))
        print('\n-------------\n')

def worker(start, end):
    for i in range(start, end):
        url = records[i][2]
        
        try:
            print(f'{i+1} --- url: {url}')
            a = eyes.app_span(
                url=url,
                depends_start=list(map(lambda each: each['url'], starts)),
                depends_end=list(map(lambda each: each['url'], ends)),
                depends_period=list(map(lambda each: each['url'], periods)),
            )
            for key in a['detail']:
                if not key == 'highlight':
                    app = a['detail'][key]
                    point = app['point']
                    
                    if point >= 0.80:
                        keyword = app['keyword']
                        
                        if key == 'app-start':
                            if not (keyword in starts or keyword in __starts):
                                starts.append({
                                    'url': url,
                                    **app
                                })
                                print(f'\n+++ append starts. keyword:{keyword}\n')
                        
                        elif key == 'app-end':
                            if not (keyword in ends or keyword in __ends):
                                ends.append({
                                    'url': url,
                                    **app
                                })
                                print(f'\n+++ append ends. keyword:{keyword}\n')
                        
                        else:
                            if not (keyword in periods or keyword in __periods):
                                periods.append({
                                    'url': url,
                                    **app
                                })
                                print(f'\n+++ append periods. keyword:{keyword}\n')

        except:
            pass
        
def main(start_point, length, rows):
    length = (len(records) - start_point) if (start_point + length) > len(records) else length
    token = int(length / rows)
    write_to = f'test/checks/'
    threads = []
    
    for i in range(0, rows):
        start = start_point + (i * token)
        
        if i == rows - 1:
            end = length
            thread = Thread(
                target=worker,
                kwargs={'start': start, 'end': end}
            )
            threads.append(thread)
            
            for thread in threads:
                thread.start()
            
            for thread in threads:
                thread.join()
                
            save_file(write_to)

        else:
            end = start + token
            thread = Thread(
                target=worker,
                kwargs={'start': start, 'end': end}
            )
            threads.append(thread)
        
if __name__ == '__main__':
    defaults = {
        'start': 0,
        'length': 'all',
        'row': 250
    }
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start", help="start point", default=defaults['start'])
    parser.add_argument("-l", "--length", help="length", default=defaults['length'])
    parser.add_argument("-r", "--row", help="row", default=defaults['row'])
    args = parser.parse_args()
    
    start_point = int(args.start)
    length = len(records) if args.length == 'all' else int(args.length)
    rows = int(args.row)

    main(start_point, length, rows)

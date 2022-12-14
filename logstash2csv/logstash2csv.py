import os
import csv
import time
import datetime

# Get date and change the index name
def change_index():
    data = ''
    date = 'test-' + datetime.date.today().strftime('%Y.%m.%d')
    with open(r'D:\ELK\logstash-7.8.0\bin\convert_csv.conf', 'r+') as f:
        for line in f.readlines():
            if line.find('    index') == 0:
                line = '    index => "%s"' % date + '\n'
            data += line
    with open(r'D:\ELK\logstash-7.8.0\bin\convert_csv.conf', 'r+') as f:
        f.writelines(data)

def run():
    route = r"D:\ELK\logstash-7.8.0\bin"
    header = ["@timestamp", "CommandLine", "Image", "port", "ParentCommandLine", "EventID", "EventType",
              "ParentImage", "LocalIP", "columns"]
    csvfile = open(r'D:\ELK\logstash-7.8.0\export\csv-export.csv', 'w', errors='ignore', newline='')
    sheet = csv.writer(csvfile)
    sheet.writerow(header)
    csvfile.close()
    time.sleep(1)
    # Use shell to execute commands
    os.system('D: && cd %s && logstash -f convert_csv.conf' % route)
    time.sleep(2)
    print("OK")
    time.sleep(2)

if __name__ == '__main__':
    # Delete the ".lock" file generated each time logstash starts
    delete = r"D:\ELK\logstash-7.8.0\data"
    os.system('D: && cd %s && del .lock' % delete)
    
    change_index()
    run()

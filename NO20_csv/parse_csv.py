import csv
import json

if __name__ == '__main__':
    count = 0
    file_region_count = 0
    with open('obs_20201021_2.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        i = 0
        for row in reader:
            if i==0:
                i += 1
                continue
            if row:
            # if row and i==2:
                t = json.loads(row[0])
                # print(row)
                region_count = len(t.get('regions'))
                file_region_count += region_count
            i += 1
    print(file_region_count)



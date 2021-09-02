import datetime
import csv

def generate_csv(a_list):
    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        
        header = [i[0] for i in a_list[0]]
        writer.writerow(header)
        for i in a_list:            
            data = [j[1] for j in i]
            for k in range(len(data)):
                # print(k, ": ", type(k))
                if type(data[k]) == tuple or type(data[k]) == list:
                    data[k] = ",".join(data[k])
                elif type(data[k]) == datetime.date:
                    data[k] = data[k].strftime('%m/%d/%Y')
            writer.writerow(data)
        
def parse_csv():
    output = []
    with open('students.csv') as students:
        reader = csv.DictReader(students)        
        for i in reader:
            date_obj = datetime.datetime.strptime(i['Birthdate'], '%m/%d/%Y').date()     
            i['Birthdate'] = date_obj
            i['Marks'] = [int(j) for j in i['Marks'].split(",")]            
            output.append(i)    
    return output

meteo = [(('temperature', 42),
    ('date', datetime.date(2017, 1, 22)),
    ('locations', ('Berlin', 'Paris')),
    ('weather', 'sunny')),
    (('temperature', -42),
    ('date', datetime.date(2017, 1, 22)),
    ('locations', ('Marseille', 'Moscow')),
    ('weather', 'cloudy'))]

generate_csv(meteo)
print(parse_csv())
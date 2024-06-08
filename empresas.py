import csv
import json

empresas_dict = {
    "empresas":[]
}

with open('data.csv','r',newline='') as file_data:
    reader = csv.reader(file_data)
    for count, row in enumerate(reader):
        print(count, row)
        if count == 0:
            row.append("clasificacionEmpresa")
        else:
            venta = float(row[2])
            if venta < 100000000:
                row.append('Pequeña empresa')
            elif 100000000 < venta < 200000000:
                row.append('Mediana empresa')
            else:
                row.append('Gran empresa')
            empresas_dict['empresas'].append(
                {
                    "rut":row[0],
                    "nombre":row[1],
                    "ventas":row[2],
                    "clasificacion": row[3]
                }
            )
with open('empresas.json','w') as json_file:
    json.dump(empresas_dict, json_file)
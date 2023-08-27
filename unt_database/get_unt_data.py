import csv

from unt_database.utils import is_float, columns


def create_csv(file_name):
    try:
        texto = open(f'./database/{file_name}.txt', 'r', encoding="latin-1").read()
        lines = texto.strip().split('\n')
        with open(f'results/{file_name}.csv', 'w', newline='') as archivo_csv:
            descriptor_csv = csv.writer(archivo_csv)
            descriptor_csv.writerow(columns)
            result = []
            current_line = 0
            while current_line < len(lines) - 2:
                linea = lines[current_line]
                if header_detect(linea):
                    current_line += 8
                    linea = lines[current_line]
                result.append(write_rows(linea))
                current_line += 1
            flatten_result = []
            for item in result:
                if not item: continue
                flatten_result.append(item)
                descriptor_csv.writerow(item)
    except Exception as e:
        print(e)
        print('Error al leer el archivo')


def header_detect(linea):
    if "UNIVERSIDAD NACIONAL DE TRUJILLO - UNT" in linea:
        return True


def write_rows(linea):
    if linea == '': return []
    if '*' in linea: return []
    if 'Nro TOTAL DE POSTULANTES' in linea: return []
    campos = [campo.strip() for campo in linea.split()]
    index_used = []
    for i, campo in enumerate(campos[3:]):
        if not is_float(campo):
            index_used.append(i + 2)
            campos[2] = campos[2] + ' ' + campo
        else:
            index_used.append(i + 2)
            break
    index_used.pop(0)
    if campos[-2] == 'NO':
        campos[-2] = 'NO INGRESA'
        campos.pop(-1)
    if campos[-1] == '2-OPC':
        campos[-2] = 'ING. 2-OPC'
        campos.pop(-1)
    campos = [campo for i, campo in enumerate(campos) if i not in index_used]
    return campos

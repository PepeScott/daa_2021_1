import xlrd
from arrays import *
def main():
    a3=Array3D(34,33,14)
    for anio in range(2017,2019,1):
        ruta="./Precipitacion/"+str(anio)+"Precip.xls"
        archivo=xlrd.open_workbook(filename=ruta)
        hoja=archivo.sheet_by_index(0)
        for r in range(1,34,1):
            for c in range(0,14,1):
                a3.set_item(anio-2017,r-1,c,hoja.cell_value(r,c))
    a=int(input("Selecciones anio 2017 o 2018: "))
    e=int(input("Seleccione estado(1-32: )"))
    m=int(input("Selecciones mes(1-12): "))
    print("En el año",a,"mes de",a3.get_item(a-2017,0,m),"en el estado",a3.get_item(a-2017,e,0),"tuvo un promedio",a3.get_item(a-2017,e,m))
    suma=0.0
    for i in range(2017,2019,1):
        suma+=a3.get_item(i-2017,e,m)
    print("El promedio anual es de: ",suma/34)
    print("La suma es de: ", suma)

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
    for c in range(1,13,1):
        suma+=a3.get_item(a-2017,e,c)
    print("El promedio anual es de: ",suma/34)
    print("La suma es de: ", suma)
    datoMayor17=0
    estadoM17=0
    mesM17=0
    datoMenor17=0
    estadoMe17=0
    mesMe17=0
    datoMayor18=0
    estadoM18=0
    mesM18=0
    datoMenor18=0
    estadoMe18=0
    mesMe18=0
    for anio in range(2017,2019,1):
        for r in range(2,33,1):
            for c in range(1,13,1):
                dato=int(a3.get_item(anio-2017,r,c))
                if anio==2017:
                    if dato > datoMayor17:
                        datoMayor17=dato
                        estadoM17=r
                        mesM17=c
                    if dato < datoMayor17:
                        datoMenor17=dato
                        estadoMe17=r
                        mesMe17=c
                else:
                    if dato > datoMayor18:
                        datoMayor18=dato
                        estadoM18=r
                        mesM18=c
                    if dato < datoMayor18:
                        datoMenor18=dato
                        estadoMe18=r
                        mesMe18=c
    print("El mes que mas llovio fue",a3.get_item(0,0,mesM17),"en el estado numero",a3.get_item(0,estadoM17,0),"con un total de ", datoMayor17,"en el anio 2017")
    print("El mes que mas llovio fue",a3.get_item(1,0,mesM18),"en el estado numero",a3.get_item(1,estadoM18,0),"con un total de ", datoMayor18,"en el anio 2018")

    print("El mes que meno llovio fue",a3.get_item(0,0,mesMe17),"en el estado numero",a3.get_item(0,estadoMe17,0),"con un total de ", datoMenor17,"en el anio 2017")
    print("El mes que meno llovio fue",a3.get_item(1,0,mesMe18),"en el estado numero",a3.get_item(1,estadoMe18,0),"con un total de ", datoMenor18,"en el anio 2018")

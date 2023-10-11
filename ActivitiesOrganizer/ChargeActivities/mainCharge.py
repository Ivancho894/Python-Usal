from ActivitiesOrganizer.Prototypes.prototypes import Activity

def mainCharge():
    n = int(input('Ingrese cantidad de actividades a cargar: '))
    actVec=[None]*n
    for i in range(n):
        name=input('Ingrese el nombre de la actividad numero '+ str(i) +': ')
        hours=input('Ingrese la cantidad de horas: ')
        days=input('Ingrese la cantidad de dias: ')
        shift=input('Manana(m) o tarde(t): ')
        actVec[i]=Activity(name,hours,days,shift)


    print(actVec[0])

test()

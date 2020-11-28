
#Realiza una función que dependiendo de los parámetros que reciba: convierte a segundos o a horas:

    #Si recibe un argumento, supone que son segundos y convierte a horas, mintos y segundos.
    #Si recibe 3 argumentos, supone que son hora, minutos y segundos y los convierte a segundos.


def convertir_tiempo(args):

    if len(args) == 1:
        hh = segundos // 3600
        mm = (segundos%3600) // 60
        ss = segundos%60
        tiempo = "Los segundos serán en total " + str(hh) + ":" + str(mm) + ":" + str(ss) + "."
        return tiempo
    elif len(args) == 3:
        hh = int(tiempo.split(":")[0])
        mm = int(tiempo.split(":")[1])
        ss = int(tiempo.split(":")[2])
        S = "La cantidad de segundos será de " + str((hh * 3600) + (mm * 60) + ss) + " segundos."
        return S

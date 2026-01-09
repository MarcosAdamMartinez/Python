from datetime import date, time, datetime, timedelta

hoy = date.today()
print(hoy)

ahora = datetime.now()
print(ahora)

hora = time(7, 22, 15)
hora2 = time(7, 22)
print(hora)
print(hora2)

fecha = date(2020, 7, 22)
print(fecha)

momento = datetime(2020, 7, 22, 21, 24, 5)
print(momento)

formateado = momento.strftime("%A %m-%b %Y")
print(formateado)

texto = "2025-01-03 14:30"
formato ="%Y-%m-%d %H:%M"
objeto = datetime.strptime(texto, formato)
print(objeto)
print(objeto.year)
print(objeto.day)


fechafutura = objeto+timedelta(days=3520, hours=8, weeks=3)
print(fechafutura)
import click
import pandas as pd
from tabulate import tabulate
from data_management import read, write
@click.group()
def main():
     pass

@main.command()
@click.option("--name",type=str,required=True, help="Name of the week to search")
def see_week(name):
     #cargar datos guardados
     data = read()
     #validar si hay datos en memoria
     if not data[0]:
          return click.echo("No hay semanas guardadas, por favor cree una semana")
     
     if name not in data[0]:
          return click.echo("No existe la semana que buscas")
     #Leer datos 
     table = tabulate(data[0][name],headers="keys",tablefmt="fancy_grid")
     click.echo(table)

@main.command()
@click.option('--name',type=str,required = True, help = 'Indetify week')
def add_week(name):
     #Primero cargar los datos que ya estan guardados
     data = read()
     #procesar datos y añadir nueva semana
     processed_data = make_week(data,name)
     #guardar datos procesados
     write(processed_data)

@main.command()
@click.option("--week",type=str,required=True, help="Week todo")
@click.option("--day",type=str,required=True, help="Day todo")
@click.option("--task",type=str,required=True, help="Task to realize")
def edit_todo_day(week,day,task):
     #leer datos guardados
     data = read()
     #validar que  la semana exista
     if week not in data[0]:
          return click.echo("No existe la semana que buscas")
     
     data[0][week][day].append(task)

     #guardar en archivo json
     write(data)
     click.echo("Sucessfull, the day's now have the task")

@main.command()
@click.option("--week",type=str,required=True, help="Week to delete")
def remove_week(week):
     #Leer datos
     data = read()

     #validaciones
     if week not in data[0]:
          return click.echo("No existe la semana que deseas eliminar")
     
     #eliminar
     del data[0][week]
     click.echo("Week deleted Succesfull")
     write(data)



@main.command()
@click.option("--week",type=str,required=True, help="Old week name")
@click.option("--newname",type=str,required=True, help="New week name")
def edit_week_name(week,newname):
     data = read()

     if week not in data[0]:
          return click.echo("No existe la semana que deseas cambiar")
     
     data[0][newname] = data[0][week]

     del data[0][week]

     write(data)

@main.command()
@click.option("--week",type=str,required=True, help="Week name")
@click.option("--day",type=str,required=True, help="Day of the week")
@click.option("--task",type=int,required=True, help="Number of your task")
@click.option("--taskediting",type=str,required=True, help="The new description of your task")
def edit_task(week,day,task,taskediting):
     #leer datos
     data = read()

     #validar
     if week not in data[0]:
          return click.echo("No existe la semana que deseas cambiar")

     if not task-1 < len(data[0][week][day]) or not task > 0:
          return click.echo("La tarea que desea modificar no existe")
     
     #modificar
     data[0][week][day][task-1] = taskediting
     click.echo("task modified succesfull")
     write(data)

@main.command()
@click.option("--week",type=str,required=True, help="Week name")
@click.option("--day",type=str,required=True, help="Day of the week")
@click.option("--task",type=int,required=True, help="Number of your task")
def mark_completed(week,day,task):
     #leer datos
     data = read()

     #validar
     if week not in data[0]:
          return click.echo("No existe la semana que deseas cambiar")

     if not task-1 < len(data[0][week][day]) or not task > 0:
          return click.echo("La tarea que desea modificar no existe")
     
     del data[0][week][day][task-1]
     click.echo("Your task is completed, it will remove from the task table")
     write(data)
     
@main.command()
@click.option("--week",type=str,required=True, help="Week name")
def to_excel_one(week):
     data = read()

     if not data[0]:
          return click.echo("Data no exist")
     
     if week not in data[0]:
          return click.echo("No existe la semana que deseas cambiar")


     mydata = data[0][week]
     longitud_maxima = max(len(listas) for listas in mydata.values())

     for lista in mydata.values():
          while len(lista) < longitud_maxima:
               lista.append("")

     df = pd.DataFrame(mydata)
     df.to_excel("semanas.xlsx",index=False)
     click.echo("¡Excel created!")

     

def make_week(data,name):
     data = data
     data[0][name] = {
          "Lunes": [],
          "Martes": [],
          "Miercoles": [],
          "Jueves": [],
          "Viernes": [],
          "Sabado": [],
          "Domingo": [],
     }
     return data


if __name__ == "__main__":
     main()
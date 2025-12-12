#Proyecto EDA# %%
import pandas as pd
cliente1 = pd.read_excel('/Users/juliapirogova/Desktop/proyecto customer/datos clientes.xlsx', sheet_name="datos cliente")
cliente2 = pd.read_excel('/Users/juliapirogova/Desktop/proyecto customer/customer-details-1.xlsx', sheet_name="conjunto")


# %%
cliente1.head(5)

# %%
cliente2.head(5)

# %%
cliente1.info()

# %%
cliente1["age"] = pd.to_numeric(cliente1["age"], errors="coerce")

# %%
cliente2.info()

# %%
cliente1.describe().T

# %%
cliente2.describe().T

# %%
cliente1.duplicated().sum()

# %%
cliente2.duplicated().sum()

# %%
proyecto = cliente1.merge(cliente2, how = "left", on= "ID")
proyecto.sample(3)

# %%
proyecto.drop(labels = "Columna1", axis = 1, inplace = True)
proyecto.head(3)

# %%
proyecto.drop(labels = "latitude", axis = 1, inplace = True)
proyecto.drop(labels = "longitude", axis = 1, inplace = True)
proyecto.sample()



# %%
proyecto.head(3).T

# %%
project = proyecto.rename (columns = {
    "default" : "incumppagos",
    "housing" : "hipoteca",
    "loan" : "prestamo",
    "Income" : "renta",
    "duration" : "duracion",
    "campaign" : "ncontactos",
    "pdays" : "diasentrecontacto",
    "previous" : "ncontactosantes",
    "exito o no": "exito"

})
pd.set_option('display.max_columns', None)

# %%
project.sample(1)

# %%
project["dia_de_semana"] = project["date"].dt.day_name()
project.sample(1)

# %%
project["year"] = project ["date"].dt.year

# %%
project["mes"] = project ["date"].dt.month

# %%
project.describe().T

# %%
tabla_exito = project.groupby("exito")["ID"].count()
porcentaje_exito = tabla_exito/tabla_exito.sum() *100
resultado_exito = pd.DataFrame({
    "total": tabla_exito,
    "porcentaje_exito" : porcentaje_exito.round(2)
}

)
resultado_exito

# %%
tabla_num_contactos =project.groupby(["ncontactos", "exito"])["ID"].count().unstack(fill_value=0)
tabla_num_contactos

# %%
tabla_num_contactos["total"] = tabla_num_contactos["no"] + tabla_num_contactos["yes"]
tabla_num_contactos["porcentaje_exito"] = tabla_num_contactos["yes"] / tabla_num_contactos["total"] * 100
tabla_num_contactos


# %%
project.groupby(["marital", "exito"])["ID"].count().unstack(fill_value=0) #casi no hay diferencia entre estado civil 89%, 89%, 86%

# %%
project.groupby(["job", "exito"])["ID"].count().unstack(fill_value=0)

# %%
tabla_job = project.groupby(["job", "exito"])["ID"].count().unstack(fill_value=0)
porcentaje = tabla_job.div(tabla_job.sum(axis=1), axis =0) *100
porcentajes_job = porcentaje.round(2)
porcentajes_job

# %%
tabla_educacion = project.groupby(["education", "exito"])["ID"].count().unstack(fill_value=0)

# %%
tabla_educacion["total"] = tabla_educacion["no"] + tabla_educacion["yes"]
tabla_educacion["porcentaje_exito"] = tabla_educacion["yes"] / tabla_educacion["total"] * 100
tabla_educacion

# %%
tabla_educacion_cor = tabla_educacion.drop(labels = "illiterate", axis = 0)
tabla_educacion_cor

# %%
def age_group (x):
    if x < 32:
        return "Joven adulto"
    if 32<=x< 38:
        return "Joven mediano"
    if 38<=x < 47:
        return "Mediana edad"
    if x>=47:
        return "Adulto mayor"

    
project["grupo_edad"] = project["age"].apply(age_group)

# %%
edad_exito = project.groupby(["grupo_edad", "exito"])["ID"].count().unstack(fill_value=0) # 87%, 85%, 89%, 91%
edad_exito

# %%
edad_exito["total"] = edad_exito["no"] + edad_exito["yes"]
edad_exito["porcentaje_exito"] = edad_exito["yes"] / edad_exito["total"] * 100
edad_exito

# %%
def income_group (x):
    if x < 49000:
        return "renta baja"
    if 49000<= x < 93000:
        return "renta mediana"
    if 93000<= x < 136000:
        return "renta alta"
    if 136000 <= x:
        return "renta muy alta"
    

    
project["grupo_renta"] = project["renta"].apply(income_group)
    

# %%
renta_exito = project.groupby(["grupo_renta", "exito"])["ID"].count().unstack(fill_value=0)

# %%
renta_exito["total"] = renta_exito["no"] + renta_exito["yes"]
renta_exito["porcentaje_exito"] = renta_exito["yes"] / renta_exito["total"] * 100
renta_exito

# %%
project.groupby(["Kidhome", "exito"])["ID"].count().unstack(fill_value=0)

# %%
project.groupby(["Teenhome", "exito"])["ID"].count().unstack(fill_value=0)

# %%
project.groupby(["incumppagos", "exito"])["ID"].count().unstack(fill_value=0)

# %%
project.groupby(["hipoteca", "exito"])["ID"].count().unstack(fill_value=0)

# %%
project.groupby(["prestamo", "exito"])["ID"].count().unstack(fill_value=0)

# %%
project["diasentrecontacto"].describe()

# %%
dias_entre =project.groupby(["diasentrecontacto", "exito"])["ID"].count().unstack(fill_value=0)
dias_entre['total'] = dias_entre['yes'] + dias_entre['no']
dias_entre['porcentaje de éxito'] = dias_entre['yes'] *100 / dias_entre['total']
dias_entre

# %%
project["ncontactosantes"].describe()

# %%
contactos_previos = project.groupby(["ncontactosantes", "exito"])["ID"].count().unstack(fill_value=0)
contactos_previos["total"] = contactos_previos["no"] + contactos_previos["yes"]
contactos_previos["porcentaje_exito"] = contactos_previos["yes"] / contactos_previos["total"] *100
contactos_previos

# %%
def duracion_group (x):
    if x < 100:
        return "llamada corta"
    if 100<= x < 180:
        return "llamada mediana"
    if 180<= x < 320:
        return "llamada larga"
    if 320<= x:
        return "llamada muy larga"
    

    
project["grupo_duracion"] = project["duracion"].apply(duracion_group)

# %%
duracion_llamada= project.groupby(["grupo_duracion", "exito"])["ID"].count().unstack(fill_value=0) 
duracion_llamada["total"] = duracion_llamada["no"] + duracion_llamada["yes"]
duracion_llamada["porcentaje_exito"] = duracion_llamada["yes"] /duracion_llamada["total"] *100
duracion_llamada

# %%
project.groupby(["grupo_duracion", "grupo_edad"])["ID"].count().unstack(fill_value=0)

# %%
project.groupby(["grupo_duracion", "grupo_renta"])["ID"].count().unstack(fill_value=0)

# %%
project.groupby(["grupo_duracion", "job"])["ID"].count().unstack(fill_value=0)

# %%
project.groupby(["grupo_duracion", "marital"])["ID"].count().unstack(fill_value=0)

# %%
project.groupby("job").get_group("student").describe().T

# %%
project.groupby("job").get_group("retired").describe().T

# %%
tabla_dias = project.groupby(["dia_de_semana", "exito"])["ID"].count().unstack(fill_value=0)
tabla_dias

# %%
tabla_diasduracion = project.groupby(["dia_de_semana", "grupo_duracion"])["ID"].count().unstack(fill_value=0)
tabla_diasduracion

# %%
tabla_dia_semana = project.groupby(["dia_de_semana", "exito"])["ID"].count().unstack(fill_value=0)
porcentaje = tabla_dia_semana.div(tabla_dia_semana.sum(axis=1), axis =0) *100
porcentajes = porcentaje.round(2)
porcentajes

# %%
tabla_dias['total'] = tabla_dias['no'] + tabla_dias['yes']
tabla_dias['porcentaje_exito'] = tabla_dias['yes'] / tabla_dias['total'] *100

tabla_dias.sort_values('porcentaje_exito', ascending=False)


# %%
project.groupby(["year", "exito"])["ID"].count().unstack(fill_value=0)

# %%
project.groupby(["mes", "exito"])["ID"].count().unstack(fill_value=0)

# %%
tabla_mes = project.groupby(["mes", "exito"])["ID"].count().unstack(fill_value=0)
porcentaje = tabla_mes.div(tabla_mes.sum(axis=1), axis =0) *100
porcentajes_mes = porcentaje.round(2)
porcentajes_mes

# %%
visitas_web =project.groupby(["NumWebVisitsMonth", "exito"])["ID"].count().unstack(fill_value=0)
visitas_web

# %%
project.groupby("exito")[["emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]].mean()


# %%
numericas = project.select_dtypes(include='number')

numerical_profile = pd.DataFrame({
    'mean': numericas.mean(),
    'median': numericas.median(),
    'std': numericas.std(),
}).round(2)

numerical_profile


# %%
categoricas = project.select_dtypes(include='object')

categorical_profile = categoricas.mode().iloc[0]
categorical_profile


# %%
import seaborn as sns
import matplotlib.pyplot as plt

# %%


plt.figure(figsize=(6,6))
plt.pie( tabla_exito, labels = ["No", "Sí"], autopct='%1.1f%%', colors=['purple', 'yellow'])
plt.title("Distribución de Éxito de la Campaña")
plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficos")

plt.show()


# %%
plt.figure(figsize=(12,5))
plt.plot(tabla_num_contactos.index, tabla_num_contactos["porcentaje_exito"], marker="o")
plt.title("Porcentaje de éxito por número de contactos")
plt.xlabel("Número de contactos")
plt.ylabel("Porcentaje de éxito (%)")
plt.grid(True)
plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficos_ncontactos")

# %%

porcentajes_job[['no', 'yes']].plot(kind='bar', stacked=True, figsize=(10,6), color=['orchid','gold'])

plt.title('Porcentaje de éxito por tipo de trabajo')
plt.ylabel('Porcentaje (%)')
plt.xlabel('Job')
plt.legend(title='Éxito')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficos_job")


# %%

plt.figure(figsize=(10,6))
bars = plt.bar(tabla_educacion_cor.index, tabla_educacion_cor['porcentaje_exito'], color='plum')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f}%', ha='center', va='bottom')

plt.title('Porcentaje de éxito por nivel educativo')
plt.ylabel('Porcentaje de éxito (%)')
plt.xlabel('Nivel educativo')
plt.xticks(rotation=30, ha='right')
plt.ylim(0, tabla_educacion_cor['porcentaje_exito'].max() + 5)
plt.tight_layout()
plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficosniveleducativo.png")


# %%
plt.figure(figsize=(8,4))
sns.histplot(project['age'].dropna(), kde=True)
plt.title("Distribución de edad")
plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficos")


# %%

edad_exito[['no', 'yes']].plot (
    kind='bar', 
    stacked=True, 
    figsize=(10,6), 
    color=['cyan','pink'])


plt.title('Porcentaje de éxito por grupo de edad')
plt.ylabel('Cantidad')
plt.xlabel('Grupo edad')
plt.legend(title='Éxito')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()

plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficos_age.png")
plt.show()


# %%

ax = edad_exito[['no', 'yes']].plot(
    kind='bar',
    stacked=True,
    figsize=(10,6),
    color=['cyan','pink']
)

plt.title('Porcentaje de éxito por grupo de edad')
plt.ylabel('Cantidad')
plt.xlabel('Grupo edad')
plt.legend(title='Éxito')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()


totales = edad_exito[['no','yes']].sum(axis=1)

for i, (no_val, yes_val) in enumerate(zip(edad_exito['no'], edad_exito['yes'])):
    total = totales[i]
  
    p_no = no_val / total * 100
  
    p_yes = yes_val / total * 100
    
  
    ax.text(i, no_val / 2, f"{p_no:.1f}%", ha='center', va='center', fontsize=9)
    ax.text(i, no_val + yes_val / 2, f"{p_yes:.1f}%", ha='center', va='center', fontsize=9)

plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficos_age1.png")
plt.show()


# %%
plt.figure(figsize=(8,4))
sns.countplot(x='marital', data=project, hue='exito')
plt.title("Clientes por estado civil y éxito")
plt.xlabel("Estado civil")
plt.ylabel("Cantidad")
plt.legend(title='Éxito')
plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficos_estadocivil.png")
plt.show()


# %%

contactos_previos[['no', 'yes']].plot(kind='bar', stacked=True, figsize=(10,6), color=['indigo','fuchsia'])

plt.title("Éxito según número de contactos previos")
plt.xlabel("Número de contactos previos")
plt.ylabel("éxito")

plt.tight_layout()
plt.show()

# %%

data = {
    'dia_de_semana': ['Thursday','Tuesday','Saturday','Sunday','Wednesday','Monday','Friday'],
    'no': [5450,5346,5448,5457,5323,5378,5539],
    'yes': [748,686,699,692,656,657,673],
    'total': [6198,6032,6147,6149,5979,6035,6212],
    'tasa_exito': [0.120684,0.113727,0.113714,0.112539,0.109717,0.108865,0.108339]
}

df = pd.DataFrame(data).set_index("dia_de_semana")

plt.figure(figsize=(8,4))
sns.heatmap(df[["tasa_exito"]], annot=True, cmap="viridis", fmt=".3f")
plt.title("Heatmap — Tasa de éxito por día de la semana")
plt.ylabel("Día de la semana")
plt.xlabel("Tasa de éxito")
plt.tight_layout()
plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficos_exitopordiadesemana.png")
plt.show()


# %%

data = {
    "renta alta":[2513,2692,2704,2675],
    "renta baja":[2533,2613,2771,2675],
    "renta mediana":[2616,2732,2873,2671],
    "renta muy alta":[2665,2735,2846,2686]
}

index = ["llamada corta","llamada larga","llamada mediana","llamada muy larga"]

df = pd.DataFrame(data, index=index)

plt.figure(figsize=(8,5))
sns.heatmap(df, annot=True, fmt="d", cmap="PuOr")
plt.title("Heatmap — Duración de llamada vs Grupo de renta")
plt.ylabel("Grupo de duración")
plt.xlabel("Rango de renta")
plt.tight_layout()
plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficos_duracionrenta")
plt.show()


# %%

data = {
    "no":[10246,9641,10692,7577],
    "yes":[81,1131,502,3130]
}

index = ["llamada corta","llamada larga","llamada mediana","llamada muy larga"]

df = pd.DataFrame(data, index=index)

plt.figure(figsize=(7,4))
sns.heatmap(df, annot=True, fmt="d", cmap="seismic")
plt.title("Heatmap — Éxito vs No éxito por duración de llamada")
plt.xlabel("Resultado")
plt.ylabel("Duración de llamada")
plt.tight_layout()

plt.show()


# %%
data = {
    "Adulto mayor":[2390,2407,2591,2498],
    "Joven adulto":[1951,2226,2309,2195],
    "Joven mediano":[2386,2367,2460,2363],
    "Mediana edad":[2335,2437,2545,2420]
}

index = ["llamada corta","llamada larga","llamada mediana","llamada muy larga"]

df = pd.DataFrame(data, index=index)

# Heatmap
plt.figure(figsize=(8,5))
sns.heatmap(df, annot=True, cmap="winter", fmt="d")
plt.title("Heatmap — Duración de llamada vs Grupo de edad")
plt.ylabel("Duración de llamada")
plt.xlabel("Grupo de edad")
plt.tight_layout()
plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficos_duracionedad")
plt.show()

# %%

plt.figure(figsize=(6,4))
sns.heatmap(edad_exito, annot=True, fmt=".0f", cmap="rocket_r")

plt.title("Éxito por grupo de edad")
plt.show()



# %%
solo_exito = dias_entre['yes']

solo_exito.plot(
    kind='bar',
    figsize=(10,6),
    legend=False,
    color= "indigo"
)

plt.title("Distribución de días entre contactos")
plt.xlabel("Días")
plt.ylabel("Cantidad")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficos_exitodiasentrecontacto.png")
plt.show()

# %%

ex_duracion = duracion_llamada['porcentaje_exito'] 

ex_duracion.plot(
    kind='bar',
    figsize=(10,6),
    color='crimson'
)

plt.title("Porcentaje de éxito según duración de la llamada")
plt.ylabel("Porcentaje de éxito (%)")
plt.xlabel("Grupo de duración")
plt.xticks(rotation=30, ha='right')


plt.tight_layout()
plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficos_exitoduracion.png")
plt.show()


# %%

porcentajes_mes[['no', 'yes']].plot(
    kind='bar',
    stacked=True,
    figsize=(10,6),
    color=['lightcoral', 'lightgreen']
)

plt.title("Porcentaje de éxito por mes")
plt.xlabel("Mes")
plt.ylabel("Porcentaje (%)")
plt.xticks(rotation=45, ha='right')
plt.legend(title="Resultado")
plt.tight_layout()
plt.show()


# %%


plt.figure(figsize=(10,6))
plt.plot(
    porcentajes_mes.index,
    porcentajes_mes['yes'],
    marker='o',
    linewidth=2,
    color='purple'
)

plt.title('Porcentaje de éxito por mes')
plt.xlabel('Mes')
plt.ylabel('Porcentaje de éxito (%)')
plt.grid(True)
plt.xticks(porcentajes_mes.index)
plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficos_exitopormes.png")
plt.tight_layout()
plt.show()


# %%

plt.figure(figsize=(8,5))
plt.barh(tabla_dias.index, tabla_dias["porcentaje_exito"], color = "salmon")
plt.xlabel("Porcentaje de éxito (%)")
plt.title("Porcentaje de éxito por día de la semana")
plt.tight_layout()
plt.savefig("/Users/juliapirogova/Desktop/proyecto customer/graficos_diadesemana.png")
plt.show()

# %%
visitas_web = visitas_web.reset_index()
visitas_web["success_rate"] = visitas_web["yes"] / (visitas_web["yes"] + visitas_web["no"]) *100

plt.figure(figsize=(12,5))
plt.bar(visitas_web["NumWebVisitsMonth"], visitas_web["success_rate"])
plt.xlabel("Número de visitas web")
plt.ylabel("Porcentaje de éxito")
plt.title("Porcentaje de éxito por número de visitas web")
plt.xticks(visitas_web["NumWebVisitsMonth"], rotation=90)
plt.grid(axis='y')

plt.show()



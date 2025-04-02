import pandas as pd

'''datos = {'Producto': ['Producto A','Producto B', 'Producto C'],
         'Precio': [100, -50, None]}

df = pd.DataFrame(datos)

df['Validacion Precio'] = df['Precio'].apply(lambda x: 'Valido' if pd.notnull(x) and x>=0 else 'Invalido')

print(df)'''

'''clientes = {'ID cliente': [1,2,2,3,3], 'Nombre': ['ana','luis', 'luis', 'maria', 'maria']}

df_clientes=pd.DataFrame(clientes)
duplicados=df_clientes[df_clientes.duplicated('ID cliente')]

print(duplicados)'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher_suite = Fernet(key)

datos_sensibles = "ricardo".encode()

datos_encriptados = cipher_suite.encrypt(datos_sensibles)
datos_desencriptados = cipher_suite.decrypt(datos_encriptados)

print(datos_encriptados)
print(datos_desencriptados)'''


df = pd.DataFrame({
    'Producto': ['A', 'B','C'],
    'Precio': [100,200,300]
})

df.to_csv('Backups ventas.csv', index=False)

print("backup guardado como 'backup_ventas.csv'")




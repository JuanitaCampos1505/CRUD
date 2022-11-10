!pip install pyrebase
!pip install firebase
from firebase import  firebase
firebase = firebase.FirebaseApplication("https://api-c8c52-default-rtdb.firebaseio.com/", None)
datos={
   'id': '11',
   'Nombre': 'Marta',
   'Apellido': 'Lopez',
   'Direccion': 'apartamento 705',
   'Telefono': '3134798627'

}
#Para llenar la base de datos método POST

resultado=firebase.post('/API_distribuidos/datos_post',datos)
print(resultado)

#Para mostrar la base de datos método GET

leer=firebase.get('/API_distribuidos/datos_post','')
print(leer)

#Para editar registros método PUT
firebase.put('/API_distribuidos/datos_post/-NGI5dZe5QyTLPbSwCaU','Nombre','Lucia')

#Para eliminar registros método DELETE
firebase.delete('/API_distribuidos/datos_post','-NGI5dZe5QyTLPbSwCaU')
print('se eliminó')

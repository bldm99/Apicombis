from django.db import models

class Distritos(models.Model):
    nombre = models.CharField(max_length=100 , unique=True)
    def __str__(self):
        return self.nombre
    
    
    
class Paraderos(models.Model):
    ubicacion = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to = "paraderos" , null =True)  
    
    def __str__(self):
        return self.ubicacion  
    
    
class Jornadas(models.Model):
    inicio = models.CharField(max_length=200)
    final= models.CharField(max_length=200)
   
    
    def __str__(self):
        return self.inicio     
    
    
   
   
    

class Rutas(models.Model):
    nombre = models.CharField(max_length=200)
    inicio = models.CharField(max_length=200)
    final = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    paraderos_id = models.ForeignKey(Paraderos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password= models.CharField(max_length=200)
    distritos_id = models.ForeignKey(Distritos , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre    

class Empresas(models.Model):
    nombre = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    distrito_id = models.ForeignKey(Distritos , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = "empresas" , null =True)  
    rutas_id = models.ForeignKey(Rutas , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre  
    
    
class Unidades(models.Model):
    conductor = models.CharField(max_length=200)
    placa= models.CharField(max_length=200)
    longitud= models.CharField(max_length=200)
    capacidad = models.IntegerField()
    lapso_tiempo=models.CharField(max_length=200)
    empresas_id = models.ForeignKey(Empresas , on_delete=models.CASCADE)
    distrito_id = models.ForeignKey(Distritos , on_delete=models.CASCADE)
    rutas_id = models.ForeignKey(Rutas , on_delete=models.CASCADE)
    jornadas_id = models.ForeignKey(Jornadas , on_delete=models.CASCADE)
    
   
    def __str__(self):
        return self.placa     
    
    
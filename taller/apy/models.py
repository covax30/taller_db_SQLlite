from django.db import models

# MODULOS STEVEN

class Cliente(models.Model):
    id_cliente = models.IntegerField(unique=True)  
    id_operacion = models.IntegerField(default=0)
    nombre = models.CharField(max_length=100)
    documento = models.BigIntegerField(default=0)
    telefono = models.BigIntegerField(default=0)
    correo = models.EmailField(max_length=100)
    fecha_operacion = models.DateField()
    monto = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id_cliente} - {self.nombre}"


class Vehiculo(models.Model):
    id_vehiculo = models.IntegerField(unique=True) 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # LLAVE
    placa = models.CharField(max_length=10, unique=True)
    modelo_vehiculo = models.CharField(max_length=100)
    marca_vehiculo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.placa} - {self.marca_vehiculo} - {self.modelo_vehiculo}"


class EntradaVehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # LLAVE
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)  # LLAVE
    fecha_ingreso = models.DateField()
    hora_ingreso = models.TimeField()

    def __str__(self):
        return f"{self.cliente.id_cliente} - {self.vehiculo.placa} - {self.fecha_ingreso} {self.hora_ingreso}"


class SalidaVehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # LLAVE
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)  # LLAVE
    diagnostico = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    hora_ingreso = models.TimeField()

    def __str__(self):
        return f"{self.cliente.id_cliente} - {self.vehiculo.placa} - {self.diagnostico}"


class Compra(models.Model):
    id_factura_compra = models.IntegerField(unique=True)
    id_compra = models.IntegerField(default=0)
    proveedor = models.CharField(max_length=100)
    fecha_compra = models.DateField()
    hora_compra = models.TimeField()

    def __str__(self):
        return f"{self.id_factura_compra} - {self.proveedor} - {self.fecha_compra} {self.hora_compra}"

#------ MODULOS ERICK ---------
#------ ENTIDAD de TIPO mantenmimiento ---------1
class TipoMantenimiento(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
        
#------- Marca-------- 
class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.tipo}"

#------ ENTIDAD REPUESTOS --------3
class Repuesto(models.Model):
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    ubicacion = models.CharField(max_length=100)
    precio = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.nombre} ({self.codigo})"  
    
#------ ENTIDAD HERRAMIENTAS --------4
class Herramienta(models.Model):

    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

#------ ENTIDAD INSUMOS --------5
class Insumos(models.Model):

    id_marca = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    costo = models.IntegerField()
    tipo = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)

    def __str__(self):

        return f"{self.nombre} ({self.id})"
    
#-------------MODULOS DE karol-----------
#-------------Modulo Administrador-----------
class Administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20, unique=True)
    edad = models.IntegerField()
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
#------- Gastos--------
class Gastos(models.Model):
    id_gasto =  models.AutoField(primary_key = True)  #ID automatico
    monto= models,models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField() 
    tipo_gastos=models.CharField(max_length=100)
             


#--------------Modulo Pago Servicio Publicos-----------
class PagoServiciosPublicos(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    monto = models,models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.id_servicio} {self.monto}"
    
#--------------Modulo Proveedores--------------
class Proveedores(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.id_proveedor} {self.correo}"
    
#--------------Modulo Pagos-----------------
class Pagos(models.Model):
    id_pago = models.AutoField(primary_key=True)
    tipo_pago = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    monto = models,models.DecimalField(max_digits=10, decimal_places=2)
    id_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    id_admin = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    id_herramienta = models.ForeignKey(Herramienta, on_delete=models.CASCADE)
    id_insumos = models.ForeignKey(Insumos, on_delete=models.CASCADE)
    id_repuestos = models.ForeignKey(Repuesto, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id_pago} {self.monto}"
    
#------- Gastos-------- ya esta subido
class Gastos(models.Model):
   
    monto= models,models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField() 
    tipo_gastos=models.CharField(max_length=100,  unique=True)
    id_pagos_servicios = models.ForeignKey(PagoServiciosPublicos, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.tipo_gastos} - ${self.monto}"
     #class meta
        #verbose_name = 'Gastos'
        #verbose_name_plural = 'Gastos'
          

#-------- Empleado-------
class Empleado(models.Model): 
   
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    identificacion = models.CharField(max_length=20, unique=True) 
    Correo= models.EmailField(max_length=254, unique=True)
    direccion = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.nombre} ({self.identificacion})"
    #class meta
        #verbose_name = 'Empleado'
        #verbose_name_plural = 'Empleado'
    
#------ ENTIDAD GESTION DE MANTENIMIENTO --------2
class Mantenimiento(models.Model):
    fallas = models.TextField()
    procesos = models.CharField(max_length=50)
    id_vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    id_tipo_mantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fallas} - {self.id_tipo_mantenimiento}"
#------------Modulo Informes-----------
class Informes(models.Model):
    id_informe = models.AutoField(primary_key=True)
    repuestos_usados = models.TextField()
    costo_mano_obra = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    hora = models.TimeField()
    id_repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo_informe = models.CharField(max_length=100)
    id_mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id_informe} {self.tipo_informe}"
#-------- nomina------
class Nomina(models.Model):
   
    rol = models.CharField(max_length=100,  unique=True) 
    monto= models.DecimalField(max_digits=10, decimal_places=2) 
    fecha_pago =  models.DateField() 
    id_empleado =   models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)            
    def __str__(self):
        return f"{self.rol} - ${self.monto} - {self.fecha_pago}"
     #class meta
        #verbose_name = 'Nomina'
        #verbose_name_plural = 'Nomina'
    
#-----------Factura-----------------
class Factura(models.Model):
    
    tipo_pago = models.CharField(max_length=45, null=True, blank=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    id_vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL, null=True, blank=True)
    id_tipo_mantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.SET_NULL, null=True, blank=True)
    servicio_prestado = models.CharField(max_length=45, null=True, blank=True)
    nombre_empresa = models.CharField(max_length=45, null=True, blank=True)
    direccion_empresa = models.CharField(max_length=45, null=True, blank=True)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Factura {self.id} - {self.tipo_pago or 'Sin pago'}"

#-----------Caja-----------------
class Caja(models.Model):
   
    tipo_movimiento= models.CharField(max_length=50)
    monto= models.DecimalField(max_digits=10, decimal_places=2)
    fecha= models.DateField()
    hora=models.TimeField()
    id_gasto= models.ForeignKey( Gastos , on_delete=models.CASCADE, null=True, blank=True )
    id_admin=models.ForeignKey(Administrador, on_delete=models.CASCADE, null=True, blank=True) 
    id_Factura= models.ForeignKey(Factura, on_delete=models.CASCADE, null=True, blank=True)
    id_pagos= models.ForeignKey(Pagos, on_delete=models.CASCADE, null=True, blank=True)
    id_nomina= models.ForeignKey(Nomina, on_delete=models.CASCADE, null=True, blank=True) 
    def __str__(self):
        return f"{self.tipo_movimiento} - {self.monto} en {self.fecha} {self.hora}"   
    #class meta
        #verbose_name = 'Caja'
        #verbose_name_plural = 'Caja'


#from django.urls import path
from rest_framework import routers


from .api import DistritosViewSet , ParaderosViewSet ,JornadasViewSet,RutasViewSet, UsuariosViewSet,EmpresasViewSet , UnidadesViewSet


router = routers.DefaultRouter()

router.register('api/distritos' ,DistritosViewSet , 'distritos' )
router.register('api/paraderos' ,ParaderosViewSet , 'paraderos' )
router.register('api/jornadas' ,JornadasViewSet , 'jornadas' )
router.register('api/rutas' ,RutasViewSet , 'rutas' )
router.register('api/usuarios' ,UsuariosViewSet , 'usuarios' )
router.register('api/empresas' ,EmpresasViewSet , 'empresas' )
router.register('api/unidades' ,UnidadesViewSet , 'unidades' )



urlpatterns =  router.urls





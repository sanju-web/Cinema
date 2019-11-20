from rest_framework.routers import SimpleRouter
from .views import MovieOperation,ActorOperation

simpleRouter = SimpleRouter()

simpleRouter.register('Movie',MovieOperation)
simpleRouter.register('Actor',ActorOperation)


urlpatterns = simpleRouter.urls
import graphene
from graphene_django import DjangoObjectType
from .models import *
import datetime
from graphene_django_subscriptions.subscription import Subscription
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User 

class ActivityType(DjangoObjectType):
    class Meta:
        model = Activity

class ReportType(DjangoObjectType):
    class Meta:
        model = Report

class Query(graphene.ObjectType):
    actividad = graphene.List(ActivityType)
    reporte = graphene.List(ReportType)

    def resolve_actividad(self, info, **kwargs):
        return Activity.objects.all()

    def resolve_reporte(self, info, **kwargs):
        return Report.objects.all()


#============= Mutaciones ======================
class Login(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
    
    user = graphene.Field(UserType)

    def mutate(self, info, **kwargs):
        try:
            user = User.objects.get(username=kwargs.get('username'))
            if user.check_password(kwargs.get('password')):
                return Login(user=user)
        except Exception as e:
            print(e)

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, **kwargs):
        try:
            user=User(
                username = kwargs.get('username'),
                first_name = kwargs.get('first_name'),
                last_name = kwargs.get('last_name'))
            user.set_password(kwargs.get('password'))
            user.save()
            return CreateUser(user = user)
        except Exception as e:
            print(e)
    

class UpdateActivity(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        estado = graphene.String()
        reporte = graphene.String(default_value='None')
        usuario = graphene.String()

    actividad = graphene.Field(ActivityType)

    def mutate(self, info, **kwargs):
        user = kwargs.get('usuario')
        try:
            id = kwargs.get('id')
            estado = kwargs.get('estado')
            reporte = kwargs.get('reporte') 

            activity = Activity.objects.get(id=id)
            activity.estado = estado

            if user == activity.responsable.username:
                activity.save()

                if reporte != 'None':
                    Report(
                        actividad = activity,
                        descripcion = reporte,
                        fecha_reporte = datetime.datetime.now()
                    ).save()

                return UpdateActivity(actividad = activity)
        except Exception as e:
            print(e)


class Mutation(graphene.ObjectType):
    actualizar_actividad = UpdateActivity.Field()
    nuevo_usuario = CreateUser.Field()
    inicio = Login.Field()

#============== Suscripciones ====================





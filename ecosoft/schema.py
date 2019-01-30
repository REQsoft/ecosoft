import graphene
import manager.schema


class Query(manager.schema.Query, 
            graphene.ObjectType):
    '''This class will inherit from multiple Queries
    as we begin to add more apps to our project'''

    pass

class Mutations(manager.schema.Mutation,
        graphene.ObjectType):
    '''This class will generate a new token to 
    authenticate and clasificate all the users that 
    send a request to our API'''
    pass


schema = graphene.Schema(query=Query, mutation=Mutations)
from ConnectionsHandler.udaconnect.models import Connection, Location, Person  # noqa
from ConnectionsHandler.udaconnect.schemas import ConnectionSchema, LocationSchema, PersonSchema  # noqa


def register_routes(api, app, root="api"):
    from ConnectionsHandler.udaconnect.controllers import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")

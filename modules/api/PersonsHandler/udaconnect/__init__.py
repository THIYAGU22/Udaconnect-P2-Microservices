from PersonsHandler.udaconnect.models import Person  # noqa
from PersonsHandler.udaconnect.schemas import PersonSchema  # noqa


def register_routes(api, app, root="api"):
    from PersonsHandler.udaconnect.controllers import api as udaconnect_persons_api

    api.add_namespace(udaconnect_persons_api, path=f"/{root}")

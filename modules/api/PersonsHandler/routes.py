def register_routes(api, app, root="api"):
    from PersonsHandler.udaconnect import register_routes as attach_person_udaconnect

    # Add routes
    attach_person_udaconnect(api, app)

def register_routes(blueprint):
    @blueprint.route('/helloworld', methods=['GET'])
    def get_title():
        result = {
            "Hello": "World",
        }

        return result

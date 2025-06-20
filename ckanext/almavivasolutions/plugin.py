import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.almavivasolutions.controllers import bp
from typing import Dict, Callable, Any

# import ckanext.almavivasolutions.cli as cli
# import ckanext.almavivasolutions.helpers as helpers
# import ckanext.almavivasolutions.views as views
# from ckanext.almavivasolutions.logic import (
#     action, auth, validators
# )

class AlmavivasolutionsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    # plugins.implements(plugins.IBeforeMap)
    
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    # plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    
    # def before_map(self, map):
    #     map.connect('sobre', '/sobre', controller='ckanext.almavivasolutions.controllers:SobreController', action='sobre')
    #     return map
    

    # IConfigurer



    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "almavivasolutions")

    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    def get_blueprint(self):
        return bp

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    # def get_helpers(self) -> Dict[str, Callable[..., Any]]:
    #     return {
    #         'exibir_grupos': exibir_grupos,
    #     }


    # def exibir_grupos():
    #     groups = toolkit.get_action('group_list')(
    #         {}, {'all_fields': True}
    #     )
    #     return groups[:10]
    # IValidators

    # def get_validators(self):
    #     return validators.get_validators()
from smartdc import DataCenter, TELEFONICA_LOCATIONS
from locust import web

mad = DataCenter(location='eu-mad-1',
              known_locations=TELEFONICA_LOCATIONS,
              login='', password='', api_version='6.5')

@web.app.route("/cloud/create")
def cloud_create():

	template_found = False
	for machine in mad.machines():
		tags = machine.get_tags()

        if tags.get('locust') == 'slave-template':
                new_machine = machine.clone()
                new_machine.add_tags(locust='slave')
                return new_machine

	return None

from pokie.core import BaseModule

from pokie_location.constants import SVC_LOCATION


class Module(BaseModule):
    name = "location"
    description = "Location Services"

    cmd = {}

    services = {
        SVC_LOCATION: "pokie_location.service.LocationService",
    }

    jobs = []

    fixtures = []

    def build(self, parent=None):
        pass

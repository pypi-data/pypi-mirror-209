from typing import List

from rick.mixin.injectable import Injectable

from pokie.constants import DI_DB
from rick_db import Repository

from pokie_location.dao import CountryRecord, TimeZoneRecord


class LocationService(Injectable):
    countries = None
    timezones = None

    def get_countries(self) -> List[CountryRecord]:
        return self._get_country_records()

    def country_list(self) -> dict:
        result = {}
        for record in self._get_country_records():
            result[record.code] = record.name
        return result

    def get_timezones(self) -> List[TimeZoneRecord]:
        return self._get_tz_records()

    def timezone_list(self) -> List:
        result = []
        for r in self._get_tz_records():
            result.append(r.timezone)
        return result

    def purge_cache(self):
        self.timezones = None
        self.countries = None

    @property
    def country_repository(self):
        return Repository(self.get_di().get(DI_DB), CountryRecord)

    @property
    def tz_repository(self):
        return Repository(self.get_di().get(DI_DB), TimeZoneRecord)

    def _get_tz_records(self) -> List[TimeZoneRecord]:
        if self.timezones is None:
            self.timezones = self.tz_repository.fetch_all_ordered(
                TimeZoneRecord.timezone
            )
        return self.timezones

    def _get_country_records(self) -> List[CountryRecord]:
        if self.countries is None:
            self.countries = self.country_repository.fetch_all_ordered(
                CountryRecord.name
            )
        return self.countries

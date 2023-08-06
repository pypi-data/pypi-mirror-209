from rick_db import fieldmapper


@fieldmapper(tablename="country", pk="id_country")
class CountryRecord:
    code = "id_country"
    name = "name"


@fieldmapper(tablename="timezone", pk="id_timezone")
class TimeZoneRecord:
    timezone = "id_timezone"
    country_code = "fk_country"

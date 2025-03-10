from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


class DateTimeFormatEnumeration(Enum):
    """The DateTimeFormatEnumeration simple type defines the different date-time
    formats that are understood by OVAL.

    Note that in some cases there are a few different possibilities
    within a given format. Each of these possibilities is unique though
    and can be distinguished from each other. The different formats are
    used to clarify the higher level structure of the date-time string
    being used.

    :cvar YEAR_MONTH_DAY: The year_month_day value specifies date-time
        strings that follow the formats: 'yyyymmdd', 'yyyymmddThhmmss',
        'yyyy/mm/dd hh:mm:ss', 'yyyy/mm/dd', 'yyyy-mm-dd hh:mm:ss', or
        'yyyy-mm-dd'
    :cvar MONTH_DAY_YEAR: The month_day_year value specifies date-time
        strings that follow the formats: 'mm/dd/yyyy hh:mm:ss',
        'mm/dd/yyyy', 'mm-dd-yyyy hh:mm:ss', 'mm-dd-yyyy', 'NameOfMonth,
        dd yyyy hh:mm:ss' or 'NameOfMonth, dd yyyy',
        'AbreviatedNameOfMonth, dd yyyy hh:mm:ss', or
        'AbreviatedNameOfMonth, dd yyyy'
    :cvar DAY_MONTH_YEAR: The day_month_year value specifies date-time
        strings that follow the formats: 'dd/mm/yyyy hh:mm:ss',
        'dd/mm/yyyy', 'dd-mm-yyyy hh:mm:ss', or 'dd-mm-yyyy'
    :cvar WIN_FILETIME: The win_filetime value specifies date-time
        strings that follow the windows file time format.
    :cvar SECONDS_SINCE_EPOCH: The seconds_since_epoch value specifies
        date-time values that represent the time in seconds since the
        UNIX epoch.  The Unix epoch is the time 00:00:00 UTC on January
        1, 1970.
    :cvar CIM_DATETIME: The cim_datetime model is used by WMI and its
        value specifies date-time strings that follow the format:
        'yyyymmddHHMMSS.mmmmmmsUUU', and alternatively 'yyyy-mm-dd
        HH:MM:SS:mmm' only when used in WMI Query Language queries.
    """

    YEAR_MONTH_DAY = "year_month_day"
    MONTH_DAY_YEAR = "month_day_year"
    DAY_MONTH_YEAR = "day_month_year"
    WIN_FILETIME = "win_filetime"
    SECONDS_SINCE_EPOCH = "seconds_since_epoch"
    CIM_DATETIME = "cim_datetime"

# -*- coding: utf-8 -*-
import enum
import logging
from enum import Enum, auto

from PyQt5.QtGui import QIcon

__all__ = ['StateAction', 'StateColor', 'Icon', 'ProjectTypes',
           'MeterTypes', 'DataType']

LOG_LEVEL_MAP = {'debug': logging.DEBUG, 'info': logging.INFO,
                 'warning': logging.WARNING, 'error': logging.ERROR,
                 'critical': logging.CRITICAL}


class StateAction(enum.Enum):
    CREATE = auto()
    UPDATE = auto()
    DELETE = auto()


class StateColor(enum.Enum):
    ACTIVE = '#11dd11'
    INACTIVE = '#ffffff'


class Icon(enum.Enum):
    """Resource Icon paths for Qt resources"""
    AUTOSIZE = ":/icons/autosize"
    OPEN_FOLDER = ":/icons/folder_open"
    AIRBORNE = ":/icons/airborne"
    MARINE = ":/icons/marine"
    METER = ":/icons/sensor"
    DGS = ":/icons/dgs"
    DGP = ":/icons/dgp_large"
    DGP_SMALL = ":/icons/dgp"
    DGP_NOTEXT = ":/icons/dgp_notext"
    GRAVITY = ":/icons/gravity"
    TRAJECTORY = ":/icons/gps"
    NEW_FILE = ":/icons/new_file"
    SAVE = ":/icons/save"
    DELETE = ":/icons/delete"
    ARROW_LEFT = ":/icons/chevron-right"
    ARROW_DOWN = ":/icons/chevron-down"
    LINE_MODE = ":/icons/line_mode"
    PLOT_LINE = ":/icons/plot_line"
    SETTINGS = ":/icons/settings"
    INFO = ":/icons/info"
    HELP = ":/icons/help_outline"
    GRID = ":/icons/grid_on"
    NO_GRID = ":/icons/grid_off"

    def icon(self):
        return QIcon(self.value)


class LogColors(Enum):
    DEBUG = 'blue'
    INFO = 'yellow'
    WARNING = 'brown'
    ERROR = 'red'
    CRITICAL = 'orange'


class ProjectTypes(enum.Enum):
    AIRBORNE = 'airborne'
    MARINE = 'marine'


class MeterTypes(enum.Enum):
    """Gravity Meter Types"""
    AT1A = 'at1a'
    AT1M = 'at1m'
    ZLS = 'zls'
    TAGS = 'tags'


class DataType(enum.Enum):
    """Gravity/Trajectory Data Types"""
    GRAVITY = 'gravity'
    TRAJECTORY = 'trajectory'


class GravityTypes(enum.Enum):
    # TODO: add set of fields specific to each dtype
    AT1A = ('gravity', 'long_accel', 'cross_accel', 'beam', 'temp', 'status',
            'pressure', 'Etemp', 'gps_week', 'gps_sow')
    AT1M = ('at1m',)
    ZLS = ('line_name', 'year', 'day', 'hour', 'minute', 'second', 'sensor',
           'spring_tension', 'cross_coupling', 'raw_beam', 'vcc', 'al', 'ax',
           've2', 'ax2', 'xacc2', 'lacc2', 'xacc', 'lacc', 'par_port',
           'platform_period')
    TAGS = ('tags', )


class GPSFields(enum.Enum):
    sow = ('week', 'sow', 'lat', 'long', 'ell_ht')
    hms = ('mdy', 'hms', 'lat', 'long', 'ell_ht')
    serial = ('datenum', 'lat', 'long', 'ell_ht')



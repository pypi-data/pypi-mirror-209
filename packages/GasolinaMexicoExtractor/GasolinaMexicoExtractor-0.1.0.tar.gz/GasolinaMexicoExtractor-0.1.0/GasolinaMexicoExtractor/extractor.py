from GasolinaMexicoScrapper import scrapper
from datetime import datetime
import os
import json
import pytz

TIMEZONE = pytz.timezone('America/Mexico_City')
DATE_FORMAT = '%Y_%m_%d'
TIME_FORMAT = '%H:%M:%S(%z)'
DATETIME_FORMAT = f"{DATE_FORMAT}T{TIME_FORMAT}"


class GasPriceExtractor:
    __save_path = None
    __work_space = None
    __filename = f"{TIMEZONE.localize(datetime.now()).strftime(DATE_FORMAT)}.json"
    __start_timestamp = None
    __end_timestamp = None
    _data = {}

    def __init__(self, save_path: str, branch: str):
        self.__save_path = save_path

        if not self.__check_save_path():
            print(f"Save path ({self.__save_path}) does not exists")

        if not self.__prepare_workspace(branch=branch):
            print(f"Workspace ({self.__work_space}) is not ready")

    def _start(self):
        now = TIMEZONE.localize(datetime.now())
        self.__start_timestamp = now.strftime(DATETIME_FORMAT)

    def _end(self):
        now = TIMEZONE.localize(datetime.now())
        self.__end_timestamp = now.strftime(DATETIME_FORMAT)

    def __check_save_path(self) -> bool:
        return os.path.exists(self.__save_path) and os.path.isdir(self.__save_path)

    def __prepare_workspace(self, branch) -> bool:
        self.__work_space = os.path.join(self.__save_path, branch)
        if not os.path.exists(self.__work_space):
            os.makedirs(self.__work_space, exist_ok=True)
        return os.path.exists(self.__work_space) and os.path.isdir(self.__work_space)

    def _save_data(self) -> bool:
        if not self.__work_space:
            return False
        file_path = os.path.join(self.__work_space, self.__filename)
        with open(file_path, "w") as f:
            f.write(self.data)
        return True

    @property
    def data(self):
        self._data.update(
            {
                "starts": self.__start_timestamp,
                "ends": self.__end_timestamp,
            }

        )
        return json.dumps(self._data)


class StateGasPriceExtractor(GasPriceExtractor):
    state_name = None
    __towns = []

    def __init__(self, state_name: str, save_path: str):
        super().__init__(save_path=save_path, branch=state_name)

        self.state_name = state_name
        self._fetch_state_data()
        self._save_data()

    @property
    def towns(self) -> list:
        return self.__towns

    def _fetch_state_data(self):
        self._start()
        self._data = scrapper.get_state(state=self.state_name)
        for town in self._data.get('towns', []):
            self.__towns.append(town)
        self._end()


class TownGasPriceExtractor(GasPriceExtractor):
    state_name = None
    town_name = None
    __stations = []

    def __init__(self, state_name: str, town_name: str, save_path: str):
        branch = f"{state_name}/{town_name}"
        super().__init__(save_path=save_path, branch=branch)

        self.state_name = state_name
        self.town_name = town_name
        self._fetch_town_data()
        self._save_data()

    @property
    def stations(self) -> list:
        return self.__stations

    def _fetch_town_data(self):
        self._start()
        self._data = scrapper.get_town(state=self.state_name, city=self.town_name)
        for station in self._data.get('stations', []):
            self.__stations.append(station)
        self._end()


class StationGasPriceExtractor(GasPriceExtractor):
    station_id = None
    station_slug = None
    state_name = None
    town_name = None

    def __init__(self, state_name: str, town_name: str, station_id: str, station_slug: str, save_path: str):
        branch = f"stations/{station_id}___{station_slug}"
        super().__init__(save_path=save_path, branch=branch)

        self.station_id = station_id
        self.station_slug = station_slug
        self.town_name = town_name
        self.state_name = state_name
        self._fetch_station_data()
        self._save_data()

    def _fetch_station_data(self):
        self._start()
        self._data = scrapper.get_station(
            state=self.state_name, city=self.town_name, id=self.station_id, name=self.station_slug

        )
        self._end()

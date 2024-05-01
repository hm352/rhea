from datetime import datetime
import requests
import json
import logging

import pandas


def get_data(url, params=None):
    data = requests.get(url, params=params).json()
    return data


if __name__ == "__main__":
    # readings_url = "https://environment.data.gov.uk/flood-monitoring/data/readings?latest"
    # readings = get_data(readings_url)
    stations_url = "http://environment.data.gov.uk/flood-monitoring/id/stations"
    stations = get_data(stations_url)
    run_time = datetime.now().strftime("%Y-%m-%d-%H:%M")
    with open(f"data/stations/{run_time}.json", "w+") as file:
        file.write(json.dumps(stations))
        measures_url = "http://environment.data.gov.uk/flood-monitoring/id/measures"

    measurements = get_data(measures_url)
    with open(f"data/measurements/{run_time}.json", "w+") as file:
        file.write(json.dumps(stations))

    measures = measurements.get("items", [])
    station_items = stations.get("items", [])

    if not measures and station_items:
        logging.info("there is no data to match")
        exit

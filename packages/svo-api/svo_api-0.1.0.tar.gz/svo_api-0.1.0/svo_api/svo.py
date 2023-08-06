import os
import requests


def get_response(url):
    """Obtains the response from a given Wiserep URL.

    Parameters
    ----------
    url: str
        Wiserep URL.

    Returns
    -------
    response: requests.Response
        Response object.
    """
    response = requests.get(url)

    if response.status_code == 200:
        return response
    else:
        return None


def get_facilities():
    """Gets a list of all the observational facilities in SVO.

    Returns
    -------
    facilities: list
        Observational facilities.
    """
    # SVO main filters' webpage
    svo_url = "http://svo2.cab.inta-csic.es/theory/fps/fps.php"
    response = get_response(svo_url)

    # get where the observational facilities are listed
    split_text = response.text.split("<PARAM")
    for section in split_text:
        if "INPUT:Facility" in section:
            facilities_section = section

    # obtain list of facilities
    facilities = []
    split_section = facilities_section.split("<OPTION")[1:]
    for line in split_section:
        facility = line.split('"')[1]
        facilities.append(facility)

    return facilities


def get_filters_sets(facility):
    """Gets a list of filters sets for a given facility.

    Parameters
    ----------
    facility: str
        Name of the observational facility.

    Returns
    -------
    filters_sets: list
        Filters sets.
    """
    # get the facility's SVO URL
    search_url = "http://svo2.cab.inta-csic.es/theory/fps/index.php?"
    facility_url = search_url + f"mode=browse&gname={facility}&asttype="
    response = get_response(facility_url)

    # get list of filters sets
    filters_sets = []
    filters_split = response.text.split(f"gname={facility}&gname2=")[1:]
    for line in filters_split:
        if len(line.split("&asttype=")) > 1:
            filter_set = line.split("&asttype=")[0]
            filters_sets.append(filter_set)

    if len(filters_sets) == 0:
        filters_sets = [facility]

    return filters_sets


def get_filters(facility, filters_sets=None, verbose=False):
    """Gets a list of filters for a given facility.

    Parameters
    ----------
    facility: str
        Name of the observational facility.
    filters_sets: str or list, default ``None``
        Name of the filters set(s). If not given, gets all the filters.
    verbose: bool, default ``False``
        If ``True``, the filter_set+filter name is printed.

    Returns
    -------
    filters: list
        Filters for the facility.
    """
    search_url = "http://svo2.cab.inta-csic.es/theory/fps/index.php?"
    if filters_sets is None:
        filters_sets = get_filters_sets(facility)
    else:
        if isinstance(filters_sets, str) is True:
            filters_sets = [filters_sets]
        valid_filters_sets = get_filters_sets(facility)
        for filter_set in filters_sets:
            assert (
                filter_set in valid_filters_sets
            ), f"Not a valid filter set ({filter_set}): {valid_filters_sets}"
    filters = []

    for filter_set in filters_sets:
        # get the facility + filters set's SVO URL
        filters_url = (
            search_url + f"mode=browse&gname={facility}&gname2={filter_set}&asttype="
        )
        response = get_response(filters_url)

        # get list of filters
        filters_split = response.text.split(f"gname={facility}&gname2={filter_set}")
        for line in filters_split:
            if line.startswith("#filter"):
                line_split = line.split("/")
                filt = line_split[1][:-1]
                filters.append(filt)

                if verbose is True:
                    print(f"{filter_set}/{filt}")

    return filters


def download_filter(facility, filter_sets=None):
    """Downloads a filter file in ascii format form the SVO website.

    The output file name has the same name as the filter, with '.dat'
    extension.

    Parameters
    ----------
    facility: str
        Name of the observational facility.
    filter_sets: str or list, default ``None``
        Name of the filters set(s). If not given, gets all the filters.
    """
    filters = get_filters(facility, filter_sets)

    for filt in filters:
        # get-data URL
        getdata_url = "http://svo2.cab.inta-csic.es/theory/fps/getdata.php?"
        filter_url = getdata_url + f"format=ascii&id={facility}/{filt}"

        # output file
        response = get_response(filter_url)
        outfile = os.path.join(facility, f"{filt}.dat")

        # check if the directory exists
        if not os.path.isdir(facility):
            os.mkdir(facility)

        # save data
        with open(outfile, "wb") as file:
            file.write(response.content)

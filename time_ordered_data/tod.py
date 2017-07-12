#!/usr/bin/python
"""
Script to simulate time-ordered data generated by a CMB experiment
scanning the sky.

Author: Julien Peloton, j.peloton@sussex.ac.uk
"""
from __future__ import division, absolute_import, print_function

import numpy as np

import detector_pointing

class TimeOrderedData():
    """ Class to handle Time-Ordered Data (TOD) """
    def __init__(self, hardware, scanning_strategy, HealpixFitsMap):
        """
        C'est parti!

        Parameters
        ----------
        hardware : hardware instance
            Instance of hardware containing instrument parameters and models.
        scanning_strategy : scanning_strategy instance
            Instance of scanning_strategy containing scan parameters.
        HealpixFitsMap : HealpixFitsMap instance
            Instance of HealpixFitsMap containing input sky parameters.
        """
        self.hardware = hardware
        self.scanning_strategy = scanning_strategy
        self.HealpixFitsMap = HealpixFitsMap

        self.pointing = None

    def ComputeBoresightPointing(self, ut1utc_fn=None):
        """
        Compute the boresight pointing for all the focal plane bolometers.
        """
        lat = float(
            self.scanning_strategy.telescope_location.lat) * 180. / np.pi

        self.pointing = detector_pointing.pointing(
            az_enc=self.scanning_strategy.scan0['azimuth'],
            el_enc=self.scanning_strategy.scan0['elevation'],
            time=self.scanning_strategy.scan0['clock-utc'],
            value_params=self.hardware.pointing_model.value_params,
            allowed_params=self.hardware.pointing_model.allowed_params,
            ut1utc_fn=ut1utc_fn,
            ra_src=self.scanning_strategy.ra_mid,
            dec_src=self.scanning_strategy.dec_mid,
            lat=lat)

    def get_tod(self):
        """
        Scan the input sky maps to generate timestreams.
        """
        pass

    def map_tod(self):
        """
        Project time-ordered data into sky maps.
        """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
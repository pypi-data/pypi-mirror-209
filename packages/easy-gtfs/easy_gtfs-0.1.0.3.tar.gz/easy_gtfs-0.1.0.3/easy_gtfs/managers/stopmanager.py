"""
    Module to manage multiple 'Stop' models, write them to a file, load them from a file or parse them from a json object.

    Author: Felix Michelis
    Date: 19/05/2023
        dd/mm/yyyy
"""
from pydantic import ValidationError
from typing import Optional, List
import csv
from collections import Counter
import json


from ..utility import get_error_manager
from ..objects.stop import Stop
from ..models.errors import ErrorTypes, StopError




class Stops():
    """A class to manage multiple 'Stop' models and write them to a file, load them from a file or parse them from a json object."""

    def __init__(self, stops: List[Stop] = None, file: str = None):
        """
            A class to manage multiple 'Stop' models and write them to a file, load them from a file or parse them from a json object.

            :param agencies [List[Stop]] -- A list of 'Stop' models, can be passed later with the respective function on function call
            :param file [str] -- The file to write to or load from, can be passed later with the respective function on function call
        """
        self.error_manager = get_error_manager()
        self.stops: List[Stop] = stops
        self.file: str = file
    

    def to_file(self, stops: Optional[List[Stop]] = None, file: Optional[str] = None) -> bool:
        """
            Writes a list of 'Stop' models to a file in csv format.

            :param stopss [Optional[List[Stop]]] -- A list containing 'Stop' models, if not given it will take 'self.stops' if set
            :param file [Optional[str]] -- The file to write to, if not given it will take 'self.file' if set

            :return bool -- True on success, else False or raises Error if not silent error enabled
        """

        if not agencies:
            if self.stops == None:
                raise TypeError("Got no stops to write to file!")
            agencies = self.stops

        if not file:
            if self.file == None:
                raise TypeError("Got no file to write to!")
            file = self.file


        headers: list = [variable for variable in stops[0].dict(exclude_unset=False).keys()] # create a list of the headers for the csv file
        rows: list = []
        
        stops_ids = [] # this list stores the ids of all the stops that will be written to the file so we can verify that no agencies have the same id
        for obj in stops:
            obj_as_dict = obj.dict(exclude_unset=False)
            stops_ids.append(obj_as_dict["stop_id"]) # add the id of the stop to our ids list for verification later on
            rows.append(obj_as_dict) # add the Stop as json to our rows that will be written to the csv file

        if len(stops_ids) > 1:
            duplicates = [k for k, v in Counter(stops_ids).items() if v>1] # returns a list with all duplicate ids; if the id '123' was for example at least 2 times in the ids list the output would be: ['123']
            if len(duplicates) > 0:
                if self.error_manager.is_silent_errors():
                    self.error_manager.add_error(StopError(
                        error_type=ErrorTypes.StopErrorDuplicateID,
                        message="Multiple stops cannot have the same id!",
                        values = duplicates
                    ))
                    return False
                else:
                    raise ValueError(f"Multiple stops cannot have the same id! Got the following duplicate ids: {duplicates}")
            

        with open(file, "w", newline='') as _file:
            csvwriter = csv.DictWriter(_file, fieldnames=headers)
            csvwriter.writeheader()
            csvwriter.writerows(rows)


        return True



    def parse(self, stops_list: List[dict]) -> List[Stop]:
        """
            Converts a list of dictionaries which each represent an 'Stop' to a list of 'Stop' models.
        """
        stops = []

        for Stop in stops_list:
            if self.is_valid_Stop(Stop):
                stops.append(Stop.parse_obj(Stop))
            else:
                if self.error_manager.is_silent_errors():
                    self.error_manager.add_error(StopError(
                        error_type = ErrorTypes.StopErrorInvalidStop,
                        message="Invalid stop from dict!",
                        values = [Stop]
                    ))
                    return False
                else:
                    raise ValueError(f"Invalid stop: {Stop}")

        return stops
    


    def load_file(self, file: Optional[str] = None) -> List[Stop]:
        """
            Reads a file in csv format and outputs a list of 'Stop' models contained in that file.

            :param file [Optional[str]] -- The file to read from, if not given it will take 'self.file' if its set

            :return List[Stop] -- A list conatining 'Stop' models
        """

        if not file:
            if self.file == None:
                raise TypeError("Got no file to load from!")
            file = self.file
        

        with open(file, "r") as _file:
            csvreader = list(csv.DictReader(_file)) # gives a list of dictionaries where each dict is a json representation of an Stop

        stops = self.parse(csvreader)

        stops_ids = []

        for Stop in stops:
            if Stop.stop_id in stops_ids:
                if self.error_manager.is_silent_errors():
                    self.error_manager.add_error(StopError(
                        error_type = ErrorTypes.StopErrorDuplicateID,
                        message="Cannot have multiple stops with the same id!",
                        values = [Stop.stop_id]
                    ))
                    return False
                else:
                    raise ValueError("Cannot have multiple stops with the same id!")
            stops_ids.append(Stop.stop_id)

        return stops

        
    def is_valid_Stop(self, stop: dict) -> bool:
        """
            Checks if a dict is a valid 'Stop' model.

            :param stop [dict] -- The dict to validate
            
            :return bool -- 'True' if it contains a valid model, otherwise ('False', dict[argument_causing_error: error_message])
        """

        try:
            Stop.parse_obj(Stop)

        except ValidationError as e:
            errors = {}

            for error in json.loads(e.json()):
                errors[error["loc"][0]] = error["msg"]

            return (False, errors)
        
        return True
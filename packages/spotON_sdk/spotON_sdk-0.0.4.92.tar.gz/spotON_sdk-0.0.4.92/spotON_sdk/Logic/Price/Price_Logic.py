from typing import List, Optional,Union
from pydantic import BaseModel, Field, validator, root_validator
from enum import Flag, auto
from dataclasses import dataclass, field
from .markets import Markets,Market




class TimeFrame_Type(Flag):
    WHOLE_DAY = auto()
    TIMEFRAME = auto()

class Timeframe(BaseModel):
    start_hour : int 
    end_hour : int 
    possibel_hours : List[int] = Field(default_factory=list)



class Wholeday(Timeframe):
    start_hour :int = field(default=0)
    end_hour :int = field(default=24)
    possibel_hours : List[int] = Field(default_factory=lambda :  [*range(0,24)])

class Timeframe_as_Int(Timeframe):

    # validate start_hour and end_hour is not negative or greater than 24
    @validator('start_hour','end_hour')
    def start_hour_and_end_hour_must_be_between_0_and_24(cls, v):
        if v < 0 or v > 24:
            raise ValueError('start_hour and end_hour must be between 0 and 24')
        return v

    # implement a function that takes start hour and end hour and returns a list of possible hours in between a smaller end value means the timeframe goes over midnight write the values in the possible hours list
    def calculate_possible_hours_from_timeframe(self):
        possible_hours = []
        start,end = self.start_hour,self.end_hour
        def loop_Hours(_start,_end):
            for hour in range (_start,_end):
                possible_hours.append(hour)
            
        if start < end:
            loop_Hours(start,end)
        elif start > end :
            loop_Hours(start,25)
            loop_Hours(0,end)


class Segmented(Timeframe):
    timeframe : List[Timeframe_as_Int] = Field(default_factory=list)
    pass

class Pricefinding(BaseModel):
    pass

class Interrupted(Pricefinding):
    pass

class Continuous(Pricefinding):
    week :int = Field(default=None)

class Price_Logic(BaseModel):
    nr_of_hours_on: int
    market: Union[str, Market] 
    timeframe: Timeframe = Field(default_factory=lambda: Wholeday())
    pricefinding : Continuous | Interrupted = Field(default_factory=lambda: Interrupted())

    resolution: float = Field(default=1)
    timeframe_longer_than_nr_of_hours_on :bool = Field(default=False)
    # root validator to set the market to the correct market object if it is a string
    @root_validator(pre=True)
    def set_market_to_market_object(cls, values):
        if isinstance(values["market"], str):
            result = Markets.get_market_by_name(values["market"])
            result = Markets.get_market_by_code(values["market"])
            if result is None:
                raise ValueError("Market is not valid")
            else:
                values["market"] = result
        return values
    
    @validator('nr_of_hours_on')
    def nr_of_hours_on_must_be_greater_than_0(cls, v):
        if v == 0:
            raise ValueError('nr_of_hours_on must be greater than 0')
        return v
    
    @root_validator(pre=True)
    def set_timeframe_type_to_whole_day_if_possible_hours_is_24(cls, values):
        if values["timeframe"].possibel_hours == [*range(0,24)]:
            values["timeframe_type"] = TimeFrame_Type.WHOLE_DAY
        return values

    # Validate that the timeframe is not shorter than the nr_of_hours_on
    @validator('timeframe')
    def timeframe_must_be_longer_than_nr_of_hours_on(cls, v, values):
        if values["nr_of_hours_on"] > len(v.possibel_hours):
            timeframe_longer_than_nr_of_hours_on = True
        return v
from dataclasses import dataclass


@dataclass
class PathParams:
    module_path:str
    src_path:str
    system_path:str


@dataclass
class RunParams:
    test:bool


@dataclass
class CommonParams:
    date:str
    now:str


@dataclass
class Params:
    path:PathParams
    run:RunParams
    common:CommonParams
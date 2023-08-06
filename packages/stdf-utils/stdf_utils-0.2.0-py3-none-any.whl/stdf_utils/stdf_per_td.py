import os.path
from collections import defaultdict
from copy import copy
from .stdf_record import StdfRecord
from .util import OpenFile


class StdfPerTD:
    def __init__(self, stdf_path: str, ptr_filter=None, ptr_extra_fields=None):
        self.stdf_path = stdf_path
        self.ptr_filter = ptr_filter or (lambda x: True)
        self.ptr_extra_fields = ptr_extra_fields or (lambda x: {})
        self.previous_rec: dict = {}
        self.handlers = {
            "Mir": self.mir_handler,
            "Ptr": self.ptr_handler,
            "Prr": self.prr_handler,
        }
        # cache
        self.mir = {}
        self.prr = {}
        self.ptr = defaultdict(list)

    def __iter__(self):
        # reset
        self.mir.clear()
        self.prr.clear()
        self.ptr.clear()
        with OpenFile(self.stdf_path) as f_in:
            for rec_type, rec in StdfRecord(f_in, set(self.handlers.keys())):
                self.handlers[rec_type](rec)
                if rec_type == "Prr":
                    site = self.prr["site"]
                    yield {
                        "mir": copy(self.mir),
                        "prr": copy(self.prr),
                        "ptr": self.ptr.pop(site) if site in self.ptr else [],
                    }

    def mir_handler(self, d: dict) -> None:
        self.mir = {
            "node": d["NODE_NAM"].decode(),
            "job": d["JOB_NAM"].decode().split("/")[-1].replace(".prog", ""),
            "name": os.path.basename(self.stdf_path).split(".")[0],
        }

    def ptr_handler(self, d: dict) -> None:
        site: int = d["SITE_NUM"]
        if self.ptr_filter(d):
            self.ptr[site].append({
                "t_num": d["TEST_NUM"],
                "text": d["TEST_TXT"].decode(),
                "val": d['RESULT'],
                "lo_lim": d['LO_LIMIT'],
                "hi_lim": d['HI_LIMIT'],
                "unit": d['UNITS'].decode(),
                **self.ptr_extra_fields(d)
            })

    def prr_handler(self, d: dict) -> None:
        self.prr = {
            "part_id": d["PART_ID"].decode(),
            "site": d["SITE_NUM"],
            "x": d["X_COORD"],
            "y": d["Y_COORD"],
            "sb": d["SOFT_BIN"],
            "hb": d["HARD_BIN"],
        }

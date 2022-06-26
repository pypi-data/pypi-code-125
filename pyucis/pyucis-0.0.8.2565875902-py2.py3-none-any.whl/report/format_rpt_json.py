'''
Created on Apr 8, 2020

@author: ballance
'''
import json
import os
from typing import List
import python_jsonschema_objects as pjs

from ucis.report.coverage_report import CoverageReport
from ucis.report.coverage_report_builder import CoverageReportBuilder
from ucis.rgy.format_if_rpt import FormatIfRpt
from ucis.ucis import UCIS


class FormatRptJson(FormatIfRpt):
    
    def __init__(self):
        self._report = None
        self._fp = None
        self._data = {}
        self._ind = ""
        self.details = False
        self.order_bins_by_hit = False
        
    def report(self, 
               db : UCIS,
               out,
               args):
        report = CoverageReportBuilder.build(db)
        self._fp = out
        self._ns = FormatRptJson.getCoverageNS()
        
        covreport = self._ns.CoverageReport()

        covreport.coverage = report.coverage
        
        for cg in self._report.covergroups:
            if covreport.covergroups is None:
                covreport.covergroups = []
            covreport.covergroups.append(self.report_covergroup(cg))
            
        json.dump(covreport.as_dict(), out)
            
    @classmethod
    def getCoverageNS(cls):
        if cls._coverage_ns is None:
            schema = cls.getCovReportSchema()
            builder = pjs.ObjectBuilder(schema)
            cls._coverage_ns = builder.build_classes()
        return cls._coverage_ns
    
    @classmethod
    def getCovReportSchema(cls):
        if cls._coverage_schema is None:
            yaml_dir = os.path.dirname(os.path.abspath(__file__))
            schema_dir = os.path.join(os.path.dirname(yaml_dir), "schema")

            with open(os.path.join(schema_dir, "covreport.json"), "r") as fp:
                cls._coverage_schema = json.load(fp)
        return cls._coverage_schema            
            
    def report_covergroup(self, cg : CoverageReport.Covergroup):
            
        cg_j = self._ns.CovergroupType()
        cg_j.coverage = cg.coverage
        
        for cp in cg.coverpoints:
            if cg_j.coverpoints is None:
                cg_j.coverpoints = []
            cg_j.coverpoints.append(self.report_coverpoint(cp))
                
        for cr in cg.crosses:
            if cg_j.crosses is None:
                cg_j.crosses = []
            cg_j.crosses.append(self.report_cross(cr))
        
        for cg_i in cg.covergroups:
            if cg_j.covergroups is None:
                cg_j.covergroups = []
            cg_j.covergroups.append(self.report_covergroup(cg_i))
                
        return cg_j
            
    def report_coverpoint(self, cp : CoverageReport.Coverpoint):
        
        cp_j = self._ns.Coverpoint()
        cp_j.coverage = cp.coverage
        
        if self.details:
            if cp.bins is not None:
                cp_j.bins = []
                for b in cp.bins:
                    b_j = self._ns.CoverBin()
                    b_j.name = b.name
                    b_j.count = b.count
                    cp_j.bins.append(b_j)
            # self.writeln("Bins:")
            # with self.indent():
            #     self.report_bins(cp.bins)
            # if len(cp.ignore_bins) > 0:
            #     self.writeln("IgnoreBins:")
            #     with self.indent():
            #         self.report_bins(cp.ignore_bins)
            # if len(cp.illegal_bins) > 0:
            #     self.writeln("IllegalBins:")
            #     with self.indent():
            #         self.report_bins(cp.illegal_bins)
                    
        return cp_j

    def report_cross(self, cr : CoverageReport.Cross):
        
        cr_j = self._ns.Cross()
        cr_j.name = cr.name
        cr_j.weight = cr.weight
        
        self.writeln("CROSS %s : %f%%", cr.name, round(cr.coverage))
        
        if self.details:
            if cr.bins is not None:
                cr_j.bins = []
                for b in cr.bins:
                    b_j = self._ns.CoverBin()
                    b_j.name = b.name
                    b_j.count = b.count
                    cr_j.bins.append(b_j)

        return cr_j

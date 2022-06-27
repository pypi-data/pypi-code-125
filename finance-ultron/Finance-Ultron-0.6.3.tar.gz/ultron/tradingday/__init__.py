# -*- coding: utf-8 -*-
from ultron.tradingday.Calendar import Calendar
from ultron.tradingday.Date import Date
from ultron.tradingday.Date import check_date
from ultron.tradingday.Period import Period
from ultron.tradingday.Period import check_period
from ultron.tradingday.Schedule import Schedule
from ultron.tradingday.Enums import BizDayConventions
from ultron.tradingday.Enums import DateGeneration
from ultron.tradingday.Enums import TimeUnits


def isBizDay(holidayCenter, ref):
    cal = Calendar(holidayCenter)
    ref = check_date(ref)
    return cal.isBizDay(ref)


def datesList(fromDate, toDate):
    fromDate = check_date(fromDate)
    toDate = check_date(toDate)
    return [Date.fromExcelSerialNumber(serial).toDateTime() for serial in
            range(fromDate.serialNumber, toDate.serialNumber + 1)]


def bizDatesList(holidayCenter, fromDate, toDate):
    cal = Calendar(holidayCenter)
    fromDate = check_date(fromDate)
    toDate = check_date(toDate)
    return [d.toDateTime() for d in cal.bizDatesList(fromDate, toDate)]


def holDatesList(holidayCenter, fromDate, toDate, includeWeekend=True):
    cal = Calendar(holidayCenter)
    fromDate = check_date(fromDate)
    toDate = check_date(toDate)
    return [d.toDateTime() for d in cal.holDatesList(fromDate, toDate, includeWeekend)]


def advanceDate(referenceDate, period):
    d = check_date(referenceDate) + period
    return d.toDateTime()


def adjustDateByCalendar(holidayCenter, referenceDate, convention=BizDayConventions.Following):
    cal = Calendar(holidayCenter)
    refer = check_date(referenceDate)
    return cal.adjustDate(refer, convention).toDateTime()


def advanceDateByCalendar(holidayCenter, referenceDate, period, convention=BizDayConventions.Following):
    cal = Calendar(holidayCenter)
    refer = check_date(referenceDate)
    period = check_period(period)
    return cal.advanceDate(refer, period, convention).toDateTime()


def nthWeekDay(nth, dayOfWeek, month, year):
    date = Date.nthWeekday(nth, dayOfWeek, month, year)
    return date.toDateTime()


def makeSchedule(firstDate,
                 endDate,
                 tenor,
                 calendar='NullCalendar',
                 dateRule=BizDayConventions.Following,
                 dateGenerationRule=DateGeneration.Forward):

    cal = Calendar(calendar)
    firstDate = check_date(firstDate)
    endDate = check_date(endDate)
    tenor = check_period(tenor)

    if tenor.units() == TimeUnits.BDays:
        schedule = []
        if dateGenerationRule == DateGeneration.Forward:
            d = cal.adjustDate(firstDate, dateRule)
            while d <= endDate:
                schedule.append(d)
                d = cal.advanceDate(d, tenor, dateRule)
        elif dateGenerationRule == DateGeneration.Backward:
            d = cal.adjustDate(endDate, dateRule)
            while d >= firstDate:
                schedule.append(d)
                d = cal.advanceDate(d, -tenor, dateRule)
            schedule = sorted(schedule)
    else:
        schedule = Schedule(firstDate, endDate, tenor, cal, convention=dateRule, dateGenerationRule=dateGenerationRule)
    return [d.toDateTime() for d in schedule]



__all__ = ["datesList",
           "bizDatesList",
           "holDatesList",
           "isBizDay",
           "advanceDate",
           "BizDayConventions",
           "DateGeneration",
           "adjustDateByCalendar",
           "advanceDateByCalendar",
           "nthWeekDay",
           "makeSchedule"]

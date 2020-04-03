import QuantLib as ql # version 1.5
import matplotlib.pyplot as plt
from datetime import datetime
#https://quant.stackexchange.com/questions/33604/pricing-of-a-foreign-exchange-vanilla-option
#https://stackoverflow.com/questions/48778712/fx-vanilla-call-price-in-quantlib-doesnt-match-bloomberg

class BlackScholes():
    async def set_values(values_dict):
        print("Entered BlackScholes")
        datetime_start_date = datetime.strptime(values_dict['start_date'], "%m/%d/%Y")
        datetime_expiry_date = datetime.strptime(values_dict['expiry_date'], "%m/%d/%Y")
        spot_rate = (float(values_dict['spot_price']))
        strike_rate = (float(values_dict['strike_price']))

        domestic_interest_rate = (float(values_dict['domestic_interest'])/100)
        foreign_interest_rate = (float(values_dict['foreign_interest'])/100)
        volatility = (float(values_dict['volatility'])/100)

        premium = BlackScholes().floatrounding(float(values_dict['premium']))
        cashflow = BlackScholes().floatrounding(float(values_dict['cashflow']))
        unit_delta = BlackScholes().floatrounding(float(values_dict['unit_delta']))
        position_delta =BlackScholes().floatrounding(float(values_dict['position_delta']))
        quantity = BlackScholes().floatrounding(float(values_dict["quantity"]))
        changed =values_dict['changed']

        expiration_date = ql.Date(datetime_expiry_date.day,datetime_expiry_date.month,datetime_expiry_date.year)
        start_date = ql.Date(datetime_start_date.day,datetime_start_date.month,datetime_start_date.year)
        settlement_date = start_date
        days = ql.Actual365Fixed()
        calendar = ql.Japan()
        frequency = ql.Annual
        day_count = ql.ActualActual().dayCount(start_date, expiration_date)

        ql.Settings.instance().evaluationDate = start_date
        if(values_dict['callput'] == 'Call'):
            option_type = ql.Option.Call
        else:
            option_type = ql.Option.Put
        compounding = ql.Compounded
        payoff = ql.PlainVanillaPayoff(option_type, strike_rate)

        eu_exercise = ql.EuropeanExercise(expiration_date)
        european_option = ql.VanillaOption(payoff, eu_exercise)

        spot_handle = ql.QuoteHandle(ql.SimpleQuote(spot_rate))
        rTS = ql.YieldTermStructureHandle(ql.FlatForward(settlement_date,domestic_interest_rate, days,compounding, frequency))
        fTS = ql.YieldTermStructureHandle(ql.FlatForward(settlement_date,foreign_interest_rate, days,compounding, frequency))
        flat_vol_ts = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(settlement_date, calendar, volatility, days))
        garman_kohlagen_process = ql.GarmanKohlagenProcess(spot_handle, fTS, rTS, flat_vol_ts)

        engine = ql.AnalyticEuropeanEngine(garman_kohlagen_process)

        european_option.setPricingEngine(engine)


        try:
            if(changed == "premium"):
                return BlackScholes().floatrounding(premium), BlackScholes().floatrounding(float(european_option.delta())), BlackScholes().floatrounding(european_option.impliedVolatility(premium, garman_kohlagen_process,0.000000001)*100),False,day_count
            elif(changed == "cashflow"):
                return BlackScholes().floatrounding(cashflow/5), BlackScholes().floatrounding(float(european_option.delta())), BlackScholes().floatrounding(european_option.impliedVolatility(cashflow/5, garman_kohlagen_process,0.000000001)*100),False,day_count
            else:
                return BlackScholes().floatrounding(float(european_option.NPV())),BlackScholes().floatrounding(float(european_option.delta())),BlackScholes().floatrounding(volatility*100),False,day_count
        except:
            return BlackScholes().floatrounding(float(european_option.NPV())),BlackScholes().floatrounding(float(european_option.delta())),BlackScholes().floatrounding(volatility*100),True,day_count

    def floatrounding(self,num):
        return float("{:.6f}".format(num))

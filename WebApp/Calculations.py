import QuantLib as ql # version 1.5
import matplotlib.pyplot as plt

#https://quant.stackexchange.com/questions/33604/pricing-of-a-foreign-exchange-vanilla-option
#https://stackoverflow.com/questions/48778712/fx-vanilla-call-price-in-quantlib-doesnt-match-bloomberg

class Calculations():
    def set_values(self,request_form):
        spot_rate = float(request_form['spotprice'])
        strike_rate = float(request_form['strikeprice'])
        domestic_interest_rate = float(request_form['domesticInterestrate'])
        foreign_interest_rate = float(request_form['foreignInterestrate'])
        volatility = float(request_form['volatility'])
        expiration_date = ql.Date(int(request_form['expirationdate'][8:10]),int(request_form['expirationdate'][5:7]),int(request_form['expirationdate'][0:4]))
        start_date = ql.Date(int(request_form['startdate'][8:10]),int(request_form['startdate'][5:7]),int(request_form['startdate'][0:4]))
        settlement_date = start_date
        days = ql.Actual365Fixed()
        calendar = ql.Japan()
        frequency = ql.Annual
        ql.Settings.instance().evaluationDate = start_date
        if(request_form['callput'] == 'call'):
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

        european_option.setPricingEngine(engine);
        return float(european_option.NPV()),float(european_option.delta())

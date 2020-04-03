from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from wtforms.fields.html5 import DateField

class OptionForm(FlaskForm):
    """Contact form."""
    startdate = DateField('日付', [
        DataRequired()],format='%m/%d/%Y')
    days = StringField('デイカウント', [
        DataRequired()])
    spotprice = DecimalField('現在の価格', [
        DataRequired()])
    strikeprice = DecimalField('行使価格', [
        DataRequired()])
    expirationdate = DateField('満期日', [
        DataRequired()],format='%m/%d/%Y')
    foreignInterestrate = DecimalField('*外国金利', [
        DataRequired()])
    domesticInterestrate = DecimalField('*国内金利', [
        DataRequired()])
    volatility = DecimalField('*ボラティリティ', [
        DataRequired()])
    callput = SelectField('コールプット',choices=[('call', 'Call'), ('put', 'Put')])
    quantity = DecimalField('数量', [
        DataRequired()])
    #add = SubmitField('Add')
    submit = SubmitField('Submit')

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired



class ChooseModel(FlaskForm):
    selectModel = SelectField('Please Choose Your Model',choices=[('perceptron', 'Perceptron'), ('mlp', 'perceptron multicouche'), ('hopfield', 'Hopfield'),('kohonen','Kohonen')])
    submit = SubmitField('Done')



class PerceptronForm(FlaskForm):
    input1 = StringField('threshold exemple : 0,5 ',validators=[DataRequired()])
    input2 = StringField('1ere Input  exemple : 3,4,5 ',validators=[DataRequired()])
    input3 = StringField('2eme Input exemple : 3,4,5 ',validators=[DataRequired()])
    submit1 = SubmitField('Done')



class mlpForm(FlaskForm):
    input4 = StringField('input size exmple : 3 ',validators=[DataRequired()])
    input5 = StringField('Hidden size exemple : 5 ',validators=[DataRequired()])
    input6 = StringField('output size exemple : 6 ',validators=[DataRequired()])
    submit4 = SubmitField('Done')


class hopfieldForm(FlaskForm):
    input7 = StringField('numero de neurouns exemple : 7',validators=[DataRequired()])
    submit7 = SubmitField('Done')


class kohonenForm(FlaskForm):
    input10 = StringField('nombre dimension  exemple : 7 ',validators=[DataRequired()])
    input11= StringField('nombre de neuroune : 6 ',validators=[DataRequired()])
    submit10 = SubmitField('Done')

from flask import Flask, render_template, url_for,redirect
from forms import ChooseModel, PerceptronForm , mlpForm , hopfieldForm , kohonenForm
from functions import  Perceptron , MLP , HopfieldNetwork ,Kohonen
import numpy as np 
app = Flask(__name__)


app.config['SECRET_KEY']= '13018089b72d2fb85b3fae027470f786'

# posts = [{
#     'author':'khalil',
#     'title': 'Project'
# }]

@app.route("/",methods = ['GET','POST'])
@app.route("/choosePage",methods = ['GET','POST'])
def choosePage():
    form = ChooseModel()
    if form.validate_on_submit():
        if form.selectModel.data == 'perceptron':
            return redirect(url_for('perceptron'))
        if form.selectModel.data == 'mlp':
            return redirect(url_for('mlp'))
        if form.selectModel.data == 'hopfield':
            return redirect(url_for('hopfield'))
        if form.selectModel.data == 'kohonen':
            return redirect(url_for('kohonen'))
    return render_template('index.html',form = form)

def resultpercept(resultat):
    return render_template('result.html',resultat = resultat)

def resultmlp(resultat):
    return render_template('resultmlp.html',resultat = resultat)


def resulthopfield(resultat):
    return render_template('resulthopfield.html',resultat = resultat)


def resultkohonen(resultat):
    return render_template('resultkohonen.html',resultat = resultat)


#Perceptron


@app.route("/perceptron",methods = ['GET','POST'])
def perceptron():
    form = PerceptronForm()
    if form.validate_on_submit():
        perceptron = Perceptron(float(form.input1.data))
        inputs = form.input2.data
        inputs = inputs.split(',')
        weights = form.input3.data
        weights = weights.split(',')
        inputs = [float(x) for x in inputs]
        weights = [float(x) for x in weights]
        resultat = perceptron.predict(inputs,weights)
        return resultpercept(resultat)
    return render_template('data.html',form= form)


#perceptron multicouche

@app.route("/mlp",methods = ['GET','POST'])
def mlp():
    form = mlpForm()
    if form.validate_on_submit():
        mlp = MLP(int(form.input4.data),int(form.input5.data),int(form.input6.data))
        inputs = np.random.randn(int(form.input4.data), int(form.input4.data))
        resultat = mlp.predict(inputs)
        return resultmlp(resultat)
    return render_template('data2.html',form= form)


#hopfield


@app.route("/hopfield",methods = ['GET','POST'])
def hopfield():
    form = hopfieldForm()
    if form.validate_on_submit():
        network = HopfieldNetwork(int(form.input7.data))
        inputs = np.random.randn(int(form.input7.data))
        resultat = network.recall(inputs)
        return resulthopfield(resultat)
    return render_template('data3.html',form= form)



@app.route("/kohonen",methods = ['GET','POST'])
def kohonen():
    form = kohonenForm()
    if form.validate_on_submit():
        kohonen = Kohonen(int(form.input10.data),int(form.input11.data))
        inputs = np.random.randn(int(form.input11.data), int(form.input10.data))
        resultat = kohonen.predict(inputs)
        return resultkohonen(resultat)
    return render_template('data4.html',form= form)



if __name__ == '__main__':
    app.run(debug=True)
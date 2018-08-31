from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

import matplotlib
import matplotlib.pyplot as plt, mpld3
import numpy as np

client = MongoClient('localhost', 27017)    #Configure the connection to the database
db = client.Sina    #Select the database
todos = db.Test #Select the collection

app = Flask(__name__)
title = "Flask数据库操作demo"
heading = "Demo"


def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')
           
@app.route('/')
@app.route('/index')
def home():
    return(render_template('index.html'))

@app.route('/pages/<template>')
def pages(template):
    return(render_template('pages/%s'% template +'.html'))
    
@app.route('/urlsqueue')
def urls():
    #Display the all Tasks
    todos_l = db.UrlsQueue.find()
    a1="active"
    return(render_template('pages/urls.html',a1=a1,todos=todos_l,t=title,h=heading))

@app.route('/list')
def lists():
    #Display the all Tasks
    todos_l = todos.find()
    a1="active"
    return(render_template('pages/list.html',a1=a1,todos=todos_l,t=title,h=heading))

@app.route("/search", methods=['GET'])
def search():
	#Searching a Task with various references
	key=request.values.get("key")
	refer=request.values.get("refer")
	if(key=="_id"):
		todos_l = todos.find({refer:ObjectId(key)})
	else:
		todos_l = todos.find({refer:key})
	return(render_template('pages/searchlist.html',todos=todos_l,t=title,h=heading))
    

@app.route("/action", methods=['POST'])
def action ():
	#Adding a Task
	url=request.values.get("url")
	db.UrlsQueue.insert({"url":url,"status":"pending"})
	return(redirect("/urlsqueue"))
   
@app.route("/remove")
def remove ():
	#Deleting a Task with various references
	key=request.values.get("_id")
	db.UrlsQueue.remove({"_id":ObjectId(key)})
	return(redirect("/urlsqueue"))
    
@app.route("/remove2")
def remove2 ():
	#Deleting a Task with various references
	key=request.values.get("_id")
	todos.remove({"_id":ObjectId(key)})
	return(redirect("/list"))
    

@app.route('/plot')
def plot():
    x1=[x-0.3 for x in range(1,13)]
    x2=[x for x in range(1,13)]
    x3=[x+0.3 for  x in range(1,13)]
    like=np.array([17682,  6766,  3209,  1842, 20317,  6719,  3645, 11121,  8326,8428,  8311,  8409])
    transfer=np.array([17682,  6766,  3209,  1842, 20317,  6719,  3645, 11121,  8326,8428,  8311,  8409])
    comment=np.array([ 72401,   1023,   3203,   5760, 178622,   2221,   9991,  37975, 10206,  39684,  10191,  39439])
    xnew=np.array([ 1.3,  1.4,  1.5,  1.6,  1.7,  1.8,  1.9,  2. ,  2.1,  2.2,  2.3,
        2.4,  2.5,  2.6,  2.7,  2.8,  2.9,  3. ,  3.1,  3.2,  3.3,  3.4,
        3.5,  3.6,  3.7,  3.8,  3.9,  4. ,  4.1,  4.2,  4.3,  4.4,  4.5,
        4.6,  4.7,  4.8,  4.9,  5. ,  5.1,  5.2,  5.3,  5.4,  5.5,  5.6,
        5.7,  5.8,  5.9,  6. ,  6.1,  6.2,  6.3,  6.4,  6.5,  6.6,  6.7,
        6.8,  6.9,  7. ,  7.1,  7.2,  7.3,  7.4,  7.5,  7.6,  7.7,  7.8,
        7.9,  8. ,  8.1,  8.2,  8.3,  8.4,  8.5,  8.6,  8.7,  8.8,  8.9,
        9. ,  9.1,  9.2,  9.3,  9.4,  9.5,  9.6,  9.7,  9.8,  9.9, 10. ,
       10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 11. , 11.1,
       11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 12. , 12.1, 12.2])
    ynew=np.array([ 81452.66666667,  73710.8372539 ,  67147.11186622,  61669.15116751,
        57184.61582163,  53601.16649248,  50826.46384393,  48768.16853986,
        47333.94124415,  46431.44262068,  45968.33333333,  45852.27404599,
        45990.92542252,  46291.94812681,  46663.00282274,  47011.75017419,
        47245.85084504,  47272.96549916,  47000.75480044,  46336.87941276,
        45189.        ,  43521.71056215,  41527.3384437 ,  39455.14432526,
        37554.38888741,  36074.33281077,  35264.23677593,  35373.3614635 ,
        36650.96755408,  39346.31572826,  43708.66666667,  49865.0747054 ,
        57453.76880266,  65990.77157217,  74992.10562762,  83973.79358275,
        92451.85805125,  99942.32164685, 105961.20698325, 110024.53667418,
       111648.33333333, 110507.09194957, 106909.19701231, 101321.50538608,
        94210.87393543,  86044.15952491,  77288.21901907,  68409.90928244,
        59876.08717958,  52153.60957503,  45709.33333333,  40902.16982963,
        37659.24848144,  35799.75321686,  35142.86796399,  35507.77665094,
        36713.66320582,  38579.71155673,  40925.10563177,  43569.02935905,
        46330.66666667,  49050.71473189,  51655.9237286 ,  54094.55707982,
        56314.87820861,  58265.15053798,  59893.63749099,  61148.60249065,
        61978.30896002,  62331.02032212,  62155.        ,  61427.55157614,
        60242.13927083,  58721.26746384,  56987.44053491,  55163.16286379,
        53370.93883024,  51733.272814  ,  50372.66919482,  49411.63235246,
        48972.66666667,  49138.00963023,  49828.83118806,  50926.03439814,
        52310.52231841,  53863.19800684,  55464.9645214 ,  56996.72492003,
        58339.3822607 ,  59373.83960137,  59981.        ,  60074.37423629,
        59697.90397691,  58928.13861027,  57841.62752477,  56514.92010883,
        55024.56575084,  53447.11383923,  51859.11376239,  50337.11490873,
        48957.66666667,  47797.3184246 ,  46932.61957095,  46440.11949411,
        46396.36758249,  46877.9132245 ,  47961.30580856,  49723.09472306,
        52239.82935642,  55588.05909704])
    matplotlib.rcParams['font.sans-serif']=['SimHei']
    fig, ax = plt.subplots()
    ax.bar(left=x1, height=like, width=0.3, alpha=0.8, color='red', label="赞")
    ax.bar(left=x2, height=transfer, width=0.3, alpha=0.8, color='green', label="转发")
    ax.bar(left=x3, height=comment, width=0.3, alpha=0.8, color='blue', label="评论")
    ax.plot(xnew,ynew,'--', label="热度曲线")
    plt.legend(loc='upper right')
    ax.grid()
    html_graph = mpld3.fig_to_html(fig)
    return(html_graph)
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
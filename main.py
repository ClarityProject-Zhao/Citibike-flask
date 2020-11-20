import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/occurrence/<int:hr>")
def occurrence(hr):
    area_image_name = [f'images/202008_area_choropleth_{str(hr)}.png' for hr in range(0,24)]
    station_image_name = [f'images/202008_avg_{str(hr)}.png' for hr in range(0,24)]
    image_name={'area': area_image_name, 'station':station_image_name}
    return render_template("occurrence.html", hr=hr,image_name=image_name)


@app.route("/clustering/<cluster_method>/<int:cluster_num>/<int:chart_type>")
def clustering(cluster_method,cluster_num,chart_type):
    cluster_image_name={}
    for c_method in ['kmeans','ward','gmm']:
        cluster_image_name[c_method] = {}
        for c_num in range(2,5):
            cluster_image_name[c_method][c_num]={
                0: f'images/202008_{c_method}_{c_num}_cluster_feature_detail.png',
                1: f'images/202008_{c_method}_{c_num}_station_detail.png'
            }
    return render_template("clustering.html", cluster_method=cluster_method,
                           cluster_num=cluster_num, chart_type=chart_type, cluster_image_name=cluster_image_name)


if __name__ == "__main__":
    app.run(port=5001)

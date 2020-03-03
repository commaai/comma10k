#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, jsonify, send_from_directory
import glob, json, subprocess, os

app = Flask(__name__, static_url_path='')
IMAGES = sorted(glob.glob('../imgs/*.png'))
config = json.load(open('config.json','r'))

REPO_URL = 'https://github.com/commaai/comma10k/'

# print(config)

@app.route('/js/<path:path>')
def send_js(path):
  return send_from_directory('static', path)

@app.route('/imgs/<path:path>')
def send_img(path):
  return send_from_directory('../imgs', path)

@app.route('/masks/<path:path>')
def send_mask(path):
  return send_from_directory('../masks', path)

@app.route('/css/<path:path>')
def send_css(path):
  return send_from_directory('static', path)


# index
@app.route('/pencil/')
def index():
  img_id = int(request.args.get('id',0))
  if img_id<0:
    return redirect("/pencil?id=0")
  elif img_id >= len(IMAGES):
    return redirect("/pencil?id="+str(len(IMAGES)-1))
  img_name = IMAGES[img_id].split('/')[-1]
  data = {'total_images':len(IMAGES), 'img_id':img_id, 'img_name':img_name, 'config':config}
  return render_template("pencil.html", data=data)

@app.route('/hub-action/')
def hub():
  img_name = request.args.get('imgfile','')
  # print(img_name)
  if img_name=='':
    return jsonify({"out":"no-file","err":""})
  else:
    file_location = 'masks/'+img_name
    print(file_location, os.path.exists(file_location))
    process = subprocess.Popen(['git', 'status'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if img_name in out.decode("utf-8"):
      process = subprocess.Popen(['git', 'add', file_location], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out, err = process.communicate()
      print('\n\n',{"out":str(out.decode("utf-8")), "err": str(err.decode("utf-8") )})
          
      process = subprocess.Popen(['git', 'commit', '-m','" add mask : '+REPO_URL + 'blob/master/imgs/' + img_name+'"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out, err = process.communicate()
      print('\n\n',{"out":str(out.decode("utf-8")), "err": str(err.decode("utf-8") )})

      process = subprocess.Popen(['git', 'push'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out, err = process.communicate()
      print('\n\n',{"out":str(out.decode("utf-8")), "err": str(err.decode("utf-8") )})

      process = subprocess.Popen(['hub', 'pull-request', '-m','" add mask : '+REPO_URL + 'blob/master/imgs/' + img_name+'"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out, err = process.communicate()
      print({"out":str(out.decode("utf-8")), "err": str(err.decode("utf-8") )})
    # print({"out":str(out.decode("utf-8")), "err": str(err.decode("utf-8") )})
    return jsonify('\n\n',{"out":str(out.decode("utf-8")), "err": str(err.decode("utf-8") )})


if __name__ == "__main__":
    app.run(debug=True)

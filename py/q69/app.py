from flask import Flask, render_template, request, redirect, url_for
import logging
import pymongo

app = Flask(__name__)

def get_collection(dbname, coname, renewdb=False):
    mc = pymongo.MongoClient(host='localhost', port=27017)
    if renewdb:
        mc.drop_database(dbname)
    db = eval("mc."+dbname)
    co = eval("db."+coname)
    return mc, db, co

def create_findcondition(form):
    conlist = list()
    if "name" in form and form["name"]:
        conlist.append({"name": form["name"]})
    if "alias" in form and form["alias"]:
        conlist.append({"aliases.name": form["alias"]})
    if "area" in form and form["area"]:
        conlist.append({"area": form["area"]})
    if "tag" in form and form["tag"]:
        conlist.append({"tages.value": form["tag"]})

    argnum = len(conlist)
    if argnum > 1:
        findand = {"$and": conlist}
    elif argnum == 1:
        findand = conlist[0]
    else:
        findand = None

    return findand

@app.route('/')
@app.route('/reset')
def index():
    return render_template('index.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    app.logger.debug(request.method)
    if request.method == 'POST':
        app.logger.debug("request.form:{}".format(request.form))
        cond = create_findcondition(request.form)
        if cond:
            mc, db, co = get_collection(dbname="artist_json", coname="artist")
            artists = list()
            sdirect = pymongo.DESCENDING if request.form["sort"] == "-1" else pymongo.ASCENDING
            for artist in co.find(cond).sort("rating.count", sdirect).limit(int(request.form["limit"])):
                name = artist["name"] if "name" in artist else "---"
                alias = [a["name"] for a in artist["aliases"]] if "aliases" in artist else ["---"]
                area = artist["area"] if "area" in artist else "---"
                tag = [a["value"] for a in artist["tags"]] if "tags" in artist else ["---"]
                rating = artist["rating"]["count"] if "rating" in artist else "00"
                artists.append([rating, name, alias, area, tag])

            return render_template('index.html', artists=artists)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    app.run()

from os import read
from flask import Flask, render_template, request, flash, redirect, url_for
from read_dump import dump_json, read_json

app = Flask(__name__)
app.secret_key = "hello"


class shots():

    @classmethod
    def read_data(cls,path):
        cls.path = path
        cls.data = read_json(path)
        return cls.data

    @classmethod
    def new_data(cls,at, new_object):
        length = len(cls.data[at])
        if length <= 0:
            last_obj = 0
        else:
        # get last object id
            last_obj = cls.data[at][length-1]['id']
        # add id
        new_object['id'] = last_obj + 1

        cls.data[at].append(new_object)
        # dump json
        dump_json(cls.path, cls.data)
        return cls.data

    @classmethod
    def get_by_id(cls,at, id):
        for obj in (cls.data[at]):
            if obj['id'] == id:
                return(obj)
            else:
                pass
        
    @classmethod
    def delete_by_id(cls,at,id):
        for i , obj in enumerate(cls.data[at]):
            if obj['id'] == id:
                del cls.data[at][i]
            dump_json(cls.path, cls.data)
      

    @classmethod
    def update_by_id(cls,at,id, new_data):
        for i, obj in enumerate(cls.data[at]):
            if obj['id'] == id:
                cls.data[at][i]['name'] = new_data['name']
                cls.data[at][i]['content'] = new_data['content']
                dump_json(cls.path, cls.data)
            else:
                pass


path = './data.json'
# shots.new_data('shows','hello')

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        data = shots.read_data(path)
        form_data = request.form
        shot_name = form_data['shotname']
        shot_content = form_data['shotcontent']
        insert = form_data['insert']
        where = form_data['where']
        try:
            if form_data['shot']:
                shot = form_data['shot']
        except:
            pass

        new_object = {"name":shot_name,"content":shot_content}
        # add new data
        shots.new_data('shows',new_object=new_object)
        return redirect('/')
    else:
        data = shots.read_data(path)
        return render_template('index.html', data = data)

@app.route("/shot/<int:id>")
def shot(id):
    data = shots.read_data(path) 
    shot = shots.get_by_id(at='shows',id=id)
    return render_template('shot.html', data=shot)



@app.route('/delete/<int:id>')
def delete(id):
    data = shots.read_data(path) 
    del_data = shots.delete_by_id(at="shows",id=id)
    return redirect('/')


@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    data = shots.read_data(path) 
    shot = shots.get_by_id(at='shows',id=id)
    if request.method == "POST":
        form_data = request.form
        new_data = {"name": form_data['shotname'],"content":form_data['shotcontent'] }
        shots.update_by_id('shows',id,new_data)
        return redirect(url_for("shot",id=id))
    else:
        print(shot['name'])
        return render_template('update.html', data=shot)

if __name__ == "__main__":
    app.run(debug=True)
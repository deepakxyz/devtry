from read_dump import read_json, dump_json
class shots():

    @classmethod
    def read_data(cls,path):
        cls.path = path
        cls.data = read_json(path)
        return cls.data

    @classmethod
    def new_data(cls,at, new_object):
        length = len(cls.data[at])
        # add id
        new_object['id'] = length

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
                print( cls.data[at][i])

    @classmethod
    def update_by_id(cls,at,id, new_data):
        for i, obj in enumerate(cls.data[at]):
            if obj['id'] == id:
                obj[i] = new_data
                dump_json(cls.path, cls.data)
            else:
                pass


path = './data.json'
data = shots.read_data(path)
id = 122
obj = shots.get_by_id('shows', id)
print(obj)
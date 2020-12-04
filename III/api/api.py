from flask import Flask,request,jsonify

import redis
from flask import Flask,request,jsonify

app = Flask(__name__)
r = redis.StrictRedis(host='3.25.174.197', port=6379, db=0)
KEY = 'compl'
'''
FORMAT:
localhost:5000/add?name=<name>
''' 

@app.route('/add')
def add_to_dict():
    try:
        name = request.args.get('name')
        print("value of name"+name)
        line = name.strip()
        for end_index in range(1, len(line)):
            prefix = line[0:end_index] 
            print("Prefix values :"+prefix)
            r.zadd(KEY,{prefix:0})
        r.zadd(KEY,{line+'*':0})
        return "Addition Successful"
    except:
        return "Addition failed"

'''
FORMAT:
localhost:5000/suggestions?prefix=<prefix_you want to match>
'''

@app.route('/suggestions')
def get_suggestions():
    prefix = request.args.get('prefix')
    results = []
    rangelen = 50
    count=50
    print("value of KEY: "+KEY)
    print("value of prefix: "+prefix)
    start = r.zrank(KEY, prefix)
    print(start)
    print ("Inside the function")
    if not start:
        return []
    while len(results) != count:
        print ("Inside the while")
        range = r.zrange(KEY, start, start + rangelen - 1)
        print('Range')
        print(range)
        start += rangelen
        if not range or len(range) == 0:
            break
        for entry in range:
            print('Inside For Loop')
            entry=entry.decode('utf-8')
            print(entry)
            len_entry = len(entry)
            len_prefix = len(prefix)
            minlen = min((len(entry), len(prefix)))
            print(minlen)
            if entry[0:minlen] != prefix[0:minlen]:
                count = len(results)
                break
            if entry[-1] == '*' and len(results) != count:
                results.append(entry[0:-1])
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)

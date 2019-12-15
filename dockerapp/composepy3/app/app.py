# Commented code used in first build
from flask import Flask, request, render_template
import redis

app = Flask(__name__)
default_key = '1'
# cache = {default_key: 'one'}
cache = redis.StrictRedis(host='redis', port=6379, db=0)
cache.set(default_key,"one")

@app.route('/', methods=['GET', 'POST'])
def mainpage():

	key = default_key
	if 'key' in request.form:
	    key = request.form['key']

	if request.method == 'POST' and request.form['submit'] == 'save':
		# cache[key] = request.form['cache_value']
		cache.set(key, request.form['cache_value'])

	cache_value = None;
	# if key in cache:
		# cache_value = cache[key]
	if cache.get(key):
		cache_value = cache.get(key).decode('utf-8')

	return render_template('index.html', key=key, cache_value=cache_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

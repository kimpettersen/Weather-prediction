from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from models import Images

@view_config(route_name='home', renderer='templates/mytemplate.pt')#renderer='json')#renderer='templates/mytemplate.pt')
def show_img(request):
	res = request.db.paths.find_one({ 'label' : '' })
	return { 'image' : res }
	
@view_config(route_name='add_label', renderer='json')
def save_label(request):
	print request.method
	if request.method == 'POST':
		try:
			label = request.params['label']
			path = request.params['path']
			try:
				query = request.db.paths.find_one({ 'path' : path })
				query['label'] = label
				request.db.paths.save(query)
				return HTTPFound(location='/')
			except:
				#db unavailable
				return { 'error' : 'Database not available' }
		except:
			#Post data not valid
			return HTTPFound(location='/')			
	return HTTPFound(location='/')
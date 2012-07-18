from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from models import Images

@view_config(route_name='home', renderer='templates/mytemplate.pt')#renderer='json')#renderer='templates/mytemplate.pt')
def show_img(request):
	res = request.db.paths.find_one({ 'label' : '' })
	return { 'image' : res }
	
@view_config(route_name='add_label', renderer='json')
def save_label(request):
	label = request.params['label']
	path = request.params['path']
	query = request.db.paths.find_one({ 'path' : path })
	query['label'] = label
	request.db.paths.save(query)
	return HTTPFound(location='/')
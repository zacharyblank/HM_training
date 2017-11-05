import json
import os

classes = [];

def convert(a):
	width = float(a['image_w_h'][0])
	height = float(a['image_w_h'][1])

	result = ''

	for object in a['objects']:
		# Build classes
		print object['label']
		
		if object['label'] not in classes
			classes.append(object['label'])

	   x = object['x_y_w_h'][0]
	   y = object['x_y_w_h'][1]
	   w = object['x_y_w_h'][2]
	   h = object['x_y_w_h'][3]

	   x_ratio = x / width
	   y_ratio = y / height
	   w_ratio = w / width
	   h_ratio = h / height

	   class_number = classes.index("label")

	   list = map(str,[class_number, x_ratio, y_ratio, w_ratio, h_ratio])

	   result = result + ' '.join(list) + '\n'

	return result



# with open('data.json') as data_file:    
#     data = json.load(data_file)


for root, dirs, filenames in os.walk('./data'):
    for f in filenames:
    	readpath = os.path.join(root, f)
    	if os.path.basename(readpath).split('.')[1] == 'json':
	    	writepath = readpath.replace('json', 'txt')
	        with open(readpath,'r') as json_file:    
	    		data = json.load(json_file)
	    		# print f
	    		# print convert(data)
	    		txt_file = open(writepath,'w')

	    		txt_file.write(convert(data))



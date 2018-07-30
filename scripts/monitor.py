# Uploads datast anytime a dataset is added nfs mounted directory
import inotify.adapters
import package as pc
import os

def _main():
    i = inotify.adapters.Inotify()

    i.add_watch('/data')

    data = [] * 2 # dataset and metadata

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event

	print(event)
        if 'IN_MODIFY' in event[1]:
            location = path + "/" + filename
	    data.append(location)

	if len(data) == 2:
            print('creating resource')
            pc.main(data)
	    for d in data:
	        os.remove(d)
            data[:] = []

if __name__ == '__main__':
    _main()

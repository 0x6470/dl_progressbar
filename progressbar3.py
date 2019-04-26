#Python 3 version, tested with Python 3.7.0
import time
import urllib.request, urllib.error, urllib.parse

def download(url):
	start = time.time()

	file_name = url.split('/')[-1]
	u = urllib.request.urlopen(url)
	file = open(file_name, 'wb')
	file_size = int(u.info().get_all("Content-Length")[0])
	print("Downloading: {} Bytes: {}".format(file_name, file_size))

	file_size_dl = 0
	block_size = 8192
	loading_bar = "  [-------------------]"
	while True:
		buffer = u.read(block_size)
		#progress = float("{0:3.0f}".format(file_size_dl * 100. / file_size)) # actually more accurate, because the value is rounded and not cut off
		progress = float(int(file_size_dl * 100. / file_size)) # progress bar here updates at multiple of 5  e.g. 5, 10, 15... (nicer to look at)
		if not buffer:
			break

		file_size_dl += len(buffer)
		file.write(buffer)
		if progress % 5 == 0.0 and progress != 0.0:
			#loading_bar = loading_bar.replace("-", "=", 1) #didn't work
			loading_bar = loading_bar[:(int(progress/5+3))].replace('-', '>') + loading_bar[(int(progress/5+3)):]
			if int(progress)/5 > 1:
				loading_bar = loading_bar[:(int(progress/5+2))].replace('>', '=') + loading_bar[(int(progress/5+2)):]
		status = r"{0:10d}  [{1:3.2f}%]".format(file_size_dl, file_size_dl * 100. / file_size) + loading_bar
		status = status + chr(8)*(len(status)+1)
		print(status, end=' ')
	print("\nCompleted in {0:3.2f}s ({1:3.3f} KiB/s)".format(time.time()-start, (file_size/1024)/(time.time()-start)))
	file.close()

download("https://github.com/jamesward/play-load-tests/raw/master/public/10mb.txt") # example file

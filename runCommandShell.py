import os, sys, subprocess, re

num_args = len(sys.argv)

if num_args <= 2:
    print("Info comando: ", os.path.basename(sys.argv[0]), " path_log_sh pattern " )
else:
	
	
	while True:
		scriptSh = "tail -1 "+sys.argv[1]+" | grep .*"+sys.argv[2]+".*"
		process = subprocess.Popen([scriptSh],  stderr=subprocess.PIPE, shell=True)
		#process.wait()
		
		line = process.stderr.readline()
		if line.decode("utf-8") != "":
			process.kill()
			exit(0)

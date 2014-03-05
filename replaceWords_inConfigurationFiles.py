
#Script: replace all keys of the dictionary found in input file with the respective values of the dictionary

import re
import os, sys

num_args = len(sys.argv)

def sostituisciConfigDatas(text, my_configuration_dict):
    rc = re.compile('|'.join(map(re.escape, my_configuration_dict)))
    def translate(match):
        return my_configuration_dict[match.group(0)]
    return rc.sub(translate, text)
	
if num_args <= 10:
    print("Info comando: ", os.path.basename(sys.argv[0]), " input_file host_name host_ip host_port db_ip db_port db_sid db_schema db_jdbc_user db_jdbc_password" )
else:
	input_file = sys.argv[1]

	# leggo il file
	fin = open(input_file, "r")
	str_input_file = fin.read()
	fin.close()
	 
	# dizionario coppia before_word:after_word
	my_configuration_dict = {
	'host_name': sys.argv[2],
	'host_ip': sys.argv[3],
	'host_port': sys.argv[4],
	'db_ip': sys.argv[5],
	'db_port': sys.argv[6],
	'db_sid': sys.argv[7],
	'db_schema': sys.argv[8],
	'db_jdbc_user': sys.argv[9],
	'db_jdbc_password': sys.argv[10]}
	 
	# cambio il testo
	str_output_file = sostituisciConfigDatas(str_input_file, my_configuration_dict)
	#print(str_output_file)
	 
	# sovrascrivo input file
	fout = open(input_file, "w")
	fout.write(str_output_file)
	fout.close()


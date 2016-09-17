import subprocess

def compileandrun(solution, language, problem_id):
	problem_name = 
	file_name = "/home/prat33k/falcon/Allsubmissions" + solution
	command = ''

	error_file =  "~/falcon/Output/" + "error.log"
	output_file =  "~/falcon/Output/" + "out.txt"

	if language == 'C':
		command = ['/usr/bin/gcc' , '-lm', '-w', file_name]
	elif language == 'C++':
		command = ['/usr/bin/gcc' , '-lm', '-w', file_name]
	else:
		pass

	copyfile(current_state, start_state)

	ferr = open(error_file,'w')

	subprocess.call(command, stderr=ferr)

	 with open(error_file, 'r') as err_file:
            error = err_file.read()
     if not error:
     	command_for_checker = ''
     	command_for_checker = ['./runner', '--input=' + current_state, ' --output=' + output_file , 'a.out']
     	ferr = open(error_file,'w')
     	subprocess.call(command_for_checker, stderr=ferr) 
     	 with open(error_file, 'r') as err_file:
            error = err_file.read()
        if not error:
        	appendfile(current_state, output_file)

        	subprocess.call()

def copyfile(file1, file2):

	with open(file2) as f:
		with open(file1, "w") as f1:
    		for line in f:
        		if "ROW" in line:
            		f1.write(line) 

def appendfile(file1,file2):
	
	with open(file2) as f:
		with open(file1,"a") as f1:
			for line in f:
				if "ROW" in line:
					f1.write("\n" + line)










import os
import re
import sys
import time
from glob import glob
import subprocess

def find_batches(globbed):
	# this sorts the scripts into batches
	# that have identical sbatch options
	# this allows us to submit everything
	# we find in the fewest job arrays possible
	batches = {}
	for script_file in globbed:
		with open(script_file, 'rt') as in_file:
			script = in_file.readlines()
		
		options = [
			line for line in script 
			if line.startswith('#SBATCH') 
			and not '--job-name' in line 
			and not '--output' in line
		]
		
		script_option_keys = [re.sub('.*--(.*?)=.*\n', '\\1', option) for option in options]
		script_option_values = [re.sub('.*--.*=(.*)\n', '\\1', option) for option in options]
		script_options = tuple(zip(script_option_keys, script_option_values))
		
		if not script_options in batches.keys():
			batches[script_options] = [script_file]
		else:
			batches[script_options].append(script_file)
	
	return batches

def submit_batched_jobs(name, args, batches, log_dir = 'joblogs'):
	print('Submitting jobs in ' + str(len(batches)) + ' array(s).')
	for i, (options, files) in enumerate(batches.items()):
		if len(files) == 1:
			x = subprocess.Popen(['sbatch', *args, files[0]])
			time.sleep(1)
			x.kill()
			continue
	
		joblist = []
		for script in files:
			with open(script, 'rt') as in_file: 
				script = in_file.readlines()
			
			script = [line.replace('\n', '') for line in script if not line.startswith('#') and not line == '\n']
			script = '; '.join(script)
			script = script.replace('\t', '').replace('\\; ', '') + '\n'
			joblist.append(script)
		
		# find the deepest common directory among the scripts
		dirname = set(os.path.dirname(script) for script in files)
		while len(dirname) > 1:
			dirname = set(os.path.dirname(d) for d in dirname)
		
		dirname = next(iter(dirname))
		
		joblist = ''.join(joblist)
		
		if len(batches) > 1:
			formatter = 'i:0' + str(len(str(len(batches)))) + 'd'
			formatter = '_{{{s:s}}}'.format(s=formatter)
			formatter = formatter.format(i=i)
		else:
			formatter = ''
		
		joblist_file = os.path.join(dirname, name + formatter + '.txt')
		
		with open(joblist_file, 'wt') as out_file:
			out_file.write(joblist)
			
		k_options = ['--' + k for k, _ in options]
		v_options = [v for _, v in options]
		options = list(zip(k_options, v_options))
		options = [v for t in options for v in t]
		
		x = subprocess.Popen([
			'dsq', 
			'--job-file', joblist_file, 
			'--status-dir', log_dir + os.path.sep,
			'--job-name', name + formatter,
			'--output', os.path.join(log_dir, name + formatter + '-%A_%a.txt'),
			'--batch-file', os.path.join(dirname, name + formatter + '.sh'),
			*options, 
			*args
		], stdout=subprocess.DEVNULL)
		while x.poll() is None:
			time.sleep(0.5)
		
		x.kill()
		
		x = subprocess.Popen([
			'sbatch',
			*args,
			os.path.join(dirname, name + formatter + '.sh')
		])
		while x.poll() is None:
			time.sleep(0.5)
		
		x.kill()
		
		# os.remove(joblist_file)
		os.remove(os.path.join(dirname, name + formatter + '.sh'))

def sbatch_all(s):
	'''
	Submit all scripts matching glob expressions as sbatch jobs
	s consists of command line args except for 'sball'
	the final argument should be the glob pattern,
	any additional preceding arguments are passed to sbatch.
	'''
	try:
		scripts = s[-1].split()
	except IndexError:
		raise IndexError('You need to provide some scripts!')
	
	args = [arg for arg in s[:-1] if not arg.startswith('name=') and not arg.startswith('regex=')]
	name = [arg.split('=')[1] for arg in s[:-1] if arg.startswith('name=')]
	name = name[0] if name else []
	
	regex = [arg.split('=')[1] for arg in s[:-1] if arg.startswith('regex=')]
	regex = regex[0] if regex else []
	
	log_dir = [arg.split('=')[1] for arg in s[:-1] if arg.startswith('log_dir=')]
	log_dir = log_dir[0] if log_dir else 'joblogs'
	
	globbed = []
	for script in scripts:
		globbed.append(glob(script, recursive=True))
	
	globbed = [script for l in globbed for script in l if script.endswith('.sh')]
	
	if regex:
		globbed = [script for script in globbed if re.match(regex, script)]
	
	if len(globbed) == 0:
		print('No scripts matching expression "' + s[-1] + '" found.')
		sys.exit(0)
	
	globbed = sorted(globbed)
	batches = find_batches(globbed)
	
	try:
		submit_batched_jobs(name=name, args=args, batches=batches, log_dir=log_dir)
	except KeyboardInterrupt:
		print('User terminated.')
		sys.exit(0)
	except Exception:
		print('Error submitting jobs using dSQ (did you `module load dSQ` first?).')
		response = input('Submit individually (y/n)? ')
		while response not in {'y', 'n'}:
			response = input('Invalid option. Please enter one of "y", "n": ')	
		
		if response == 'y':
			for script in globbed:
				x = subprocess.Popen(['sbatch', *args, script])
				time.sleep(1)
				x.kill()
		elif response == 'n':
			pass

if __name__ == '__main__':
	args = [arg for arg in sys.argv[1:] if not arg == 'sball.py']
	sbatch_all(args)

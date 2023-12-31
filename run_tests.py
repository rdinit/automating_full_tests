import subprocess
import os

def run_in_directory(start_dir):
    start_dir += '/bin'
    texts = []
    for file in os.listdir(start_dir):
        texts.append('\nTESTS from: ' + file)
        texts.append(subprocess.Popen([start_dir + '/' + file], stdout=subprocess.PIPE).communicate()[0].decode("utf-8") )
    return texts.copy()


res = []
res += run_in_directory('complex_tests')
res += run_in_directory('rational_tests')
res += run_in_directory('dynarr_tests')

with open('test_output.txt', 'w') as f:
    f.write('\n'.join(res))
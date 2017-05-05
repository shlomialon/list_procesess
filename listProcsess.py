 #!/usr/bin/env python
import json
import os.path
import subprocess


class ProcessesDisplayer(object):
    all_processes_data = []
    ps_paramters = ['PID','TTY','TIME','COMMAND']
    filename = ''

    def __init__(self, filename):
        self.filename = filename
        ps_command_res = subprocess.Popen("ps -aux --sort +time", shell=True, stdout=subprocess.PIPE)
        all_ps_string = ps_command_res.stdout.read()
        ps_command_res.stdout.close()
        ps_command_res.wait()
        lines = all_ps_string.split('\n')[1:]
        for line in lines:
            process = [x for x in line.split(' ') if x != '']
            process_dict = dict(zip(self.ps_paramters,process))
            self.all_processes_data.append(process_dict)
        
    # def compare_two_time(self,string1,string2):
    #     for i in string1:
    #         if(i == ':'):
    #             if(int(string1[i-2:i]) > int(string2[i-2:i])):
    #                 return string1
    #             if(int(string1[i-2:i]) < int(string2[i-2:i])):
    #                 return string2
    #     return string1    
                    
    # def find_sub_string(self,word, string_word):
    #     len_word = len(word)
    #     for i in range(len(string_word)-1):
    #         if string_word[i: i + len_word] == word:
    #             return True
    #         else:
    #             return False          
                
                
 # ----- Saves to json file ------# 
    def save_to_json_file(self):
        with open(self.filename, 'w') as outstream:
            json.dump(self.all_processes_data, outstream)

# ----- Reads from json file -----#
    def read_json_file(self):
        if os.path.isfile(self.filename):
            with open(self.filename) as file_data:
                data = json.load(file_data)
                print data

def main():
    processDisplayer = ProcessesDisplayer("psdata.json")
    processDisplayer.save_to_json_file()
    processDisplayer.read_json_file()
main()

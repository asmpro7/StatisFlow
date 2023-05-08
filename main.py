# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher,FlowLauncherAPI
import statistics
import subprocess

def copy2clip(txt):
    cmd = 'echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

class statis(FlowLauncher):

    def query(self, query):
        results = []
        try:
             
            if len(query.strip()) == 0:
                    results.append({
                        "Title": "Enter the value",
                        "SubTitle": " separated them by commas",
                        "IcoPath": "Images/app.png"})
            else:
                value = []
                index = []
                listQ=query.split(",")
                for num in listQ:
                    value.append(int(num))

                for num in sorted(value):
                    index.append(str(num))
                sortT="Sorted numbers: " + ",".join(index)
                sortV=",".join(index)
                results.append({
                    "Title": sortT,
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {"method": "copy", "parameters": [sortV], }})
                nT="n: " + str(len(value))
                nV= str(len(value))
                results.append({
                    "Title": nT,
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {"method": "copy", "parameters": [nV], }})
                meanT="Mean: " + str(statistics.mean(value))
                meanV=str(statistics.mean(value))
                results.append({
                    "Title": meanT,
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {"method": "copy", "parameters": [meanV], }})
                medianV = statistics.median(value)
                medianT = f"Median(Q2): {str(medianV)}"
                results.append({
                    "Title": medianT,
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {"method": "copy", "parameters": [str(medianV)], }})
                modeT="Mode: "+ str(statistics.mode(value))
                modeV=str(statistics.mode(value))
                results.append({
                    "Title": modeT,
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {"method": "copy", "parameters": [modeV], }})
                minT="Minimum: "+ str(index[0])
                minV= str(index[0])
                results.append({
                    "Title": minT,
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {"method": "copy", "parameters": [minV], }})
                maxT="Maximum: "+ str(index[-1])
                maxV= str(index[-1])
                results.append({
                    "Title": maxT,
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {"method": "copy", "parameters": [maxV], }})
                rangeT="Range: "+ str(int(index[-1])-int(index[0]))
                rangeV=str(int(index[-1])-int(index[0]))
                results.append({
                    "Title": rangeT,
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {"method": "copy", "parameters": [rangeV], }})

                Q1_list = []
                Q3_list = []
                for number in value:
                    if number < medianV:
                        Q1_list.append(number)
                    elif number > medianV:
                        Q3_list.append(number)

                q1V = str(statistics.median(Q1_list))
                q1T= "Q1: "+ q1V
                results.append({
                    "Title": q1T,
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {"method": "copy", "parameters": [q1V], }})

                q3V= str(statistics.median(Q3_list))
                q3T="Q3: "+ q3V
                results.append({
                    "Title": q3T,
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {"method": "copy", "parameters": [q3V], }})
                IqRT="IQR: "+ str(float(q3V)-float(q1V))
                IqRV=str(float(q3V)-float(q1V))
                results.append({
                    "Title": IqRT,
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {"method": "copy", "parameters": [IqRV], }})
                varianceT="Variance: "+ str(statistics.pvariance(value))
                varianceV=str(statistics.pvariance(value))
                results.append({
                    "Title": varianceT,
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {"method": "copy", "parameters": [varianceV], }})
                SdT="Standard deviation: "+ str(statistics.pstdev(value))
                SdV=str(statistics.pstdev(value))             
                results.append({
                    "Title": SdT,
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {"method": "copy", "parameters": [SdV], }})
                 
        except:
             results.append({
                "Title": "Invalid Notation",
                "SubTitle": "Please, Verify and try again",
                "IcoPath": "Images/app.png"})
        
        return results

    def copy(self, ans):
        FlowLauncherAPI.show_msg("Copied to clipboard", copy2clip(ans))

    

if __name__ == "__main__":
    statis()

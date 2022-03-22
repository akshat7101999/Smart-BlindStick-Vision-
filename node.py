import cv2
import requests
import speech_recognition as SRG 
import time
import pyttsx3
import json
import base64

url = 'http://localhost:5000/predict_api'
store = SRG.Recognizer()


def text2audio(text):
    
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def askQuestion():
    
    with SRG.Microphone() as s:
     
        print("Speak...")

        audio_input = store.record(s, duration=5)
        print("Recording time:",time.strftime("%I:%M:%S"))

        try:
            text_output = store.recognize_google(audio_input)
            print("Text converted from audio:\n")
            print(text_output)
            return text_output
            print("Finished!!")

            print("Execution time:",time.strftime("%I:%M:%S"))
        except:
               return "Could not get what you said"

def main():
    #cam = cv2.VideoCapture(0)
    while(True):
        print("Please select 1 if you want to click the picture")
        text2audio("Select 1 to click")
        
        option = input()
        if(str(option) == "1"):
            #ret, frame = cam.read()
            frame = cv2.imread('/Users/akshatsharma/Desktop/a.jpeg')
            string = base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode()
            frame = string
            '''
            send frame to server CLIP, async and wait
            inference = received
            
            '''
            #text2audio(inference)
            while(True):
                print("Please select 1 if you want to use VQA for the picture")
                text2audio("Please select 1 if you want to use VQA for the picture")
                boolVQA = input()
                if(str(boolVQA) == "1"):
                    ques = askQuestion()
                    r = requests.post(url,json={'url':frame, 'ques':ques + "?"})
                    print(r.json())
                    '''
                    send frame along with the question to server ViLT, async and wait
                    inferenceVQA = receivedVQA

                    ''' 
                    text2audio(r.json())

                else:
                    print("No question, moving ahead")
                    text2audio("No question, moving ahead")
                    break
                
        else:
            print("thanks for using !")
            text2audio("thanks for using !")
            break
main()
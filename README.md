# Smart-BlindStick-Vision-

The motivation behind this project is to help visually impaired person to percept their surroundings better. The person will use a blindstick equipped with a camera, a mic and a speaker which will be acting as a node. Whenever the person wants to percept their surrounding they will press a button and the camera will capture a picture. This captured image is sent to a remote server where the inference will be generated using CLIP model which is an image captioning model and will be sent back to the person. The inference will be spoken out and he/she can hear it to better understand its surroundings. Later on he/she can ask some questions related to the things that have been heard and again that speech will be converted to text and sent to server. The server will answer the questions using the ViLT model which is a Visual Question Answering (VQA) model and result will be sent back to the node. Text to Audio module will read it out for the visually impaired.


**Create a conda environment with python version 3.8 with -----  conda create -n "myenv" python=3.8**

1) For completing the dependencies of server.py, following needs to be installed :  
   - pip install -q git+https://github.com/huggingface/transformers.git
   - opencv
   - Flask
   - torch (gets installed with the first command but if it is not installed, install separately)
2) For completing the dependencies of node.py, following needs to be installed : 
   - speech_recognition (will require to install pyaudio)
   - pyttsx3
 3) Once everything is in place run server.py
 4) Then run node.py on other terminal or on different laptop over same LAN. 
 
 NOTE : Ngrok can be used for giving public public access over the internet.
 

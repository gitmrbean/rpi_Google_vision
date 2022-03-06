./gspch.sh Welcome to GCP based Image detection
rm out.jpg
rm cam.jpg
./gspch.sh Please show the object to be identified in front of camera
sudo fswebcam cam.jpg
#./gspch.sh Image captured.
#./gspch.sh Loading Captured image in window for you
gpicview& cam.jpg
./gspch.sh Processing identification of the object . Please wait 
python imgan_TVM.py cam.jpg
sudo chmod 777 cam.jpg
kill $(ps aux | grep gpicview)

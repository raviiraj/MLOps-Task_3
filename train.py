actual_accuracy=$(sudo cat /root/MLOps-Task_3/accuracy.txt)
target_accuracy=94

if
sudo [ $actual accuracy -gt $target_accuracy ]

then

sudo sed -i '26i model.add (Dense unit=60 , input_dim = 28*28 activation='relu' ))' /root/MLOps-Task_3/train.py

fi
if [ sudo git diff train.py ]
then
sudo git add --all
sudo git commit -m ""
else
sudo python3 /root/MLOps-Task_3/notify_success.py
fi
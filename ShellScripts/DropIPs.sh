BLOCKDB=$1
IPS=$(grep -Ev "^#" $BLOCKDB)
for i in $IPS
do
echo "Access Denied:"$i
iptables -A INPUT -s $i -j DROP
done

#for redhat or centos
#service iptables save

sleep $2m

for j in $IPS
do
echo "Access Allowed:"$j 
iptables -D INPUT -s $j -j DROP
done

#for redhat or centos
#service iptables save

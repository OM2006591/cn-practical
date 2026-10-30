#include <bits/stdc++.h>
using namespace std;

int main(){
    int prefix = 24;
    int subnets = 2;

    int bits = log2(subnets);
    int newPrefix = prefix + bits;

    int hostBits = 32 - newPrefix;

    int hosts = pow(2, hostBits) - 2;

    int blockSize = pow(2, hostBits);

    cout << "New Prefix: /" << newPrefix << endl;
    cout << "Subnet Mask: 255.255.255.128" << endl;
    cout << "Usable Hosts per Subnet: " << hosts << endl;

    for(int i = 0; i < subnets; i++)
    {
        int network = i * blockSize;
        int broadcast = network + blockSize - 1;

        cout << "\nSubnet " << i + 1 << endl;
        cout << "Network Address: 192.168.1." << network << endl;
        cout << "Broadcast Address: 192.168.1." << broadcast << endl;
        cout << "First Usable IP: 192.168.1." << network + 1 << endl;
        cout << "Last Usable IP: 192.168.1." << broadcast - 1 << endl;
    }

    return 0;
}

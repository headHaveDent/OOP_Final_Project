#Module of List of Problems

class ProblemList:
    def __init__(self):
        self._problem_list = []

    def addProblem(self, problem_name, problem_description, problem_Cause, problem_solution):
        member = ProblemType(problem_name, problem_description, problem_Cause, problem_solution)
        self._problem_list.append(member)

    def getProblemList(self):
        return tuple(self._problem_list)



class ProblemType:
    def __init__(self, problem_name, problem_description ,problem_Cause, problem_solution):
        self._problem_name = problem_name
        self._problem_description = problem_description
        self._problem_Cause = problem_Cause
        self._problem_solution = problem_solution

    def getProblemName(self):
        return self._problem_name
    def getProblemDescription(self):
        return self._problem_description
    def getProblemCause(self):
        return self._problem_Cause
    def getProblemSolution(self):
        return self._problem_solution


#init problem
PROBLIST = ProblemList()


#Encoding Problems
PROBLIST.addProblem('Wi-Fi Authentication Error / "Incorrect Password" Loop'
,'''Your device repeatedly prompts for the Wi-Fi password or says "Authentication Error" / "Can't connect to network," even though you know the password is correct'''
,'''*Router security protocol mismatch (e.g., the router is set to WPA3 or WPA2-AES, but an older client device only supports WPA-TKIP or WEP)”.\n*Corrupted saved wireless profile on your computer containing an old password hash.\n*MAC address filtering enabled on the router blocking your device.'''
,'''*Forget the Network: Delete/forget the wireless profile completely from your computer and reconnect fresh.\n*Adjust Router Security: Log into your router admin panel and change the security mode to WPA2-PSK (AES) or WPA2/WPA3 Mixed Mode for maximum compatibility with older hardware.\n*Disable MAC Filtering: Ensure MAC address filtering is turned off or your device's physical MAC address is whitelisted.''')

PROBLIST.addProblem('Captive Portal Login Page Fails to Load (Public Wi-Fi / Hotels / Airports)'
,'''You connect to a public Wi-Fi network, but the browser fails to automatically pop up the login/terms page, leaving you with no internet.'''
,'''*Your operating system's captive portal detection service is disabled or blocked.\n*Custom DNS settings (like 1.1.1.1 or 8.8.8.8) are overriding the local network's DNS resolver, blocking the redirect.'''
,'''*Disable Custom DNS Temporarily: Ensure your Wi-Fi adapter is set to Obtain DNS server address automatically.\n*Trigger the Portal Manually: Open a web browser and type a non-HTTPS web address (like [http://example.com]) or [http://captive.apple.com] (for Mac/iOS) or [http://connectivitycheck.gstatic.com] (for Android/Windows) to force the redirect page to load.'''
)

PROBLIST.addProblem('802.1X / Enterprise Authentication Failures (RADIUS Servers)'
,'''University or corporate secure Wi-Fi networks reject your login credentials.'''
,'''*Untrusted root certificate installed on the device.\n*Incorrect EAP method selected (e.g., PEAP vs. TTLS).'''
,'''*Install the institution's official security root certificate profile.\n*Manually configure the network connection properties to match IT guidelines (choose PEAP, MSCHAPv2, and validate server certificates).'''
)

PROBLIST.addProblem('APIPA / Link-Local Addressing (169.254.x.x)'
,'''Your computer shows an IP address starting with 169.254, and you have zero local network or internet access'''
,'''*Your computer's DHCP client requested an IP address from your router or DHCP server, but received no response, causing the OS to assign itself a temporary link-local fallback address (Automatic Private IP Addressing).'''
,'''*Restart your router and computer to force a fresh DHCP handshake.\n*Check if the DHCP Server service is running (on Windows, check services.msc to ensure DHCP Client is set to Automatic and running).\n*Assign a temporary Static IP address manually to test if communication with the router is possible.'''
)

PROBLIST.addProblem('Duplicate IP Address Conflict'
,'''Network connectivity drops randomly, accompanied by system notifications warning of an "IP address conflict on the network.'''
,'''Two distinct devices on the same local network have been manually assigned the exact same static IP address.'''
,'''*Configure all devices on your network to use DHCP (dynamic assignment) via the router.\n*If using static IPs for printers or servers, map them outside the router's automatic DHCP pool range.'''
)

PROBLIST.addProblem('Negotiated Link Speed Bottlenecks (10/100 Mbps instead of 1 Gbps / 2.5 Gbps)'
,'''Your wired gigabit connection is stuck maxing out at 94 Mbps, or your network card drops down to 10 Mbps.'''
,'''*Damaged or low-quality Ethernet cable (missing or broken internal wire pairs; only using 2 pairs instead of all 4 pairs for Gigabit).\n*Cheap, unmanaged fast-ethernet switches or older router ports.\n*Oxidation or bent pins inside the RJ45 port.'''
,'''*Replace the Ethernet cable with a certified Cat6 or Cat6a cable.\n*Check adapter properties in Device Manager > Advanced > Speed & Duplex, and ensure it is set to 1.0 Gbps Full Duplex (auto-negotiation) rather than being hard-locked to 100 Mbps.'''
)

PROBLIST.addProblem('Packet Loss & High Latency Due to Cable Length or Interference'
,'''High ping spikes, jitter, and packet loss during online gaming or video calls despite a wired connection.'''
,'''*Ethernet cable exceeding the maximum reliable specification length of 100 meters (328 feet) without a repeater/switch.\n*Running unshielded Ethernet cables parallel to high-voltage electrical lines or fluorescent lighting ballasts (causing electromagnetic interference).'''
,'''*Keep cable runs under 100 meters or use fiber optic converters for long distances.\n*Use Shielded Twisted Pair (STP) cables if running wires near electrical conduits.'''
)

PROBLIST.addProblem('Third-Party Antivirus / Firewall Packet Filtering Blocks'
,'''Internet works initially after booting, but completely stops working after a few minutes once third-party security software loads.'''
,'''Aggressive or corrupted third-party firewall/internet security suites (like McAfee, Norton, or Kaspersky) flagging valid network traffic as malicious or trapping network hook filters.'''
,'''*Temporarily disable the third-party firewall/antivirus shield to test.\n*Completely uninstall and reinstall the security software using the manufacturer's official cleanup utility, or rely on built-in Windows Defender.'''
)

PROBLIST.addProblem('VPN (Virtual Private Network) Tap Adapter & Routing Table Corruption'
,'''After uninstalling a VPN client, you find you can no longer access any websites, even though you are connected to Wi-Fi.'''
,'''The Cause: The VPN software left behind a corrupted virtual network adapter driver (TAP adapter) or modified system routing tables, trapping outgoing packets.'''
,'''Open Command Prompt as Administrator and reset the network stack:use either [netsh winsock reset]
 or [netsh int ip reset]\n*Go to Device Manager > Network Adapters, look for orphaned TAP or VPN virtual adapters, right-click, and choose Uninstall device.'''
)

PROBLIST.addProblem('Browser Proxy Server Misconfiguration / Malware Hijack'
,'''Specialized software or malware has forced your computer to route all web traffic through a non-existent local proxy port, breaking web browsers while apps like Discord or Steam still work.'''
,'''Malicious scripts or proxy settings altering system-wide web traffic pathways.'''
,'''*Windows: Go to Settings > Network & Internet > Proxy, and ensure "Use a proxy server" is toggled Off (unless specifically required by an enterprise network).\n*Run an adware/malware removal scan using tools like Malwarebytes.'''
)

PROBLIST.addProblem('Co-Channel and Adjacent Channel Interference (CCI)'
,'''Your Wi-Fi speeds plummet during evenings when neighbors are home, even with a strong signal indicator.'''
,'''Multiple nearby routers broadcasting on the exact same wireless channel in the 2.4 GHz spectrum (which only has 3 non-overlapping channels: 1, 6, and 11).'''
,'''*Use a Wi-Fi analyzer app on your phone to scan local airwaves.\n*Log into your router and manually select the least congested channel (typically 1, 6, or 11 for 2.4 GHz; use wider 40MHz/80MHz channels on the 5 GHz / 6 GHz bands where available).'''
)

PROBLIST.addProblem('Bufferbloat'
,'''High ping spikes and lag whenever someone else in your house uploads files, streams video, or updates a game, even on a high-speed fiber connection.'''
,'''Your router's buffer queue becomes completely overwhelmed by incoming/outgoing data packets, causing latency to skyrocket.'''
,'''Enable Quality of Service (QoS) or Smart Queue Management (SQM) inside your router's advanced settings to prioritize latency-sensitive traffic (like gaming and VoIP calls) over bulk downloads.'''
)

PROBLIST.addProblem('Carrier-Grade NAT (CGNAT) / Double NAT Conflicts'
,'''You cannot host game servers, set up port forwarding, access your home security cameras remotely, or connect via peer-to-peer (P2P) networks.'''
,'''*Your ISP has placed you behind CGNAT because IPv4 addresses are scarce, meaning your router shares a public IP with dozens of other houses.\n*You have two routers plugged into each other (e.g., an ISP modem-router combo plugged into your own personal wireless router), creating two private subnets (Double NAT).'''
,'''*Put your ISP-provided modem/router combo into Bridge Mode so your personal router handles all routing directly.\n*Contact your ISP to request a dedicated public static IP address if you require incoming port forwarding.'''
)

PROBLIST.addProblem('Line Attenuation & DSL / Cable SNR (Signal-to-Noise Ratio) Degradation'
,'''Your broadband connection constantly drops synchronization ("sync drops"), especially during bad weather or high temperatures.'''
,'''Oxidized outdoor telephone lines, damaged coaxial cable splitters, water in outside utility pedestals, or high line noise degrading the Signal-to-Noise Ratio.'''
,'''*Remove unnecessary cable television splitters from your incoming coaxial line.\n*Check all telephone/DSL filters.\n*Contact your ISP to run a line test for physical noise and signal degradation on your outside drop wire.'''
)

PROBLIST.addProblem('No Internet Access (Connected to Wi-Fi/Ethernet, but No Web Pages Load)'
,'''When your device says it is connected to your router or local network, but apps and browsers cannot reach the internet.'''
,'''*ISP Outage: Your internet service provider is experiencing an outage in your area.\n*DNS Server Failure: The Domain Name System (which translates web addresses like google.com into IP addresses) is failing to respond.\n*IP Configuration Issues: Your computer has an expired, conflicting, or static IP address that doesn't match your router's subnet.
*Expired DHCP Lease: Your router failed to renew your computer's local IP address.'''
,'''*Power Cycle Network Equipment: Unplug your modem and router, wait 30 seconds, and plug them back in (modem first, then router after 1 minute).\n*Flush DNS and Renew IP:\n   *Windows: Open Command Prompt as Administrator and run these three commands: \n   [ipconfig /flushdns], [ipconfig /release], and [ipconfig/ renew] 
   *Mac: Open Terminal and run:\n   [sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder].\n*Change DNS Servers: Switch your network adapter settings from your ISP's default DNS to a public provider like Cloudflare (1.1.1.1) or Google (8.8.8.8).\n*Check ISP Status: Connect a phone to cellular data and check your provider's status page or app for service outages.'''
)

PROBLIST.addProblem('Frequent Disconnections or Dropped Signals'
,'''Your connection works intermittently, cutting out randomly throughout the day.'''
,'''*Wi-Fi Interference: Physical walls, thick concrete, mirrors, microwaves, baby monitors, and neighboring routers operating on the same wireless channel.\n*Outdated Network Drivers: Buggy or outdated Wi-Fi/Ethernet card drivers.\n*Hardware Overheating: Routers or network switches overheating under heavy loads.\n*Power Management Settings: The operating system is putting the network adapter to sleep to save power.'''
,'''*Update Drivers: Download the latest network adapter drivers directly from your motherboard or laptop manufacturer's website.\n*Change Wi-Fi Channels: Log into your router's admin panel and switch from crowded 2.4 GHz channels (choose 1, 6, or 11) to the less congested 5 GHz or 6 GHz bands.\n*Disable Power Saving for Adapters (Windows):\n   1.Open Device Manager > Network Adapters.\n   2.Right-click your Wi-Fi/Ethernet adapter > Properties > Power Management.\n   3.Uncheck "Allow the computer to turn off this device to save power."\n*Relocate Equipment: Move your router away from dense obstructions and electronic interference sources.'''
)

PROBLIST.addProblem('Slow Internet Speeds'
,'''Websites take a long time to load, video streaming buffers constantly, or large file downloads crawl.'''
,'''*Bandwidth Saturation: Other devices on the network are downloading large files, streaming 4K video, or seeding torrents.\n*Weak Signal Strength (Wi-Fi): Distance from the router or physical obstructions reducing link speed.\n*ISP Throttling or Plan Limits: You may have exceeded a monthly data cap, or your ISP is throttling specific traffic types.\n*Background Applications: Cloud backup services (OneDrive, Google Drive), Windows updates, or malware running in the background.'''
,'''*Run a Speed Test: Test your speed via tools like Speedtest.net while connected directly to the router via Ethernet to rule out Wi-Fi bottlenecks.\n*Check Bandwidth Hogs: Review connected devices on your router's app or admin panel to see who is using the most data.\n* Connect high-demand devices (work laptops, gaming consoles, desktop PCs) directly to the router using a Cat6 (or better) Ethernet cable.\n*Run a full system antivirus scan to ensure your computer isn't part of a botnet or downloading unauthorized data.'''
)

PROBLIST.addProblem('Limited or No Local Connectivity ("Unidentified Network" / Yellow Triangle)'
,'''Your computer cannot communicate with the router at all, often displaying an "Unidentified Network" error or a yellow exclamation mark over the connection icon'''
,'''*Incorrect Static IP Settings: Your network card is configured with a manual IP address that does not match your router's gateway.\n*Faulty Ethernet Cable or Port: A damaged physical cable, bent pins in the port, or a dead switch port.\n*Network Stack Corruption: Corrupted TCP/IP stack configuration files in your operating system.\n*Third-Party Antivirus/Firewall Blocking: Aggressive security software blocking local network communication.'''
,'''*Reset TCP/IP and Winsock (Windows): Open Command Prompt as Administrator and run [netsh int ip reset] and [netsh winsock reset]\n*Verify IP Settings: Ensure your network adapter is set to "Obtain an IP address automatically" (DHCP).\n*Swap Physical Hardware: Test a different Ethernet cable and plug into a different port on the router or switch.\n*Disable Third-Party Firewalls Temporarily: Turn off third-party antivirus suites to see if they are blocking local traffic.'''
)


PROBLIST.addProblem('Bluetooth and Wi-Fi Interference (Combo Cards)'
,'''Laptops and modern motherboards often share a single physical chip for both Wi-Fi and Bluetooth, leading to connection drops on both when one is heavily utilized.'''
,'''*Shared Antenna Conflict: 2.4 GHz Wi-Fi and Bluetooth operate on the exact same frequency band and can interfere with each other.\n*Outdated Bluetooth/Wi-Fi Firmware: Driver bugs causing conflicts in how the card allocates resources.'''
,'''*Switch to 5 GHz Wi-Fi: Moving your Wi-Fi connection to the 5 GHz band completely removes 2.4 GHz interference with Bluetooth devices like mice, keyboards, or headphones.\n*Update Combo Drivers: Install the latest combined WLAN/Bluetooth driver package from the manufacturer.'''
)






'''
### TESTING AREA BEGINS ###
"""Below are test code for this python code
Runs if directly Executed
Does not run if used as module"""

def main():

    #prints the whole list of problems
    for member in PROBLIST.getProblemList():
        print(f"""
Problem:
{member.getProblemName()}

Symptoms:
{member.getProblemDescription()}

Cause:
{member.getProblemCause}

Solution:
{member.getProblemSolution()}
\n""")

def main1():
    print(PROBLIST.getProblemNameList())

if __name__ == '__main__':
    main()
### TESTING AREA END ###
'''
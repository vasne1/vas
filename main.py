
import ddos, vpnandproxi

#ver = pyfiglet.Figlet('univers')  # font='slant'
#print(ver.renderText('VASNE'))
print('Vasne')

def function():
    print(f"""1.DDOS-ATTACK
2.VPN/Proxi""")


function()
while True:
    action = int(input())

    if action == 1:
        ddos.ddos(input('which site: '), input('how many requests: '))
        function()

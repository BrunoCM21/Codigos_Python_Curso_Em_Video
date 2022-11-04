metros = float(input("Insira um valor em metros: "))

conversaocm = metros * 100
conversaomm = metros * 1000
conversaodm = metros * 10
conversaokm = metros / 1000
conversaohm = metros / 100
conversaodcm = metros / 10

print(f"De {metros:.0f}m para {conversaodm:.0f}dm, para {conversaocm:.0f}cm e para {conversaomm:.0f}mm")
print(f"De {metros:.0f}m para {conversaodcm}dcm, para {conversaohm}hm e para {conversaokm}km")

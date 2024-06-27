import os
import time
import urllib.request

print("Welcome to Multiple Software Downloader")

def user_input():
    time.sleep(1)
    global file_path
    global usr_inpt
    file_path = input("Please choose download location [Leave Blank for Default]: ")
    if file_path == "":
        file_path = "C:\\Multiple_Software_Downloader\\"
    print("1. Google Chrome")
    print("2. Mozilla Firefox")
    print("3. Microsoft Office")
    print("4. LibreOffice")
    print("5. Avast Antivirus")
    print("6. Bitdefender Antivirus")
    print("7. VLC Media Player")
    print("8. 7-Zip")
    print("9. Win-Rar")
    print("10. Exit")
    time.sleep(0.5)
    usr_inpt = input("Please choose the ones you want [Separated by commas]: ")
    time.sleep(0.5)
    
def folder_creation():
        
        os.makedirs(file_path)
        os.chdir(file_path)

def download_install():
    global choices
    if usr_inpt.strip() == "10":
        exit()
    else:
        choices = usr_inpt.split(',')
        choices = [choice.strip() for choice in choices]
        if len(choices) == 0:
            print("Please choose at least one software or exit")
            user_input()
    google_chrome = "1"
    firefox = "2"
    microsoft_office = "3"
    libreoffice = "4"
    avast = "5"
    bitdefender = "6"
    vlc = "7"
    seven_zip = "8"
    winrar = "9"

    google_chrome_present = False
    firefox_present = False
    microsoft_office_present = False
    libreoffice_present = False
    avast_present = False
    bitdefender_present = False
    vlc_present = False
    seven_zip_present = False
    winrar_present = False

    if google_chrome in choices:
        google_chrome_present = True
    elif firefox in choices:
        firefox_present = True
    elif microsoft_office in choices:
        microsoft_office_present = True
    elif libreoffice in choices:
        libreoffice_present = True
    elif avast in choices:
        avast_present = True
    elif bitdefender in choices:
        bitdefender_present = True
    elif vlc in choices:
        vlc_present = True
    elif seven_zip in choices:
        seven_zip_present = True
    elif winrar in choices:
        winrar_present = True

    google_url = "https://dl.google.com/update2/installers/ChromeSetup.exe"
    firefox_url = "https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US"
    microsoft_office_url = "https://c2rsetup.officeapps.live.com/c2r/download.aspx?ProductreleaseID=O365HomePremRetail&language=en-us&platform=def&version=O16GA&source=MktDownloadForWinPage"
    libreoffice_url = "https://ftp.gwdg.de/pub/tdf/libreoffice/stable/24.2.4/win/x86_64/LibreOffice_24.2.4_Win_x86-64.msi/"
    avast_url = "https://files.avast.com/iavs9x/avast_free_antivirus_setup_online.exe"
    bitdefender_url = "https://download.bitdefender.com/windows/installer/en-us/bitdefender_avfree.exe"
    vlc_url = "https://get.videolan.org/vlc/3.0.16/win64/vlc-3.0.16-win64.exe"
    seven_zip_url = "https://www.7-zip.org/a/7z1900-x64.exe"
    winrar_url = "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-602.exe"

    if google_chrome_present:
        urllib.request.urlretrieve(google_url, "ChromeSetup.exe")
        print("Google Chrome downloaded successfully!")
    if firefox_present:
        urllib.request.urlretrieve(firefox_url, "Firefox Installer.exe")
        print("Mozilla Firefox downloaded successfully!")
    if microsoft_office_present:
        urllib.request.urlretrieve(microsoft_office_url, "OfficeSetup.exe")
        print("Microsoft Office downloaded successfully!")
    if libreoffice_present:
        urllib.request.urlretrieve(libreoffice_url, "LibreOffice_24.2.4_Win_x86-64.msi")
        print("LibreOffice downloaded successfully!")
    if avast_present:
        urllib.request.urlretrieve(avast_url, "avast_free_antivirus_setup_online.exe")
        print("Avast Antivirus downloaded successfully!")
    if bitdefender_present:
        urllib.request.urlretrieve(bitdefender_url, "bitdefender_avfree.exe")
        print("Bitdefender Antivirus downloaded successfully!")
    if vlc_present:
        urllib.request.urlretrieve(vlc_url, "vlc-3.0.16-win64.exe")
        print("VLC Media Player downloaded successfully!")
    if seven_zip_present:
        urllib.request.urlretrieve(seven_zip_url, "7z1900-x64.exe")
        print("7-Zip downloaded successfully!")
    if winrar_present:
        urllib.request.urlretrieve(winrar_url, "winrar-x64-602.exe")
        print("Win-Rar downloaded successfully!")

    print("All file(s) downloaded successfully!")
    time.sleep(1)

    if google_chrome_present:
        os.system("ChromeSetup.exe")
    if firefox_present:
        os.system("Firefox Installer.exe")
    if microsoft_office_present:
        os.system("OfficeSetup.exe")
    if libreoffice_present:
        os.system("LibreOffice_24.2.4_Win_x86-64.msi")
    if avast_present:
        os.system("avast_free_antivirus_setup_online.exe")
    if bitdefender_present:
        os.system("bitdefender_avfree.exe")
    if vlc_present:
        os.system("vlc-3.0.16-win64.exe")
    if seven_zip_present:
        os.system("7z1900-x64.exe")
    if winrar_present:
        os.system("winrar-x64-602.exe")

    print("All file(s) instalation began successfully!")
    time.sleep(1)
def removal():
    for file in os.listdir('.'):
        if file.endswith(".exe") or file.endswith(".msi"):
            os.remove(file)

user_input()
folder_creation()
download_install()
removal()

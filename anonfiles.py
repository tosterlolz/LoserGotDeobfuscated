import xbmc, xbmcplugin, xbmcaddon, xbmcgui, base64, requests
import sys
from resources.lib.modules.params import p
from base64 import b64decode

xbmc.log(str(p.get_params()),xbmc.LOGDEBUG)

name            = p.get_name()
url             = p.get_url()
mode            = p.get_mode()
icon            = p.get_icon()
fanart          = p.get_fanart()
description     = p.get_description()
Project_key     = "NTIwNGQ3OWQyZThjZmUw"
Project_ID      = '4720061'
PIN_DATA        = xbmcaddon.Addon().getSetting('pin')
def GetWidth (OOO0O0OOO0O00OO00 ):#line:1
	import re #line:2
	OOO0O0OOO0O00OO00 =re .sub ('\[.+\]','',OOO0O0OOO0O00OO00 )#line:3
	import string #line:4
	OO0OO0O0OO000O0O0 =0 #line:5
	for O00OOOOO0OOO0OOOO in OOO0O0OOO0O00OO00 :#line:6
		if O00OOOOO0OOO0OOOO in 'lij|\' ':OO0OO0O0OO000O0O0 +=37 #line:7
		elif O00OOOOO0OOO0OOOO in '![]fI.,:;/\\t':OO0OO0O0OO000O0O0 +=50 #line:8
		elif O00OOOOO0OOO0OOOO in '`-(){}r"':OO0OO0O0OO000O0O0 +=60 #line:9
		elif O00OOOOO0OOO0OOOO in '*^zcsJkvxy':OO0OO0O0OO000O0O0 +=85 #line:10
		elif O00OOOOO0OOO0OOOO in 'aebdhnopqug#$L+<>=?_~FZT'+string .digits :OO0OO0O0OO000O0O0 +=95 #line:11
		elif O00OOOOO0OOO0OOOO in 'BSPEAKVXY&UwNRCHD':OO0OO0O0OO000O0O0 +=112 #line:12
		elif O00OOOOO0OOO0OOOO in 'QGOMm%W@':OO0OO0O0OO000O0O0 +=135 #line:13
		else :OO0OO0O0OO000O0O0 +=50 #line:14
	return int (OO0OO0O0OO000O0O0 *6.5 /100 )#line:15
def Keyboard (Heading =xbmcaddon .Addon ().getAddonInfo ('name')):#line:17
	OO0000OOO000O00O0 =xbmc .Keyboard ('',Heading )#line:18
	OO0000OOO000O00O0 .doModal ()#line:19
	if (OO0000OOO000O00O0 .isConfirmed ()):#line:20
		return OO0000OOO000O00O0 .getText ()#line:21
def Browse (OO000000OO000OO0O ):#line:23
	import webbrowser #line:25
	O0OOOO0O0O0O0OOOO =webbrowser .open #line:27
	OOO0OOOOO0OOO0OO0 =xbmc .executebuiltin #line:28
	O0O0000O0OOO000O0 =lambda OOOOO0O0O00O00000 :xbmc .getCondVisibility (str (OOOOO0O0O00O00000 ))#line:29
	O000O0O0OOOO0OO0O =lambda O00O0OOOO00OO0OOO :OOO0OOOOO0OOO0OO0 ('StartAndroidActivity(,android.intent.action.VIEW,,%s)'%(O00O0OOOO00OO0OOO ))#line:30
	OOOOOOOO00O0OOO0O ='System.Platform.Android'#line:32
	if O0O0000O0OOO000O0 (OOOOOOOO00O0OOO0O ):O000O0O0OOOO0OO0O (OO000000OO000OO0O )#line:34
	else :O0OOOO0O0O0O0OOOO (OO000000OO000OO0O )#line:35
def Check ():#line:38
		import sys #line:40
		O0O00000O0O0OO0OO =xbmcaddon .Addon ().getAddonInfo #line:44
		O0OO0O0OO0OOO0O00 =O0O00000O0O0OO0OO ('name')#line:45
		OOO00000O00O0O0O0 =('To access [COLOR white][B]UK TURK PLAYLIST[/B][/COLOR] you will need an access token. Please press continue to get an access token.')#line:46
		OOO0O0000O0OOOOO0 =OOO00000O00O0O0O0 #line:47
		OOOO00O0O00O00OO0 =("If you have already got your token please select [B][COLOR white]Enter Token[/COLOR][/B] if you do not have a token please select [B][COLOR white]Get Token[/COLOR][/B] or go to [B][COLOR white]https://bit.ly/2WahdNX[/COLOR][/B] via a external device.")#line:48
		OO00O0000OO0OO0O0 =xbmcaddon .Addon ().getSetting ('pin')#line:49
		OO0O0OO0OOO0OO00O =lambda OOO0OOO0O0O000000 :base64 .b64decode (str (OOO0OOO0O0O000000 ))#line:50
		OOO0O00O0O0OOO0OO =("https://development-tools.net/tools-api/api?pin=")+xbmcaddon .Addon ().getSetting ('pin') +('&key=')+ (Project_key )
		O00O00OOOO0000O00 =lambda O0O00OO0OO0OOO00O :requests .get (OOO0O00O0O0OOO0OO ,verify =False ).text .strip ()#line:52
		OO00OOOOOOO00000O =lambda O0000OO00O0O0O0OO :xbmcaddon .Addon ().setSetting (b64decode ("cGlu").decode ('utf-8'),O0000OO00O0O0O0OO )#line:53
		OO0O0000000OOO0O0 =lambda O0OOO0O0O0O000000 :xbmcgui .Dialog ().yesno (O0O00000O0O0OO0OO ('name'),O0OOO0O0O0O000000 ,yeslabel ="Continue",nolabel ='Cancel',)#line:54
		OO0OOO0O00O00OOOO =lambda OO0OO0OO00OO00O00 :xbmcgui .Dialog ().yesno (O0O00000O0O0OO0OO ('name'),OO0OO0OO00OO00O00 ,yeslabel ="Enter token",nolabel ='Get token',)#line:55
		O0O0OO0O000000O0O =bool (O00O00OOOO0000O00 (OO00O0000OO0OO0O0 )==("Pin Verified"))#line:56
		OO00OOOO0OO0OO00O =("https://bit.ly/2WahdNX")#line:57
		if O0O0OO0O000000O0O :return #line:59
		else :#line:60
			if OO0O0000000OOO0O0 (OOO00000O00O0O0O0 ):#line:62
				if OO0OOO0O00O00OOOO (OOOO00O0O00O00OO0 ):#line:63
					OOOO00OO00OOOO00O =Keyboard (('Type Your access token here'))#line:64
					OO00OOOOOOO00000O (OOOO00OO00OOOO00O )#line:65
					Check ()#line:66
				else :#line:67
					Browse (OO00OOOO0OO0OO00O )#line:68
					sys .exit (1 )#line:69
			else :#line:70
				sys .exit ()

Check()
if mode==None:
    from resources.lib.modules.menus import main
    Check()
    main()

elif mode==1:
	from resources.lib.modules.menus import sub_menu
	sub_menu(name,url,icon,fanart)

elif mode==2:
	from xbmcaddon import Addon
	from addonvar import addon_id
	Addon(addon_id).openSettings()

elif mode==3:
	from resources.lib.modules.player import Player
	p = Player(name, url, icon)
	p.play_link()

elif mode==4:
	from resources.lib.modules.functions import BSHOWS
	from resources.lib.modules.best_series import  new_shows
	BSHOWS(new_shows)

elif mode==5:
	from resources.lib.modules.functions import BSHOWS
	BSHOWS(url)

elif mode==6:
	from resources.lib.modules.functions import BSHOWS2
	BSHOWS2(url)

elif mode==7:
	from resources.lib.modules.functions import SHOWIMAGE
	SHOWIMAGE(url)

elif mode==8:
	from resources.lib.modules.functions import BSHOWS_SERIES
	from resources.lib.modules.best_series import  most_popular
	BSHOWS_SERIES(most_popular)

elif mode==9:
	from resources.lib.modules.functions import BSHOWS_SERIES
	BSHOWS_SERIES(url)

elif mode==10:
	from resources.lib.modules.functions import BSHOWS_EPISODES
	BSHOWS_EPISODES(url)

elif mode==11:
	from resources.lib.modules.functions import ADDTOFAVS
	ADDTOFAVS(name, url, icon)

elif mode==12:
	from resources.lib.modules.functions import REMFAVS
	REMFAVS(name)

elif mode==13:
	from resources.lib.modules.functions import GETFAVS
	GETFAVS()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
import xbmc, xbmcplugin, xbmcaddon, xbmcgui, base64, requests
import sys
from resources.lib.modules.params import p
from base64 import b64decode

xbmc.log(str(p.get_params()),xbmc.LOGDEBUG)

name            = p.get_name()
url             = p.get_url()
mode            = p.get_mode()
icon            = p.get_icon()
fanart          = p.get_fanart()
description     = p.get_description()
Project_key     = "NTIwNGQ3OWQyZThjZmUw"
Project_ID      = '4720061'
PIN_DATA        = xbmcaddon.Addon().getSetting('pin')

def GetWidth (OOO0O0OOO0O00OO00 ):#line:1
	import re #line:2
	OOO0O0OOO0O00OO00 =re .sub ('\[.+\]','',OOO0O0OOO0O00OO00 )#line:3
	import string #line:4
	OO0OO0O0OO000O0O0 =0 #line:5
	for O00OOOOO0OOO0OOOO in OOO0O0OOO0O00OO00 :#line:6
		if O00OOOOO0OOO0OOOO in 'lij|\' ':OO0OO0O0OO000O0O0 +=37 #line:7
		elif O00OOOOO0OOO0OOOO in '![]fI.,:;/\\t':OO0OO0O0OO000O0O0 +=50 #line:8
		elif O00OOOOO0OOO0OOOO in '`-(){}r"':OO0OO0O0OO000O0O0 +=60 #line:9
		elif O00OOOOO0OOO0OOOO in '*^zcsJkvxy':OO0OO0O0OO000O0O0 +=85 #line:10
		elif O00OOOOO0OOO0OOOO in 'aebdhnopqug#$L+<>=?_~FZT'+string .digits :OO0OO0O0OO000O0O0 +=95 #line:11
		elif O00OOOOO0OOO0OOOO in 'BSPEAKVXY&UwNRCHD':OO0OO0O0OO000O0O0 +=112 #line:12
		elif O00OOOOO0OOO0OOOO in 'QGOMm%W@':OO0OO0O0OO000O0O0 +=135 #line:13
		else :OO0OO0O0OO000O0O0 +=50 #line:14
	return int (OO0OO0O0OO000O0O0 *6.5 /100 )#line:15
def Keyboard (Heading =xbmcaddon .Addon ().getAddonInfo ('name')):#line:17
	OO0000OOO000O00O0 =xbmc .Keyboard ('',Heading )#line:18
	OO0000OOO000O00O0 .doModal ()#line:19
	if (OO0000OOO000O00O0 .isConfirmed ()):#line:20
		return OO0000OOO000O00O0 .getText ()#line:21
def Browse (OO000000OO000OO0O ):#line:23
	import webbrowser #line:25
	O0OOOO0O0O0O0OOOO =webbrowser .open #line:27
	OOO0OOOOO0OOO0OO0 =xbmc .executebuiltin #line:28
	O0O0000O0OOO000O0 =lambda OOOOO0O0O00O00000 :xbmc .getCondVisibility (str (OOOOO0O0O00O00000 ))#line:29
	O000O0O0OOOO0OO0O =lambda O00O0OOOO00OO0OOO :OOO0OOOOO0OOO0OO0 ('StartAndroidActivity(,android.intent.action.VIEW,,%s)'%(O00O0OOOO00OO0OOO ))#line:30
	OOOOOOOO00O0OOO0O ='System.Platform.Android'#line:32
	if O0O0000O0OOO000O0 (OOOOOOOO00O0OOO0O ):O000O0O0OOOO0OO0O (OO000000OO000OO0O )#line:34
	else :O0OOOO0O0O0O0OOOO (OO000000OO000OO0O )#line:35
def Check ():#line:38
		import sys #line:40
		O0O00000O0O0OO0OO =xbmcaddon .Addon ().getAddonInfo #line:44
		O0OO0O0OO0OOO0O00 =O0O00000O0O0OO0OO ('name')#line:45
		OOO00000O00O0O0O0 =base64 .b64decode ('VG8gYWNjZXNzIFtDT0xPUiB3aGl0ZV1bQl1VSyBUVVJLIFBMQVlMSVNUWy9CXVsvQ09MT1JdIHlvdSB3aWxsIG5lZWQgYW4gYWNjZXNzIHRva2VuLiBQbGVhc2UgcHJlc3MgY29udGludWUgdG8gZ2V0IGFuIGFjY2VzcyB0b2tlbi4=')#line:46
		OOO0O0000O0OOOOO0 =OOO00000O00O0O0O0 #line:47
		OOOO00O0O00O00OO0 =base64 .b64decode ("SWYgeW91IGhhdmUgYWxyZWFkeSBnb3QgeW91ciB0b2tlbiBwbGVhc2Ugc2VsZWN0IFtCXVtDT0xPUiB3aGl0ZV1FbnRlciBUb2tlblsvQ09MT1JdWy9CXSBpZiB5b3UgZG8gbm90IGhhdmUgYSB0b2tlbiBwbGVhc2Ugc2VsZWN0IFtCXVtDT0xPUiB3aGl0ZV1HZXQgVG9rZW5bL0NPTE9SXVsvQl0gb3IgZ28gdG8gW0JdW0NPTE9SIHdoaXRlXWh0dHBzOi8vYml0Lmx5LzJXYWhkTlhbL0NPTE9SXVsvQl0gdmlhIGEgZXh0ZXJuYWwgZGV2aWNlLg==")#line:48
		OO00O0000OO0OO0O0 =xbmcaddon .Addon ().getSetting ('pin')#line:49
		OO0O0OO0OOO0OO00O =lambda OOO0OOO0O0O000000 :base64 .b64decode (str (OOO0OOO0O0O000000 ))#line:50
		OOO0O00O0O0OOO0OO =b64decode ("aHR0cHM6Ly9kZXZlbG9wbWVudC10b29scy5uZXQvdG9vbHMtYXBpL2FwaT9waW49").decode ('utf-8')+OO00O0000OO0OO0O0 +b64decode ("JmtleT0=").decode ('utf-8')+b64decode (Project_key ).decode ('utf-8')#line:51
		O00O00OOOO0000O00 =lambda O0O00OO0OO0OOO00O :requests .get (OOO0O00O0O0OOO0OO ,verify =False ).text .strip ()#line:52
		OO00OOOOOOO00000O =lambda O0000OO00O0O0O0OO :xbmcaddon .Addon ().setSetting (b64decode ("cGlu").decode ('utf-8'),O0000OO00O0O0O0OO )#line:53
		OO0O0000000OOO0O0 =lambda O0OOO0O0O0O000000 :xbmcgui .Dialog ().yesno (O0O00000O0O0OO0OO ('name'),O0OOO0O0O0O000000 ,yeslabel ="Continue",nolabel ='Cancel',)#line:54
		OO0OOO0O00O00OOOO =lambda OO0OO0OO00OO00O00 :xbmcgui .Dialog ().yesno (O0O00000O0O0OO0OO ('name'),OO0OO0OO00OO00O00 ,yeslabel ="Enter token",nolabel ='Get token',)#line:55
		O0O0OO0O000000O0O =bool (O00O00OOOO0000O00 (OO00O0000OO0OO0O0 )==b64decode ("UGluIFZlcmlmaWVk").decode ('utf-8'))#line:56
		OO00OOOO0OO0OO00O =base64 .b64decode ("aHR0cHM6Ly9iaXQubHkvMldhaGROWA==")#line:57
		if O0O0OO0O000000O0O :return #line:59
		else :#line:60
			if OO0O0000000OOO0O0 (OOO00000O00O0O0O0 ):#line:62
				if OO0OOO0O00O00OOOO (OOOO00O0O00O00OO0 ):#line:63
					OOOO00OO00OOOO00O =Keyboard (base64 .b64decode ('VHlwZSBZb3VyIGFjY2VzcyB0b2tlbiBoZXJl'))#line:64
					OO00OOOOOOO00000O (OOOO00OO00OOOO00O )#line:65
					Check ()#line:66
				else :#line:67
					Browse (OO00OOOO0OO0OO00O )#line:68
					sys .exit (1 )#line:69
			else :#line:70
				sys .exit ()

Check()
if mode==None:
    from resources.lib.modules.menus import main
    Check()
    main()

elif mode==1:
	from resources.lib.modules.menus import sub_menu
	sub_menu(name,url,icon,fanart)

elif mode==2:
	from xbmcaddon import Addon
	from addonvar import addon_id
	Addon(addon_id).openSettings()

elif mode==3:
	from resources.lib.modules.player import Player
	p = Player(name, url, icon)
	p.play_link()

elif mode==4:
	from resources.lib.modules.functions import BSHOWS
	from resources.lib.modules.best_series import  new_shows
	BSHOWS(new_shows)

elif mode==5:
	from resources.lib.modules.functions import BSHOWS
	BSHOWS(url)

elif mode==6:
	from resources.lib.modules.functions import BSHOWS2
	BSHOWS2(url)

elif mode==7:
	from resources.lib.modules.functions import SHOWIMAGE
	SHOWIMAGE(url)

elif mode==8:
	from resources.lib.modules.functions import BSHOWS_SERIES
	from resources.lib.modules.best_series import  most_popular
	BSHOWS_SERIES(most_popular)

elif mode==9:
	from resources.lib.modules.functions import BSHOWS_SERIES
	BSHOWS_SERIES(url)

elif mode==10:
	from resources.lib.modules.functions import BSHOWS_EPISODES
	BSHOWS_EPISODES(url)

elif mode==11:
	from resources.lib.modules.functions import ADDTOFAVS
	ADDTOFAVS(name, url, icon)

elif mode==12:
	from resources.lib.modules.functions import REMFAVS
	REMFAVS(name)

elif mode==13:
	from resources.lib.modules.functions import GETFAVS
	GETFAVS()

xbmcplugin.endOfDirectory(int(sys.argv[1]))

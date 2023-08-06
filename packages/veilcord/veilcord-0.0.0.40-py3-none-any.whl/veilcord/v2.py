from base64       import b64encode
from json         import dumps
from tls_client   import Session
from typing       import Optional, Literal
from websocket    import WebSocket
from json         import dumps, loads
from time         import sleep, time
from terminut     import printf as print
from threading    import Thread
from httpx        import get
from re           import search


class HTTPClient:
    def __init__(self):
        self.session = Session(client_identifier="firefox_113", random_tls_extension_order=True)


class Globals:
    session_id = None
    sessionThread = None
    sessionOn = True


class VeilCord:
    def __init__(
        self, 
        session: Optional[Session] = HTTPClient().session,
        device_type: Literal["browser", "mobile", "app"] = "browser", 
        user_agent: Optional[str] = None
    ) -> None:
        self.session = HTTPClient().session if session is None else session
        self.user_agent_browser = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
        self.user_agent_mobile  = "Discord-Android/170014;RNA"
        self.user_agent_app     = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9013 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36"
        self.device_type_browser = "Windows"
        self.device_type_mobile  = "Android"

        if device_type == "browser":
            self.device_type = "browser"
            if user_agent is not None:
                self.user_agent_browser = user_agent
        elif device_type == "mobile":
            self.device_type = "mobile"
            if user_agent is not None:
                self.user_agent_mobile = user_agent
        elif device_type == "app":
            self.device_type = "app"
            if user_agent is not None:
                self.user_agent_app = user_agent
        else:
            raise ValueError("An invalid device_type was provided. Acceptable values: ['browser', 'mobile', 'app']")
        
    
    def generateXProp(
        self,
        browsername: Optional[str] = None, 
        build_num:   Optional[int] = None
    ):
        if self.device_type == "mobile":
            xsup = {
                "os": self.device_type_mobile,
                "browser": "Discord Android",
                "device": "RMX2117L1",
                "system_locale": "en-US",
                "client_version": "177.21 - rn",
                "release_channel": "googleRelease",
                "device_vendor_id": "c3c29b3e-4e06-48ff-af49-ec05c504c63e",
                "browser_user_agent": "",
                "browser_version": "",
                "os_version": "31",
                "client_build_number": 1750160087099,
                "client_event_source": None,
                "design_id": 0
            }
        elif self.device_type == "browser":
            xsup = {
                "os": self.device_type_browser,
                "browser": browsername if browsername else "Firefox",
                "device": "",
                "system_locale": "en-US",
                "browser_user_agent": self.user_agent_browser,
                "browser_version": "113.0",
                "os_version": "10",
                "referrer": "",
                "referring_domain": "",
                "referrer_current": "",
                "referring_domain_current": "",
                "release_channel": "stable",
                "client_build_number": 198318,
                "client_event_source": None
            }
        elif self.device_type == "app":
            xsup = {
                "os": self.device_type_browser,
                "browser": "Discord Client",
                "release_channel": "stable",
                "client_version": "1.0.9013",
                "os_version": "10.0.22621",
                "os_arch": "x64",
                "system_locale": "en-US",
                "browser_user_agent": self.user_agent_app,
                "browser_version": "22.3.2",
                "client_build_number": 199537,
                "native_build_number": 32266,
                "client_event_source": None,
                "design_id": 0
            }
        else:
            raise ValueError("An invalid type for generateXProp() was provided. Acceptable values: ['browser', 'mobile', 'app']")
        
        if build_num is not None:
            xsup["client_build_number"] = build_num
        
        return b64encode(dumps(xsup, separators=(',', ':')).encode()).decode()


    def getFingerprint(
        self,
        xsup: Optional[str] = None,
        withCookies: Optional[bool] = True
    ) -> list:
        if not xsup:
            xsup = self.generateXProp()
        if self.device_type == "mobile":
            headers = {
                'Host': 'discord.com',
                'X-Super-Properties': xsup,
                'Accept-Language': 'en-US',
                'X-Discord-Locale': 'en-US',
                'X-Debug-Options': 'bugReporterEnabled',
                'User-Agent': self.user_agent_mobile,
                'Content-Type': 'application/json',
            }
        elif self.device_type == "browser":
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.5",
                "connection": "keep-alive",
                "host": "discord.com",
                "referer": "https://discord.com/register",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": self.user_agent_browser,
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": xsup
            }
        # elif self.device_type == "app":
        #     self.client.headers = {
        #         "authority": "discord.com",
        #         "accept": "*/*",
        #         "accept-language": "en-US",
        #         "connection": "keep-alive",
        #         "content-type": "application/json",
        #         "origin": "https://discord.com",
        #         "referer": "https://discord.com/channels/@me",
        #         'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
        #         'sec-ch-ua-mobile': '?0',
        #         'sec-ch-ua-platform': '"Windows"',
        #         'sec-fetch-dest': 'empty',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'same-origin',
        #         "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9013 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36",
        #         "x-debug-options": "bugReporterEnabled",
        #         "x-discord-locale": "en-US",
        #         "x-discord-timezone": "America/New_York",
        #         "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDEzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MjEiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMTMgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMiBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMjIuMy4yIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTk5NTM3LCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozMjI2NiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==",
        #     }
        else: raise ValueError("An invalid type for getFingerprint() was provided. Acceptable values: ['browser', 'mobile']")
        response = self.session.get('https://discord.com/api/v9/experiments', headers=headers)
        if withCookies:
            return response.json().get("fingerprint"), response.cookies
        return response.json().get("fingerprint")


    def _wsconn(self, token, type, keepAlive):
        ws = WebSocket()
        ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
        if type == 1:
            message = {
                "op":2,
                "d":{
                    "token":token,
                    "capabilities":8189,
                    "properties":{
                        "os":"Windows",
                        "browser":"Chrome",
                        "device":"",
                        "system_locale":"en-US",
                        "browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
                        "browser_version":"113.0.0.0",
                        "os_version":"10",
                        "referrer":"",
                        "referring_domain":"",
                        "referrer_current":"","referring_domain_current":"","release_channel":"stable",
                        "client_build_number":199356,"client_event_source":None,
                        "design_id":0
                    },
                    "presence":{
                        "status":"online",
                        "since":0,"activities":[],"afk":False
                    },
                    "compress":False,
                    "client_state":{
                        "guild_versions":{},"highest_last_message_id":"0","read_state_version":0,
                        "user_guild_settings_version":-1,"user_settings_version":-1,"private_channels_version":"0",
                        "api_code_version":0
                    }
                }
            }
        elif type == 2:
            message = {
            "op": 2,
            "d": {
                "token": token,
                "capabilities": 8189,
                "properties":{
                    "os": "Windows",
                    "browser": "Discord Client",
                    "device":"",
                    "system_locale": "en-US",
                    "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9013 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36",
                    "browser_version": "22.3.2",
                    "client_version": "1.0.9013",
                    "os_version": "10.0.22621",
                    "os_arch": "x64",
                    "referrer":" ",
                    "referring_domain": "",
                    "referrer_current": "",
                    "referring_domain_current": "",
                    "release_channel": "stable",
                    "client_build_number": 199357,
                    "native_build_number": 32266,
                    "client_event_source": None,
                    "design_id": 0
                },
                "presence":{
                        "status":"online",
                        "since":0,"activities":[],"afk":False
                    },
                "compress":False,
                "client_state":{
                    "guild_versions":{},
                    "highest_last_message_id":"0",
                    "read_state_version":0,
                    "user_guild_settings_version":-1,
                    "user_settings_version":-1,
                    "private_channels_version":"0",
                    "api_code_version":0
                }
            }
        }
        else:
            raise ValueError("Invalid type provided. [1,2]")

        ws.send(
            dumps(message)
        )
        for _ in range(5):
            try:
                result = loads(ws.recv())
            except:
                print("(!) Error Getting WS (probably invalid token)")
            if "heartbeat_interval" in dumps(result):
                rpbeat = result["d"].get("heartbeat_interval")
                # print(f"(~) HB: {rpbeat}")
            if "session_id" in dumps(result):
                session_id = result['d'].get("session_id")
                if not keepAlive: return session_id
                Globals.session_id = session_id
                # print(f"(~) SessionID: {session_id}")
                break
                
        if keepAlive:
            while Globals.sessionOn:
                sleep(rpbeat / 1000)
                ws.send(dumps({"op":1,"d":10}))
                # print(f"(*) Sent HB.")
            

    def getSession(self, token: str, type: int = 1, keepAlive: bool = False):
        if keepAlive: 
            print("[WARN] KeepAlive is expirimental")
            t1 = Thread(target=self._wsconn, args=[token, type, keepAlive])
            Globals.sessionThread = t1
            t1.start()
            while Globals.session_id is None:
                sleep(0.1)
            return Globals.session_id
        else:
            return self._wsconn(token, type, keepAlive)
    
    def closeSession(self, token):
        Globals.sessionOn = False
        if Globals.sessionThread is None:
            return print("(!) Cannot close an unopened session.")
        Globals.sessionThread.join()
        return
    
    
    
    
    # non self #
    
    def getBuildNum():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Alt-Used': 'discord.com',
            'Connection': 'keep-alive',
            'Referer': 'https://discord.com/',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-origin',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'trailers',
        }
        html = get(f"https://discord.com/app?_={(time() * 1000)}", headers=headers).text

        last_index = html.rfind('/assets/')
        closing_quote_index = html.find('"', last_index)
        prefetched_script = html[last_index:closing_quote_index]

        response = get(f'https://discord.com{prefetched_script}', headers=headers).text

        buildnum = response.split("buildNumber:\"")[1].split("\"")[0]
        
        return buildnum
    
    
    def extractCode(invite):
        """Extracts the invite code from a Discord invite link"""
        code_regex = r"(?:(?:http:\/\/|https:\/\/)?discord\.gg\/|discordapp\.com\/invite\/|discord\.com\/invite\/)?([a-zA-Z0-9-]+)"
        match = search(code_regex, invite)
        if match:
            try:
                return match.group(1)
            except:
                return match.group(0)
        else:
            return None
        
        
        
        
        
        
        
        
        
        
## out of the class for old projects use
        
def getBuildNum():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Alt-Used': 'discord.com',
        'Connection': 'keep-alive',
        'Referer': 'https://discord.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'trailers',
    }
    html = get(f"https://discord.com/app?_={(time() * 1000)}", headers=headers).text

    last_index = html.rfind('/assets/')
    closing_quote_index = html.find('"', last_index)
    prefetched_script = html[last_index:closing_quote_index]

    response = get(f'https://discord.com{prefetched_script}', headers=headers).text

    buildnum = response.split("buildNumber:\"")[1].split("\"")[0]
    
    return buildnum


def extractCode(invite):
    """Extracts the invite code from a Discord invite link"""
    code_regex = r"(?:(?:http:\/\/|https:\/\/)?discord\.gg\/|discordapp\.com\/invite\/|discord\.com\/invite\/)?([a-zA-Z0-9-]+)"
    match = search(code_regex, invite)
    if match:
        try:
            return match.group(1)
        except:
            return match.group(0)
    else:
        return None
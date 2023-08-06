# VeilCord.
<img src="https://img.shields.io/pypi/v/veilcord?style=for-the-badge&logo=python">
<img alt="followers" src="https://img.shields.io/github/followers/imvast?color=f429ff&style=for-the-badge&logo=github&label=Follow"/>

```less
              > Custom Discord Tools Going To Be Used For My Projects
                    And Available To Anyone Else Who Wants To Use <
```

---

### Installation
```yaml
! package NOT FULLY available for non-personal use !
```

### Example Usage
```py
from veilcord import VeilCord

veilcord = VeilCord(
    session = None, # for custom tls_client sessions
    device_type = "browser", # types : browser, mobile, app
    user_agent = None # for custom user agent
)

# GETTING X-Super-Properties
xsup = veilcord.generateXProp()
print(f"(+) Retrieved XSup: {xsup}")

# GETTING ALL THE COOKIES AND FINGERPRINT
cookies = veilcord.getFingerprint(xsup)
print(f"(+) Retrieved Fingerprint: {cookies[0]}")
# returns a set.  [0] - Fingerprint  |  [1] - COOKIESJAR


# GET THE NEW SESSION ID BS
token = ""
sessionid = veilcord.getSession(
      token = token, # obv the token 
      type = 1, # type : 1 - web | 2 - app
      keepAlive = False # keep the session alive | only needed if ur code is slow (avg. session is live for ~40 seconds.)
)
print(f"(+) Got Session ID: {sessionid}")

# close the session, if keepAlive is enabled.
# veilcord.closeSession(token)

```

---

## * [vast#1337](https://discord.com/users/1109124745477246988) | [imvast@github](https://github.com/imvast) | [vast.gay](https://vast.gay) *
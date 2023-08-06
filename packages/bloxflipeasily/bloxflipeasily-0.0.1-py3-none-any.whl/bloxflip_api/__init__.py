import cloudscraper


scraper = cloudscraper.create_scraper()
""""

For the purposes of copyright, it is important to note that the source code utilized within Bloxflip API INC's products and services is solely owned by the company. Any unauthorized use, reproduction, or distribution of this code without explicit permission from Bloxflip API INC is considered theft and may result in legal action being taken against the offending party. It is important to understand that while the code may be used for its intended purpose, it should not be stolen or copied under any circumstances.

Furthermore, it is essential to recognize that copyright laws exist to protect the intellectual property of individuals and companies alike. The theft of source code can have significant financial and reputational consequences for a company such as Bloxflip API INC. As such, it is crucial that individuals and organizations respect these laws and seek appropriate permissions before using any copyrighted material.

In addition to legal consequences, there may also be ethical considerations when it comes to using stolen or copied code. Using someone else's work without proper attribution not only violates copyright law but also undermines the hard work and creativity of the original author. It is important to maintain a sense of integrity and respect for intellectual property in all aspects of business and technology.

Overall, it is clear that proper copyright practices are essential in protecting the rights of individuals and companies in the tech industry. By respecting these laws and seeking appropriate permissions when necessary, we can ensure a fair and equitable environment for all involved parties."""


class user:
  def __init__(self, auth: str) -> None:
    self.auth = auth

  def ValidUserCheck(self, invaild_auth_message:None, success_auth_message=None) -> None:
    """Check if an auth is vaild"""
    scraping = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
    if scraping["success"] == False and invaild_auth_message == None:
      return "User's auth is invaild"
    else:
      scraping = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
      if scraping["success"] == False and invaild_auth_message != None:
        return invaild_auth_message
      else:
        scraping = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
    if scraping["success"] == True and success_auth_message == None:
      return "User's auth is vaild"
    else:
      if success_auth_message != None:
        return success_auth_message
        
  def userName(self, invaild_auth_message:None, success_auth_message=None) -> None:
    scraping = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
    if scraping == False and invaild_auth_message == None:
      return "User's auth is invaild"
    else:
      if scraping == True and invaild_auth_message != None:
        return invaild_auth_message
      else:
        pass
        username=scraping["user"]["robloxUsername"]
        return username


  def userID(self, invaild_auth_message:None, success_auth_message=None) -> None:
    scraping = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
    if scraping == False and invaild_auth_message == None:
      return "User's auth is invaild"
    else:
      if scraping == True and invaild_auth_message != None:
        return invaild_auth_message
      else:
        pass
        userID=scraping["user"]["robloxId"]
        return userID
  def userAffiliateCode(self, invaild_auth_message:None, success_auth_message=None) -> None:
    scraping = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
    if scraping == False and invaild_auth_message == None:
      return "User's auth is invaild"
    else:
      if scraping == True and invaild_auth_message != None:
        return invaild_auth_message
      else:
        pass
        affliateCode=scraping["user"]["affiliateCode"]
        return affliateCode
  def userRobux(self, invaild_auth_message:None) -> None:
      scraping = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
      if scraping == False and invaild_auth_message == None:
        return "User's auth is invaild"
      else:
        if scraping == True and invaild_auth_message != None:
          return invaild_auth_message
        else:
            pass
            wallet = scraping["user"]["wallet"]
        return f"{wallet:.2f}"


  def userWithdrawn(self, invaild_auth_message:None) -> None:
      scraping = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
      if scraping == False and invaild_auth_message == None:
        return "User's auth is invaild"
      else:
        if scraping == True and invaild_auth_message != None:
          return invaild_auth_message
        else:
            pass
            withdraaw = scraping["user"]["totalWithdrawn"]
        return f"{withdraaw:.2f}"



  def userWagered(self, invaild_auth_message:None) -> None:
    """Grab the user's wagered"""
    scraping = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
    if scraping == False and invaild_auth_message == None:
      return "User's auth is invaild"
    else:
      if scraping == True and invaild_auth_message != None:
        return invaild_auth_message
      else:
        pass
        wagered = scraping["user"]["wager"]
        return f"{wagered:.2f}"
        

  def test(self) -> None:
    """testing"""
    headers = {"x-auth-token": self.auth}
    r = scraper.get("https://rest-bf.blox.land/user", headers=headers).json()
    return r

class grab:
  def crash(games:int) -> None:
    """Grab the data from crash games"""
    if games > 34:
      return "Error: games limit is 34"
    else:
      history = scraper.get("https://rest-bf.blox.land/games/crash").json()["history"]
      data =  [float(crashpoint["crashPoint"]) for crashpoint in history][::-1][-games:]
      return data
  def roulette(games:int):
    """Grab the data from roulette games"""
    if games > 34:
      return "Bloxflip only supports 34 games"
    else:
      history = scraper.get("https://rest-bf.blox.land/games/roulette").json()["history"]
      data = [winningColor["winningColor"]for winningColor in history]
      return data
  def uncovered_locations(auth:str,games:int, invaild_auth_message=None) -> None:
    """Grab the data from mines game"""
    headers= {"x-auth-token": auth}
    params = {
      "size": games,
      "page":0,
    }
    r = scraper.get("https://rest-bf.blox.land/user", headers=headers).json()
    if not r["success"]:
      return "User's auth is invalid" if invaild_auth_message is None else invaild_auth_message
    else:
      r_2 = scraper.get("https://rest-bf.blox.land/games/mines/history", headers=headers, params=params).json()["data"]
      data = [uncovered_locations["uncoveredLocations"] for uncovered_locations in r_2]
      return data

  def uncovered_mines(auth:str,games:int, invaild_auth_message=None) -> None:
    """Grab the data from mines game"""
    headers= {"x-auth-token": auth}
    params = {
      "size": games,
      "page":0,
    }
    r = scraper.get("https://rest-bf.blox.land/user", headers=headers).json()
    if not r["success"]:
      return "User's auth is invalid" if invaild_auth_message is None else invaild_auth_message
    else:
      r_2 = scraper.get("https://rest-bf.blox.land/games/mines/history", headers=headers, params=params).json()["data"]
      data = [uncovered_locations["mineLocations"] for uncovered_locations in r_2]
      return data

  def completedLevels(auth:str,games:int, invaild_auth_message=None) -> None:
    """Grab the data from mines game"""
    headers= {"x-auth-token": auth}
    params = {
      "size": games,
      "page":0,
    }
    r = scraper.get("https://rest-bf.blox.land/user", headers=headers).json()
    if not r["success"]:
      return "User's auth is invalid" if invaild_auth_message is None else invaild_auth_message
    else:
      r_2 = scraper.get("https://rest-bf.blox.land/games/towers/history", headers=headers, params=params).json()["data"]
      data = [uncovered_locations["completedLevels"] for uncovered_locations in r_2]
      return data

class isActive:
  def crashActive(active_true, active_false):
    url = "https://rest-bf.blox.land/games/crash"
    a = scraper.get(url).json()
    if a["current"]["status"] != 2:
      return active_false
    else:
      return active_true

  def minesActive(invaild_auth_message:None,auth,active_true, active_false):
    r = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": auth}).json()
    if not r["success"]:
      return "User's auth is invalid" if invaild_auth_message is None else invaild_auth_message
    url = "https://rest-bf.blox.land/games/mines"
    headers = {"x-auth-token": auth}
    a = scraper.get(url,headers=headers).json()
    if a["hasGame"] == False:
      return active_false
    else:
      if a["hasGame"] == True:
        return active_true

  def towersActive(invaild_auth_message:None,auth,active_true, active_false):
    r = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": auth}).json()
    if not r["success"]:
      return "User's auth is invalid" if invaild_auth_message is None else invaild_auth_message
    url = "https://rest-bf.blox.land/games/towers"
    headers = {"x-auth-token": auth}
    a = scraper.get(url,headers=headers).json()
    if a["hasGame"] == False:
      return active_false
    else:
      if a["hasGame"] == True:
        return active_true


class uuid:
  """"Grab a game current uuid"""
  def crash():
    url = scraper.get("https://rest-bf.blox.land/games/crash").json()
    uuid = url["current"]["_id"]
    return uuid

  def roulette():
    url = scraper.get("https://rest-bf.blox.land/games/roulette").json()
    uuid = url["current"]["_id"]
    return uuid

  def jackpot():
    url = scraper.get("https://rest-bf.blox.land/games/crash").json()
    uuid = url["current"]["_id"]
    return uuid



class create:
  def __init__(self, auth: str) -> None:
    self.auth = auth

  def mines(self, mines, bet, invalid_auth_message=None, invalid_bet_message=None, invalid_mines_message=None,user_has_invalid_balance_message=None, success_game_started=None) -> None:
    r = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
    if not r["success"]:
      return "User's auth is invalid" if invalid_auth_message is None else invalid_auth_message
    else:
      if bet < 5 or bet == 0 and invalid_bet_message == None:
        return "Bet is less 5"
      else:
        if bet < 5 or bet == 0 and invalid_bet_message != None:
          return invalid_bet_message
        else:
          if mines == 0 or mines >24 and invalid_mines_message == None:
            return "Mine's is over 24 or is 0"
          else:
            if mines == 0 or mines > 24 and invalid_mines_message != None:
              return invalid_mines_message
            else:
              user = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
              wallet = user["user"]["wallet"]
              if wallet < bet and user_has_invalid_balance_message == None:
                return "Error: Bet is higher than user's robux"
              else:
                if wallet < bet and user_has_invalid_balance_message != None:
                  return user_has_invalid_balance_message
                else:
                  #Posting the data
                  json = {
                    "betAmount": bet,
"mines": mines
                  }
                  headers = {"x-auth-token": self.auth}
                  data_combined = scraper.post("https://rest-bf.blox.land/games/mines/create", headers=headers, json=json)
                  if success_game_started == None:
                    return "Game has been started successfully"
                  else:
                    json = {
                    "betAmount": bet,
"mines": mines
                  }
                    headers = {"x-auth-token": self.auth}
                    data_combined = scraper.post("https://rest-bf.blox.land/games/mines/create", headers=headers, json=json)
                    if success_game_started == None:
                      return success_game_started                            

  def towers(self, mode, bet, invalid_auth_message=None, invalid_bet_message=None, invalid_mines_message=None,user_has_invalid_balance_message=None, success_game_started=None, invalid_mode_message=None) -> None:
    if invalid_mode_message is None:
        if mode not in ['easy', 'normal', 'hard']:
            return "Error: Mode is not in list"
    else:
        if mode not in list and invalid_mode_message != None:
            return invalid_mode_message
    r = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
    if not r["success"]:
        return "User's auth is invalid" if invalid_auth_message is None else invalid_auth_message
    else:
        if bet < 5 or bet == 0 and invalid_bet_message == None:
            return "Bet is less 5"
        else:
            if bet < 5 or bet == 0 and invalid_bet_message != None:
                return invalid_bet_message
            else:
                user = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
                wallet = user["user"]["wallet"]
                if wallet < bet and user_has_invalid_balance_message == None:
                    return "Error: Bet is higher than user's robux"
                else:
                    if wallet < bet and user_has_invalid_balance_message != None:
                        return user_has_invalid_balance_message
                    else:
                        #Posting the data
                        json = {
                            "betAmount": bet,
                            "difficulty": mode
                        }
                        headers = {"x-auth-token": self.auth}
                        data_combined = scraper.post("https://rest-bf.blox.land/games/towers/create", headers=headers, json=json)
                        if success_game_started == None:
                          return "Game started successfully"
                        else:
                          json = {
                            "betAmount": bet,
                            "difficulty": mode
                        }
                          headers = {"x-auth-token": self.auth}
                          data_combined = scraper.post("https://rest-bf.blox.land/games/towers/create", headers=headers, json=json)
                          if success_game_started != None:
                            return success_game_started

class click:
  def __init__(self, auth: str) -> None:
    self.auth = auth

  def mines(self, spot, no_game_message=None, invalid_auth_message=None, successfully_started_clicked_message=None) -> None:
    r = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
    if not r["success"]:
      return "User's auth is invalid" if invalid_auth_message is None else invalid_auth_message
    else:
      url = scraper.get("https://rest-bf.blox.land/games/mines", headers={"x-auth-token": self.auth}).json()
      if url["hasGame"] == False and no_game_message == None:
        return "User has no active game"
      else:
        if url["hasGame"] == False and no_game_message != None:
          return no_game_message
        else:
          if successfully_started_clicked_message == None:
            json = {
            "cashout": False,
            "mine": spot
          }
            url = "https://rest-bf.blox.land/games/mines/action"
            headers = {"x-auth-token": self.auth}
            data = scraper.post(url, headers=headers, json=json).json()
            return f"Successfully clicked {spot}."
          else:
            if successfully_started_clicked_message != None:
              json = {
            "cashout": False,
            "mine": spot
          }
              url = "https://rest-bf.blox.land/games/mines/action"
              headers = {"x-auth-token": self.auth}
              data = scraper.post(url, headers=headers, json=json)
              return successfully_started_clicked_message

  def towers(self, spot, no_game_message=None, invalid_auth_message=None, successfully_started_clicked_message=None) -> None:
    r = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
    if not r["success"]:
      return "User's auth is invalid" if invalid_auth_message is None else invalid_auth_message
    else:
      url = scraper.get("https://rest-bf.blox.land/games/towers", headers={"x-auth-token": self.auth}).json()
      if url["hasGame"] == False and no_game_message == None:
        return "User has no active game"
      else:
        if url["hasGame"] == False and no_game_message != None:
          return no_game_message
        else:
          if successfully_started_clicked_message == None:
            json = {
            "cashout": False,
            "tile": spot
          }
            url = "https://rest-bf.blox.land/games/towers/action"
            headers = {"x-auth-token": self.auth}
            data = scraper.post(url, headers=headers, json=json).json()
            return f'Successfully clicked {spot}'
          else:
            if successfully_started_clicked_message != None:
              json = {
            "cashout": False,
            "tile": spot
          }
              url = "https://rest-bf.blox.land/games/towers/action"
              headers = {"x-auth-token": self.auth}
              data = scraper.post(url, headers=headers, json=json).json()
              return successfully_started_clicked_message

  def mines_cashout(self, invalid_auth_message=None, no_game_message=None, game_ended_message=None) -> None:
    r = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
    if not r["success"]:
      return "User's auth is invalid" if invalid_auth_message is None else invalid_auth_message
    else:
      url = scraper.get("https://rest-bf.blox.land/games/mines", headers={"x-auth-token": self.auth}).json() 
      if url["hasGame"] == False and no_game_message == None:
        return "User has no active game"
      else:
        if url["hasGame"] == False and no_game_message != None:
          return no_game_message
        else:
          if game_ended_message == None:
            response = scraper.post("https://rest-bf.blox.land/games/mines/action", headers={
                            "x-auth-token": self.auth
                        },
                        json={
                            "cashout": True
                        }
                    ).json()
            return "Game has been ended"
          else:
                      if game_ended_message != None:
                        response = scraper.post("https://rest-bf.blox.land/games/mines/action", headers={
                            "x-auth-token": self.auth
                        },
                        json={
                            "cashout": True
                        }
                    ).json()
                        return game_ended_message
          

  def towers_cashout(self, invalid_auth_message=None, no_game_message=None, game_ended_message=None) -> None:
    r = scraper.get("https://rest-bf.blox.land/user", headers={"x-auth-token": self.auth}).json()
    if not r["success"]:
      return "User's auth is invalid" if invalid_auth_message is None else invalid_auth_message
    else:
      url = scraper.get("https://rest-bf.blox.land/games/towers", headers={"x-auth-token": self.auth}).json() 
      if url["hasGame"] == False and no_game_message == None:
        return "User has no active game"
      else:
        if url["hasGame"] == False and no_game_message != None:
          return no_game_message
        else:
          if game_ended_message == None:
            response = scraper.post("https://rest-bf.blox.land/games/towers/action", headers={
                            "x-auth-token": self.auth
                        },
                        json={
                            "cashout": True
                        }
                    ).json()
            return "Game has been ended"
          else:
                      if game_ended_message != None:
                        response = scraper.post("https://rest-bf.blox.land/games/towers/action", headers={
                            "x-auth-token": self.auth
                        },
                        json={
                            "cashout": True
                        }
                    ).json()
                        return game_ended_message
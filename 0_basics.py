#!/usr/bin/env python
# coding: utf-8

# # Cricket Simulator
# 1. Database search & get data
# 2. EDA
# 3. EDA Plots
# 4. Simulator for scores

# In[1]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[3]:


p_names = {
    'ind': {
        'bt': ['rsharma', 'klrahul', 'vkohli', 'arahane', 'stendulkar', 'rdravid', 'sganguly'], 
        'wk': ['dhoni'], 'all': ['hpandya', 'jadeja', 'kpandya', 'ysingh'], 
        'bl': ['bkumar', 'rashwin', 'mdshami', 'bumrah', 'akumble', 'hsingh', 'isharma', 'zkhan', 'anehra']
    }, 
           
    'aus': {
        'bt': ['mhayden', 'rponting', 'mhussey', 'jlanger', 'ssmith'], 
        'wk': ['agilchrist'], 'all': ['symonds', 'abitchell'], 
        'bl': ['swarne', 'mmarsh', 'blee', 'gmcgrath']
    }, 
    
    'saf': {
        'bt': ['gkirsten', 'bdipenner', 'abdevilliers', 'hgibbs', 'faulkner', 'gsmith'], 
        'wk': ['mboucher'], 'all': ['spollock', 'kallis'], 
        'bl': ['adonald', 'mntini', 'dsteyn']
    }, 
    
    'win': {
        'bt': ['cgayle', 'whinds', 'blara', 'schanderpaul'], 
        'wk': ['keepr'], 'all': ['pollard', 'bravo'], 
        'bl': ['bkumar', 'rashwin', 'mdshami', 'bumrah']
    }, 
    
    'sri': {
        'bt': ['kaluwithrana', 'atapattu', 'jayavardene'], 
        'wk': ['sangakara'], 'all': ['jayasuriya', 'adesilva'], 
        'bl': ['cvaas', 'murali', 'fernando', 'yokumar']
    }
          }


# In[4]:


class Team():
    '''
    Class of Team object
    Attributes like team name, matches played, wins, etc. 
    will be part of this class
    '''
    
    def_compos = {'bt': 4, 'wk': 1, 'all': 2, 'bl': 4}
    
    def __init__(self, team_name):
        self.team_name = team_name
        self.m_played = 0
        self.m_wins = 0
        self.team_compos = Team.def_compos
        self.players = self.generate_team()
        
        
    def generate_team(self):
        curr_team = {skill: list(np.random.choice(p_names[self.team_name][skill], self.team_compos[skill]))
                     for skill in ['bt', 'wk', 'all', 'bl']}
        self.players_obj_list = {curr_team[sk][i]: Player(p_name = curr_team[sk][i], p_skill = sk) for sk in ['bt', 'wk', 'all', 'bl'] for i in range(len(curr_team[sk]))}      
        return curr_team
    
    
    def update_team_comp(self, sk_bt = None, sk_wk = None, sk_all = None, sk_bl = None):
        if sk_bt != None:
            self.team_compos['bt'] = sk_bt
        if sk_wk != None:
            self.team_compos['wk'] = sk_wk
        if sk_all != None:
            self.team_compos['all'] = sk_all
        if sk_bl != None:
            self.team_compos['bl'] = sk_bl
    
    


# In[5]:


class Player():
    '''
    Class of Player object
    Attributes like player name, matches played, runs, wickets, wins, etc. 
    will be part of this class
    '''
    
    def __init__(self, p_name, p_skill):
        self.p_name = p_name
        self.p_skill = p_skill  # batsman, bowler, wk
        self.m_played = 0
        self.bt_runs = 0
        self.bt_balls = 0
        self.bl_wkts = 0
        self.bl_runs = 0
        self.bl_balls = 0
        self.m_wins = 0
        
        
    def update_bt_runs(self):
        pass
    
    
    def update_bt_balls(self):
        pass
    
    
    def update_bl_wkts(self):
        pass
    
    
    def update_bl_runs(self):
        pass
    
    
    def update_bl_balls(self):
        pass
    
    
    def update_score(self):
        pass


# In[6]:


class Match():
    '''
    Class of Match object
    Attributes like teams playing, runs scored, wickets taken, etc. 
    will be part of this class
    '''
    match_cnt = 0
    match_dict = {}
    
    def __init__(self, team1, team2):
        Match.match_cnt += 1
        Match.match_dict[Match.match_cnt] = [team1, team2]
        self.teams = [team1, team2]
        self.first_bt_team = np.random.choice(self.teams, 1)[0]
        self.second_bt_team = list(set(self.teams).difference(set(self.bt_team)))[0]
        


# In[7]:


class Innings(Match):
    '''
    Class of Innings object
    Attributes like runs scored, wickets taken, etc. 
    will be part of this class
    '''
    
    wkts_proba = {0: 995, 1: 0.005}
    runs_proba = {0: 0.6, 1: 0.23, 2: 0.1, 3: 0.005, 4: 0.054, 5: 0.001, 6: 0.01}
    
    def __init__(self, team1, team2):
        
        self.bt_team = bt_team
        self.bl_team = bl_team
        # batting stats
        self.runs = 0
        self.fours = 0
        self.sixes = 0
        self.boundary = 0
        # bowling stats
        self.wkts = 0
        self.wide = 0
        self.noball = 0
        self.bye = 0
        self.lbye = 0
        
    
    def simulate_ball(self, legal_flag = True):
        if legal_flag:
            balls += 1
            runs += Match.simulate_run()
            if (runs == 4) or (runs == 6):
                self.boundary += 1
                if runs == 4:
                    self.fours += 1
                else: 
                    self.sixes += 1
            
            
    # @ class method
    def simulate_run():
        run_in_ball = np.random.choice(a = [0, 1, 2, 3, 4, 5, 6], p = pd.Series(list(runs_proba.values())))
        return run_in_ball


# In[8]:


team_name = ['ind', 'saf', 'win', 'sri', 'aus']
team_list = {tn: Team(tn) for tn in team_name}


# In[9]:


TEAMNAME = 'ind'
team_list[TEAMNAME].team_name
team_list[TEAMNAME].players


# In[10]:


team_list[TEAMNAME].players_obj_list.keys()


# In[11]:


PLNAME = list(team_list[TEAMNAME].players_obj_list.keys())[3]
team_list[TEAMNAME].players_obj_list[PLNAME].p_name
team_list[TEAMNAME].players_obj_list[PLNAME].bt_runs


# In[12]:


team_list.keys()


# In[13]:


wkts_proba = {0: 0.977, 1: 0.023}
runs_proba = {0: 0.6, 1: 0.23, 2: 0.1, 3: 0.005, 4: 0.054, 5: 0.001, 6: 0.01}
pd.Series(list(runs_proba.values())).sum()
pd.Series(list(wkts_proba.values())).sum()


# In[14]:


def simulate_score(wkts, balls):
    
    balls += 1
    wkts_in_ball = np.random.choice(a = [0, 1], p = pd.Series(list(wkts_proba.values())))
    if wkts_in_ball:
        wkts += 1
        run_in_ball = -1
    else: 
        run_in_ball = np.random.choice(a = [0, 1, 2, 3, 4, 5, 6], p = pd.Series(list(runs_proba.values())))
    
    return (wkts, wkts_in_ball, run_in_ball, balls)


# In[15]:


def run_bkts(ball_run_dict):
    temp_df = pd.Series(list(ball_run_dict.values())).to_frame()
    temp_df.columns = ['runs']

    score_df = temp_df['runs'].value_counts().to_frame()
    score_df['score'] = score_df.index
    score_df['run_sum'] = score_df['score'] * score_df['runs']

    return score_df


# In[16]:


def innings_simulator():
    wkts = 0
    balls = 0
    runs = 0
    ball_run_dict = {}
    ball_wkt_dict = {}

    while wkts <= 10: 
        if balls >= 300:
            break
        else:
            wkts, wkts_in_ball, run_in_ball, balls = simulate_score(wkts, balls)
            ball_run_dict[balls] = run_in_ball
            ball_wkt_dict[balls] = wkts_in_ball
    #         f"balls: {balls} | wkts: {wkts} | run: {run_in_ball}"
            runs += run_in_ball if run_in_ball != -1 else 0
    print(f"overall runs: {runs}")
    print(f"balls: {balls}")
    print(f"wkts: {pd.Series(list(ball_wkt_dict.values())).sum()}")
    
    return run_bkts(ball_run_dict)


# In[24]:


innings_simulator()


# In[ ]:





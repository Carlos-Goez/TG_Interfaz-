# -*-coding utf-8-*-
import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout 
import matplotlib.pyplot as plt
import sqlite3
import os
import time

plt.plot([1, 23, 2, 4])
plt.ylabel('some numbers')


def conect_to_database(path):
    try:
        con = sqlite3.connect(path)
        con.commit()
        con.close()
    except Exception as e:
        print(e)      

class MainWid(ScreenManager):
    def __init__(self,**kwargs):
        super(MainWid,self).__init__()
        self.APP_PATH = os.getcwd()
        self.DB_PATH = self.APP_PATH+"/my_database.db"
        
        #Instaciamos las pantallas 
        self.HistoryWid = HistoryWid(self)
        self.StatsWid = StatsWid(self)
        self.HomeWid = HomeWid(self)
        self.SettingsWid = SettingsWid(self)
        
        #Control botones 
        wid = Screen(name ='Home')
        wid.add_widget(self.HomeWid)
        self.add_widget(wid)
        wid = Screen(name ='History')
        wid.add_widget(self.HistoryWid)
        self.add_widget(wid)
        wid = Screen(name ='Stats')
        wid.add_widget(self.StatsWid)
        self.add_widget(wid)
        wid = Screen(name='Settings')
        wid.add_widget(self.SettingsWid)
        self.add_widget(wid)
        
        self.goto_Home()
        
    def goto_Home(self):
        self.current = 'Home'
    def goto_History(self):
        self.current = 'History'
    def goto_Stats(self):
        self.current = 'Stats'
    def goto_Settings(self):
        self.current = 'Settings'
        
            
class HomeWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(HomeWid,self).__init__()
        self.mainwid = mainwid    
    def change_Home(self):
        self.mainwid.goto_Home()
    def change_History(self):
        self.mainwid.goto_History()
    def change_Stats(self):
        self.mainwid.goto_Stats()
    def change_Settings(self):
        self.mainwid.goto_Settings() 
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")     

class HistoryWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(HistoryWid,self).__init__()
        self.mainwid = mainwid
    def change_Home(self):
        self.mainwid.goto_Home()
    def change_History(self):
        self.mainwid.goto_History()
    def change_Stats(self):
        self.mainwid.goto_Stats()
    def change_Settings(self):
        self.mainwid.goto_Settings()

class StatsWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(StatsWid,self).__init__()
        self.mainwid = mainwid
    def change_Home(self):
        self.mainwid.goto_Home()
    def change_History(self):
        self.mainwid.goto_History()
    def change_Stats(self):
        self.mainwid.goto_Stats()
    def change_Settings(self):
        self.mainwid.goto_Settings()

class SettingsWid(BoxLayout):
    def __init__(self,mainwid,**kwargs):
        super(SettingsWid,self).__init__()
        self.mainwid = mainwid
    def change_Home(self):
        self.mainwid.goto_Home()
    def change_History(self):
        self.mainwid.goto_History()
    def change_Stats(self):
        self.mainwid.goto_Stats()
    def change_Settings(self):
        self.mainwid.goto_Settings()
        
class GridHistorico(GridLayout):
    pass
         
class MainApp(App):
    title = 'main'
    def build(self):
        return MainWid()
    
if __name__ == "__main__":
    MainApp().run()
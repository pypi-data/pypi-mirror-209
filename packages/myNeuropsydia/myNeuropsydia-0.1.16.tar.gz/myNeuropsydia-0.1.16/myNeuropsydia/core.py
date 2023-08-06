# -*- coding: utf-8 -*-
# screen 
monitor_diagonal = 24

import myNeuropsydia.screen as scr

import os
import pygame

import numpy as np
import datetime

from .path import *
from .screen import *


 
def newpage(color_name="white", opacity=100, 
            fade=False, fade_speed=60, fade_type="out", 
            auto_refresh=True):
    
    """
    Fill the background with a color.

    Parameters
    ------------
        color_name : str, tuple, optional
            name of the color (see color() function), or an RGB tuple (e.g., (122,84,01)).
        opacity : int, optional
            opacity of the color (in percents).
        fade : bool, optional
            do you want a fade effect?
        fade_speed : int, optional
            frequency (speed) of the fading.
        fade_type : str, optional
            "out" or "in", fade out or fade in.


    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.newpage("blue")
    >>> n.refresh()
    >>> n.time.wait(500)
    >>> n.close()

    Notes
    ----------
    *Authors*

    - Dominique Makowski (https://github.com/DominiqueMakowski)

    *Dependencies*

    - pygame
    - time
    """
    
    if color_name is not None:
        if fade is False:
            if opacity == 100:
                try:
                    scr.screen.fill(color(color_name))
                    #print('success')
                except:
     
                    print("NEUROPSYDIA ERROR: newpage(): wrong argument")
                    
            else:
                opacity = int(opacity * 255 / 100)
                color_name = color(color_name) + (opacity,)
                mask = pygame.Surface((scr.screen_width, 
                                       scr.screen_height), 
                                      pygame.SRCALPHA)  # per-pixel alpha
                
                mask.fill(color_name)  # notice the alpha value in the color
                scr.screen.blit(mask, (0, 0))
                
            if auto_refresh is True:
                refresh()
                
        if fade is True:
            original_color_name = color_name
            clock = pygame.time.Clock()
            
            for i in range(0, 40, 1):
                clock.tick_busy_loop(fade_speed)
                if fade_type == "out":
                    color_name = color(original_color_name) + (i,)
                else:
                    color_name = color(original_color_name) + (255-i, )
                    
                mask = pygame.Surface((scr.screen_width, 
                                       scr.screen_height), 
                                      pygame.SRCALPHA)  # per-pixel alpha
                
                mask.fill(color_name)  # notice the alpha value in the color
                scr.screen.blit(mask, (0, 0))
                refresh()
                
            scr.screen.fill(color(original_color_name))
    
    
def refresh():
    
    """
    Refresh / flip the screen: actually display things on screen.


    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.newpage("blue")
    >>> n.refresh()
    >>> n.time.wait(500)
    >>> n.close()

    Notes
    ----------
    *Authors*

    - Dominique Makowski (https://github.com/DominiqueMakowski)

    *Dependencies*

    - pygame
    """

    pygame.display.flip()
    

keys = {
"normal":
    {109: ',', 44: ';', 46: ':',47: '!', 97: 'q',
     98: 'b', 99: 'c', 100: 'd', 101: 'e',
     102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j',
     107: 'k', 108: 'l', 59: 'm', 110: 'n', 111: 'o',
     112: 'p', 113: 'a', 114: 'r', 115: 's', 116: 't',
     117: 'u', 118: 'v', 119: 'z', 120: 'x', 121: 'y',
     122: 'w', 57: 'ç', 56: '_', 55: 'è', 54: '-', 53: '(',
     52: "_", 51: '_', 50:'é', 49: '&', 48: 'à', 32: 'SPACE',
     13: "ENTER",276: "LEFT",274: "DOWN",275: "RIGHT",273: "UP",
     266: ".",
     pygame.K_KP0: '0', pygame.K_KP1: '1', pygame.K_KP2: '2', pygame.K_KP3: '3',pygame.K_KP4: '4', pygame.K_KP5: '5',pygame.K_KP6: '6',pygame.K_KP7: '7',pygame.K_KP8: '8',pygame.K_KP9: '9'},

"shift":
    {109:'?', 44: '.', 46: '/',47: '§', 97: 'Q',
     98: 'B', 99: 'C', 100: 'D', 101 : 'E',
     102: 'F', 103: 'G', 104: 'H', 105: 'I', 106: 'J',
     107: 'K', 108: 'L', 59: 'M', 110: 'N', 111: 'O',
     112: 'P', 113: 'A', 114: 'R', 115: 'S', 116: 'T',
     117: 'U', 118: 'V', 119: 'Z', 120: 'X', 121: 'Y',
     122: 'W', 57: '9', 56: '8', 55: '7', 54: '6', 53: '5',
     52: '4', 51: '3', 50: '2', 49: '1', 48: '0', 32: 'SPACE',
     13: "ENTER",276: "LEFT",274: "DOWN",275: "RIGHT",273: "UP",
     266: ".",
     pygame.K_KP0: '0',pygame.K_KP1: '1',pygame.K_KP2: '2',pygame.K_KP3:'3',pygame.K_KP4: '4',
     pygame.K_KP5: '5',pygame.K_KP6: '6',pygame.K_KP7: '7',pygame.K_KP8: '8',pygame.K_KP9:'9'},

"altgr":
    {97: 'q', 98: 'b', 99: 'c', 100: 'd', 101 : '€',
     102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j',
     107: 'k', 108: 'l', 59: 'm', 110: 'n', 111: 'o',
     112: 'p', 113: 'a', 114: 'r', 115: 's', 116: 't',
     117: 'u', 118: 'v', 119: 'z', 120: 'x', 121: 'y',
     122: 'w', 57: '^', 56: '_', 55: '`', 54: '|', 53: '[',
     52: '{', 51: '#', 50: '~', 49: '1', 48: '@', 32: 'SPACE',
     13: "ENTER",276: "LEFT",274: "DOWN",275: "RIGHT",273: "UP",
     266: ".",
     pygame.K_KP0: '0',pygame.K_KP1: '1',pygame.K_KP2: '2',pygame.K_KP3: '3',pygame.K_KP4: '4',
     pygame.K_KP5: '5',pygame.K_KP6: '6',pygame.K_KP7: '7',pygame.K_KP8: '8',pygame.K_KP9: '9'}
}


def wait_for_input(time_max=None, unicode = False):
    
    """
    Low level input checker.

    Parameters
    ----------
    time_max = int
        time max in ms

    Returns
    ----------
    key
        A key.
    Example
    ----------
    NA

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame
    - time
    """
    
    if pygame.event.get_blocked(pygame.KEYDOWN) is True:
        blocked = True
        pygame.event.set_allowed(pygame.KEYDOWN)
        
    else:
        blocked = False
        pygame.event.set_allowed(pygame.KEYDOWN)

    time_out = False
    loop = True
    
    event_tc = []
    if time_max is None:

        while loop:
            for event in pygame.event.get():
                
                event_tc.append(event)
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        modifier = "shift"
                    elif pygame.key.get_mods() & pygame.KMOD_RALT:
                        modifier = "altgr"
                    else:
                        modifier = "normal"
                    if event.key != pygame.K_RSHIFT and event.key != pygame.K_LSHIFT and event.key != pygame.K_RALT:
                        loop = False
                        
    else:
        
        local_time = Time()
        while loop and local_time.get(reset=False) < time_max:
            for event in pygame.event.get():
                
                event_tc.append(event)
                if event.type == pygame.KEYDOWN:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        modifier = "shift"
                    elif pygame.key.get_mods() & pygame.KMOD_RALT:
                        modifier = "altgr"
                    else:
                        modifier = "normal"
                    if event.key != pygame.K_RSHIFT and event.key != pygame.K_LSHIFT and event.key != pygame.K_RALT:
                        loop = False
                        
        if local_time.get(reset=False) > time_max:
            time_out = True


    
    if blocked is True:
        pygame.event.set_blocked(pygame.KEYDOWN)

    if time_out == True:
        return("Time_Max_Exceeded")
    
    else:
        while event_tc[-1].type != pygame.KEYDOWN:
            event_tc.pop()
            
        if unicode:
            return(event_tc[-1].unicode)
        
        else:
            try: 
                return(keys[modifier][event_tc[-1].key])
            
            except (KeyError, AttributeError):
                return(event.key)


def response(allow=None, enable_escape=True, 
             time_max=None, get_RT=True, unicode = False):
    
    """
    Get a (keyboard, for now) response.

    Parameters
    ----------
    allow : str or list
        Keys to allow.
    enable_escape : bool
        Enable escape key to exit.
    time_max : int
        Maximum time to wait for a response (ms).
    get_RT : bool
        Return response time.

    Returns
    ----------
    str or tuple
        returns a tuple when get_RT is set to True

    Notes
    ----------
    *Authors*

    - Dominique Makowski (https://github.com/DominiqueMakowski)

    *Dependencies*

    - pygame
    """
    
    local_time = Time()
    if allow is not None:
        if not isinstance(allow, list):
            allow = [allow]

    while True:
        if unicode:
            pressed_key = wait_for_input(time_max=time_max, unicode = True)
        else:
            pressed_key = wait_for_input(time_max=time_max)
        if pressed_key == "Time_Max_Exceeded":
            return("Time_Max_Exceeded", local_time.get())
        
        if pressed_key == pygame.K_ESCAPE:
            if enable_escape is True:
                if get_RT is True:
                    return("ESCAPE", local_time.get())
                else:
                    return("ESCAPE")
                
        elif allow is not None:
            if pressed_key in allow:
                if get_RT is True:
                    return(pressed_key, local_time.get())
                else:
                    return(pressed_key)
                
        else:
            if get_RT is True:
                return(pressed_key, local_time.get())
            else:
                return(pressed_key)


class Coordinates:
    
    """
    A class object to go from pygame corrdinates system to neuropsydia's and vice versa.

    Its methods (functions) are:
        - to_pygame()
        - from_pygame()

    Parameters
    ----------
    None

    Returns
    ----------
    None

    Example
    ----------
    None

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pygame
    """
    
    def to_pygame(x=None, y=None, 
                  distance_x=None, distance_y=None):
        
        """
        Convert coordinates from neuropsydia (-10:10) to pygame's system (in pixels).

        Parameters
        ----------
        x = float
            [-10:10]
        y = float
            [-10:10]
        distance_x = convert a horizontal distance
            [-10:10]
        distance_y = convert a horizontal distance
            [-10:10]
        Returns
        ----------
        NA

        Example
        ----------
        NA

        Authors
        ----------
        Dominique Makowski

        Dependencies
        ----------
        - pygame
        """
        
        if x != None and y == None:
            x = (x+10.0)/(10.0+10.0)*(scr.screen_width-0.0)+0.0
            return(int(x))
        
        if x == None and y != None:
            y = (-y+10.0)/(10.0+10.0)*(scr.screen_height-0.0)+0.0
            return(int(y))
        
        if x != None and y != None:
            x = (x+10.0)/(10.0+10.0)*(scr.screen_width-0.0)+0.0
            y = (-y+10.0)/(10.0+10.0)*(scr.screen_height-0.0)+0.0
            return(int(x),int(y))
        
        if distance_x != None and distance_y is None:
            distance_x = (distance_x)/(10.0+10.0)*(scr.screen_width-0.0)+0.0
            return(int(distance_x))
        
        if distance_y != None and distance_x is None:
            distance_y = (-distance_y)/(10.0+10.0)*(scr.screen_height-0.0)+0.0
            return(int(distance_y))
        
        if distance_x != None and distance_y != None:
            distance_x = (distance_x)/(10.0+10.0)*(scr.screen_width-0.0)+0.0
            distance_y = (-distance_y)/(10.0+10.0)*(scr.screen_height-0.0)+0.0
            return(int(distance_x), int(distance_y))



    def from_pygame(x=None, y=None,
                    distance_x=None, distance_y=None):
        
        """
        Help incomplete, sorry.

        Parameters
        ----------
        NA

        Returns
        ----------
        NA

        Example
        ----------
        NA

        Authors
        ----------
        Dominique Makowski

        Dependencies
        ----------
        - pygame
        """
        
        if x != None and y == None:
            x =20*x/scr.screen_width - 10
            return(x)
        
        if x == None and y != None:
            y = -(20*y/scr.screen_height) + 10
            return(y)
        
        if x != None and y != None:
            x =20*x/scr.screen_width - 10
            y = -(20*y/scr.screen_height) + 10
            return(x, y)

        if distance_x != None and distance_y is None:
            distance_x = (distance_x)*(10.0+10.0)/(scr.screen_width-0.0)
            return(distance_x)

        if distance_y != None and distance_x is None:
            distance_y = (distance_y)*(10.0+10.0)/(scr.screen_height-0.0)
            return(distance_y)
        
        if distance_x != None and distance_y != None:
            distance_x = (distance_x)*(10.0+10.0)/(scr.screen_width-0.0)
            distance_y = (distance_y)*(10.0+10.0)/(scr.screen_height-0.0)
            return(distance_x, distance_y)

        

    def to_physical(distance_x=None, distance_y=None, 
                    monitor_diagnonal=monitor_diagonal, unit="cm"):
        
        """
        Help incomplete, sorry.

        Parameters
        ----------
        monitor_diagonal = int
            in inches (24, 27, etc).

        Returns
        ----------
        NA

        Example
        ----------
        NA

        Authors
        ----------
        Dominique Makowski

        Dependencies
        ----------
        None
        """

        if unit=="cm":
            diagonal = monitor_diagonal*2.54

        coef = np.sqrt(((scr.screen_height*scr.screen_height) 
                        + (scr.screen_width*scr.screen_width))/(diagonal*diagonal))

        monitor_height = scr.screen_height/coef
        monitor_width = scr.screen_width/coef


        if distance_x != None and distance_y is None:
            distance_x = (distance_x)/(10.0+10.0)*(monitor_width-0.0)+0.0
            return(int(distance_x))
        
        if distance_y != None and distance_x is None:
            distance_y = (distance_y)/(10.0+10.0)*(monitor_height-0.0)+0.0
            return(int(distance_y))
        
        if distance_y != None and distance_x != None:
            distance_x = (distance_x)/(10.0+10.0)*(monitor_width-0.0)+0.0
            distance_y = (distance_y)/(10.0+10.0)*(monitor_height-0.0)+0.0
            return(distance_x, distance_y)
        
        
    def from_physical(distance_x=None, distance_y=None, 
                      monitor_diagonal=monitor_diagonal, unit="cm"):
        
        """
        Help incomplete, sorry.

        Parameters
        ----------
        monitor_diagonal = int
            in inches (24, 27, etc).

        Returns
        ----------
        NA

        Example
        ----------
        NA

        Authors
        ----------
        Dominique Makowski

        Dependencies
        ----------
        None
        """

        if unit=="cm":
            diagonal = monitor_diagonal*2.54

        coef = np.sqrt(((scr.screen_height*scr.screen_height) 
                        + (scr.screen_width*scr.screen_width))/(diagonal*diagonal))

        monitor_height = scr.screen_height/coef
        monitor_width = scr.screen_width/coef


        if distance_x != None and distance_y is None:
            distance_x = (distance_x)*(10.0+10.0)/(monitor_width-0.0)+0.0
            return(int(distance_x))
        
        if distance_y != None and distance_x is None:
            distance_y = (distance_y)*(10.0+10.0)/(monitor_height-0.0)+0.0
            return(int(distance_y))
        
        if distance_y != None and distance_x != None:
            distance_x = (distance_x)/(10.0+10.0)*(monitor_width-0.0)+0.0
            distance_y = (distance_y)/(10.0+10.0)*(monitor_height-0.0)+0.0
            return(distance_x, distance_y)

'''
class Font_Cache_Init:
    
    def __init__(self):
        self.cache = {}  #Initialize an empty cache
        
    def get(self,font_path,size):
        
        if not (font_path,int(size)) in self.cache:  #if not in cache,
            if os.path.exists(font_path):  #if the path leads to a font,
                self.cache[font_path,int(size)] = pygame.font.Font(font_path, int(size))  
              
            else:
                self.cache[font_path,int(size)] = pygame.font.SysFont(font_path, int(size))  #load a system font
        
        return(self.cache[font_path,int(size)])
    
    
 #Create the font object that will update itself with the different loaded fonts
'''

color_list = {
"white":(255,255,255),
"w":(255,255,255),
"black":(0,0,0),
"b":(0,0,0),
"grey":(128,128,128),
"g":(128,128,128),
"raw_red":(255,0,0),
"raw_green":(0,255,0 ),
"raw_blue":(0, 0, 255),

"red":(244,67,54),
"pink":(233,30,99),
"purple":(156,39,176),
"deeppurple":(103,58,183),
"indigo":(63,81,181),
"blue":(33,150,243),
"lightblue":(3,169,244),
"cyan":(0,188,212),
"teal":(0,150,136),
"green":(76,175,80),
"lightgreen":(139,195,74),
"lime":(205,220,57),
"yellow":(255,235,59),
"amber":(255,193,7),
"orange":(255,152,0),
"deeporange":(255,87,34),
"brown":(121,85,72),
"lightgrey":(220,220,220),
"darkgrey":(105,105,105),
"bluegrey":(96,125,139),

"pale_red":(239,154,154),
"pale_pink":(244,143,177),
"pale_purple":(206,147,216),
"pale_deeppurple":(179,157,219),
"pale_indigo":(159,168,218),
"pale_blue":(144,202,249),
"pale_light_blue":(129,212,250),
"pale_cyan":(128,222,234),
"pale_teal":(128,203,196),
"pale_green":(165,214,167),
"pale_lightgreen":(197,225,165),
"pale_lime":(230,238,156),
"pale_yellow":(255,245,157),
"pale_amber":(255,224,130),
"pale_orange":(255,204,128),
"pale_deeporange":(255,171,145),
"pale_brown":(188,170,164),

"blue_shade":[(204,229,255),(153,204,255),(102,178,222),(51,153,255),(0,128,255)],
"red_shade":[(255,204,204),(255,153,153),(255,102,102),(255,51,51),(255,0,0)],
"green_shade":[(204,255,204),(153,255,153),(102,255,102),(51,255,51),(0,255,0)],
"multi_shade":[(255,51,51),(255,51,255),(51,153,255),(51,255,51),(255,153,51)]
}


def color(color):
    
    """
    Returns an RGB color tuple (or list) from its name.

    Parameters
    ----------
    color = str
        one from the color_list list

    Returns
    ----------
    tuple or list

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> print(n.color_list)
    >>> print(n.color("blue"))
    >>> n.close()

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    None
    """
    
    if isinstance(color,str):
        try:
            return(color_list[color])
        except:
            print("NEUROPSYDIA WARNING: color() was used, however the argument " + str(color) + " was not detected and might cause errors.")
            return(color)
        
    else:
        return(color)


def cursor(visible=True):
    
    """
    Set the mouse cursor to visible or invisible.

    Parameters
    ----------
    visible = bool
        True for visible, False for invisible.

    Returns
    ----------
    None

    Example
    ----------
    >>> import neuropsydia as n
    >>> n.start()
    >>> n.cursor(True)
    >>> n.time.wait(2000)
    >>> n.close()

    Authors
    ----------
    The pygame team

    Dependencies
    ----------
    - pygame 1.9.2
    """
    
    pygame.mouse.set_visible(visible)

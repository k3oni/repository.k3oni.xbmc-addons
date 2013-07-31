
import time
import simplejson
from channel import BaseChannel, ChannelException,ChannelMetaClass, STATUS_BAD, STATUS_GOOD, STATUS_UGLY
from utils import *

##################
## AlJazeera AR ##
##################

class AlJazeeraArabic(BaseChannel):
    playable = False
    short_name = 'aljazeera_ar'
    long_name = 'Al-Jazeera Live (Arabic)'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
	data.update({'action': 'play_stream', 'Title': 'High Definition', 'stream_url': 'rtmp://hd3.lsops.net/live playpath=aljazeer_ar_838 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" pageURL="http://www.livestation.com/channels/3-al-jazeera-english-english" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Standard Definition', 'stream_url': 'rtmp://hd3.lsops.net/live playpath=aljazeer_ar_372 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" pageURL="http://www.livestation.com/channels/3-al-jazeera-english-english" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Low Definition', 'stream_url': 'rtmp://hd3.lsops.net/live playpath=aljazeer_ar_145 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" pageURL="http://www.livestation.com/channels/3-al-jazeera-english-english" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

##################
## AlJazeera EN ##
##################

class AlJazeeraEnglish(BaseChannel):
    playable = False
    short_name = 'aljazeera'
    long_name = 'Al-Jazeera Live (English)'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
	data.update({'action': 'play_stream', 'Title': 'High Definition', 'stream_url': 'rtmp://hd2.lsops.net/live playpath=aljazeer_en_838 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" pageURL="http://www.livestation.com/channels/3-al-jazeera-english-english" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Standard Definition', 'stream_url': 'rtmp://hd2.lsops.net/live playpath=aljazeer_en_372 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" pageURL="http://www.livestation.com/channels/3-al-jazeera-english-english" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Low Definition', 'stream_url': 'rtmp://hd2.lsops.net/live playpath=aljazeer_en_145 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" pageURL="http://www.livestation.com/channels/3-al-jazeera-english-english" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

###############
## ABCNews24 ##
###############  

class ABCNews24(BaseChannel):
    playable=False
    short_name = 'abc24'
    long_name = "ABC News 24"
    default_action = 'list_streams'

    def action_list_streams(self):
	data = {}
	data.update(self.args)
	data.update({'action': 'play_stream', 'Title': 'ABC News 24 - (Australia Only)', 'stream_url': 'http://www.abc.net.au/res/streaming/video/hls/news24.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'ABC News 24', 'stream_url': 'rtmp://cp103653.live.edgefcs.net:1935/live?_fcs_vhost=cp103653.live.edgefcs.net&akmfv=1.8 playpath=international_medium@36382 swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
	self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

#########
## BBC ##
#########    
        
class BBC(BaseChannel):
    playable = False
    short_name = 'bbc'
    long_name = 'BBC'
    default_action = 'list_streams'

    def action_list_streams(self):
	data = {}
	data.update(self.args)
#     data.update({'action': 'play_stream', 'Title': 'BBC News', 'stream_url': 'rtmp://media4.lsops.net/live/ playpath=bbcnews_en_high.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageUrl="http://www.livestation.com/channels/10-bbc-world-news-english" swfVfy=true live=true'})
#         self.plugin.add_list_item(data, is_folder=False)
	data.update({'action': 'play_stream', 'Title': 'BBC World News', 'stream_url': 'http://akamedia2.lsops.net/live/bbcworld1_en.smil/playlist.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
	self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

#################
## BigPondNews ##
#################   

# class BigPondNews(BaseChannel):
#     playable = False
#     short_name = 'bigpond_news'
#     long_name = 'BigPond News'
#     default_action = 'list_streams'
#     
#     def action_list_streams(self):
#         data = {}
#         data.update(self.args)
#         data.update({'action': 'play_stream', 'Title': 'High Quality', 'stream_url': 'http://bptvlive.ngcdn.telstra.com/bp_online_bpnews_high'})
#         self.plugin.add_list_item(data, is_folder=False)
#         data.update({'action': 'play_stream', 'Title': 'Low Quality', 'stream_url': 'http://bptvlive.ngcdn.telstra.com/bp_online_bpnews_low'})
#         self.plugin.add_list_item(data, is_folder=False)
#         self.plugin.end_list()
# 
#     def action_play_stream(self):        
#         self.plugin.set_stream_url(self.args['stream_url'])

##########
## CNBC ##
##########

class CNBC(BaseChannel):
    playable = True
    short_name = 'cnbc'
    long_name = 'CNBC'
    default_action = 'play_stream' 

    def action_play_stream(self):
        self.plugin.set_stream_url('http://livestation_hls-lh.akamaihd.net/i/cnbc_en@106428/master.m3u8')

########
## RT ##
########
        
class RT(BaseChannel):
    playable = False
    short_name = 'rt'
    long_name = 'RT'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'English', 'stream_url': 'rtmp://fms5.visionip.tv/live app=live swfUrl=http://rt.com/s/swf/player5.4.viral.swf pageURL=http://rt.com/on-air/ playpath=RT_3 live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Spanish', 'stream_url': 'rtmp://rt.fms.visionip.tv/live/ app=live swfurl=http://actualidad.rt.com/swf/player.swf pageurl=http://actualidad.rt.com/mas/envivo/ playpath=RT_Spanish_3 swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Arabic', 'stream_url': 'rtmp://russiatoday.fms.visionip.tv/rt/Russia_al_yaum_1000k_1 app=rt/Russia_al_yaum_1000k_1 swfurl=http://arabic.rt.com/style/liveplayer.swf pageurl=http://arabic.rt.com/live_high playpath=1000k_1 swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

#############
## i24news ##
#############
        
class i24news(BaseChannel):
    playable = False
    short_name = 'i24news'
    long_name = 'i24news'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'English', 'stream_url': 'http://brightcove03-f.akamaihd.net/english_1_650@117902 '})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'French', 'stream_url': 'http://brightcove03-f.akamaihd.net/french_1_650@117902'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Arabic', 'stream_url': 'http://brightcove03-f.akamaihd.net/arabic_1_650@117902'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])
    
##############
## EuroNews ##
##############

class EuroNews(BaseChannel):
    playable = False
    short_name = 'euronews'
    long_name = 'EuroNews'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'Arabic', 'stream_url': 'rtmp://hd1.lsops.net/live/ swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf playpath=euronews_ar_340 pageUrl=http://www.livestation.com/ar/euronews'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'English', 'stream_url': 'rtmp://hd1.lsops.net/live/ swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf playpath=euronews_en_340 pageUrl=http://www.livestation.com/en/euronews'})
        self.plugin.add_list_item(data, is_folder=False)
	data.update({'action': 'play_stream', 'Title': 'French', 'stream_url': 'rtmp://hd1.lsops.net/live/ swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf playpath=euronews_fr_340 pageUrl=http://www.livestation.com/fr/euronews'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'German', 'stream_url': 'rtmp://hd1.lsops.net/live/ swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf playpath=euronews_de_340 pageUrl=http://www.livestation.com/de/euronews'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Italian', 'stream_url': 'rtmp://hd1.lsops.net/live/ swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf playpath=euronews_it_340 pageUrl=http://www.livestation.com/it/euronews'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Portuguese', 'stream_url': 'rtmp://hd1.lsops.net/live/ swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf playpath=euronews_pt_340 pageUrl=http://www.livestation.com/pt/euronews'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Russian', 'stream_url': 'rtmp://hd1.lsops.net/live/ swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf playpath=euronews_ru_340 pageUrl=http://www.livestation.com/ru/euronews'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Spanish', 'stream_url': 'rtmp://hd1.lsops.net/live/ swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf playpath=euronews_es_340 pageUrl=http://www.livestation.com/es/euronews'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Turkish', 'stream_url': 'rtmp://hd1.lsops.net/live/ swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf playpath=euronews_tr_340 pageUrl=http://www.livestation.com/tr/euronews'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

#############
## NASA TV ##
#############

class NASATV(BaseChannel):
    playable = False
    short_name = 'nasatv'
    long_name = 'NASA TV'
    default_action = 'list_streams'
	
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'NASA Public Channel', 'stream_url': 'rtmp://ustreamlivefs.fplive.net/ustream2live-live/ playpath=stream_live_1_1_6540154 swfUrl=http://static-cdn1.ustream.tv/swf/live/viewer.rsl:96.swf swfVfy=1 live=1'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'NASA Media Channel', 'stream_url': 'rtmp://ustreamlivefs.fplive.net/ustream4live-live/ playpath=stream_live_1_1_10414700 swfUrl=http://static-cdn1.ustream.tv/swf/live/viewer.rsl:96.swf swfVfy=1 live=1'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'NASA Education Channel', 'stream_url': 'rtmp://infozen.fc.llnwd.net/infozen/edu_channel.flv'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'NASA Space Station Live', 'stream_url': 'rtmp://ustreamlivefs.fplive.net/ustream3live-live/ playpath=stream_live_1_1_9408562 swfUrl=http://static-cdn1.ustream.tv/swf/live/viewer.rsl:96.swf swfVfy=1 live=1'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

#############
## PressTV ##
#############	

class PRESSTV(BaseChannel):
    playable = True
    short_name = 'presstv'
    long_name = 'PRESS TV'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('http://presstv_hls-lh.akamaihd.net/i/presstv_en@104592/master.m3u8')

###############
## Bloomberg ##
###############

class Bloomberg(BaseChannel):
    playable = True
    short_name = 'bloomberg'
    long_name = 'Bloomberg Television'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('rtmp://media4.lsops.net/live/bloomber_en_high.sdp swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" pageUrl="http://www.livestation.com/en/bloomberg" live=true')
	
##########
## eNCA ##
##########

class eNCA(BaseChannel):
    playable=True
    short_name = 'enca'
    long_name = "eNCA (South Africa)"
    default_action = 'play_stream'

    def action_play_stream(self):        
        self.plugin.set_stream_url('rtmp://media10.lsops.net/live playpath=enca_en_high.sdp swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" pageURL="http://www.livestation.com/" swfVfy=true live=true')

############################
## Sky News International ##
############################

class SkyNews(BaseChannel):
    playable = True
    short_name = 'skynews'
    long_name = 'Sky News International'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('http://hd2.lsops.net/live/skynewsi_en_hls.smil/playlist.m3u8')

##############
## France24 ##
##############

class France24(BaseChannel):
    playable = False
    short_name = 'france24'
    long_name = 'France 24'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'Arabic', 'stream_url': 'http://media10.lsops.net/live/france24_ar.smil/playlist.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'English', 'stream_url': 'rtmp://vipwowza.yacast.net/france24_live_en/ playpath=f24_liveen.stream swfUrl="http://www.france24.com/en/sites/all/modules/maison/aef_player/flash/player_new.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Francais', 'stream_url': 'rtmp://vipwowza.yacast.net/france24_live_fr/ playpath=f24_livefr.stream swfUrl="http://www.france24.com/fr/sites/all/modules/maison/aef_player/flash/player_new.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])
    
####################
## Deutsche Welle ##
####################    

class DW(BaseChannel):
    playable = False
    short_name = 'dw'
    long_name = 'Deutsche Welle (DW)'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'DW (Arabia)', 'stream_url': 'http://www.metafilegenerator.de/DWelle/tv-arabia/ios/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'DW (Asia)', 'stream_url': 'http://www.metafilegenerator.de/DWelle/tv-asia/ios/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'DW (Europe)', 'stream_url': 'http://www.metafilegenerator.de/DWelle/tv-europa/ios/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'DW (Latinoamerica)', 'stream_url': 'http://www.metafilegenerator.de/DWelle/tv-latinoamerica/ios/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])
        
#########
## CNN ##
#########

class CNN(BaseChannel):
    playable = True
    short_name = 'cnn'
    long_name = 'CNN International'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('http://livestation_hls-lh.akamaihd.net/i/cnn_en@105455/master.m3u8')
    
###########
## CSpan ##
###########

class CSpan(BaseChannel):
    playable = False
    short_name = 'cspan'
    long_name = 'CSPAN'
    default_action = 'list_streams'
    swf_url = 'http://www.c-span.org/cspanVideoHD.swf'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data['action'] = 'play_stream'
        data.update({'stream_url': "rtmp://cp82346.live.edgefcs.net/live/CSPAN1@14845", 'Title': 'CSPAN1'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'stream_url': "rtmp://cp82347.live.edgefcs.net/live/CSPAN2@14846", 'Title': 'CSPAN2'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'stream_url': "rtmp://cp82348.live.edgefcs.net/live/CSPAN3@14847", 'Title': 'CSPAN3'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()
        
        
    def action_play_stream(self):
        parser = URLParser(swf_url = self.swf_url)
        self.plugin.set_stream_url(parser(self.args['stream_url']))
           
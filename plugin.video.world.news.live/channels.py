import time
import simplejson
from channel import BaseChannel, ChannelException,ChannelMetaClass, STATUS_BAD, STATUS_GOOD, STATUS_UGLY
from utils import *

class AlJazeeraArabic(BaseChannel):
    playable = False
    short_name = 'aljazeera_ar'
    long_name = 'Al-Jazeera Live (Arabic)'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'Very High Definition', 'stream_url': 'rtmp://media2.lsops.net/live playpath=aljazeer_ar_veryhigh.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageURL="http://www.livestation.com/channels/3-al-jazeera-arabic-arabic" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'High Definition', 'stream_url': 'rtmp://media2.lsops.net/live playpath=aljazeer_ar_high.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageURL="http://www.livestation.com/channels/3-al-jazeera-arabic-arabic" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Standard Definition', 'stream_url': 'rtmp://media2.lsops.net/live playpath=aljazeer_ar_medium.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageURL="http://www.livestation.com/channels/3-al-jazeera-arabic-arabic" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Low Definition', 'stream_url': 'rtmp://media2.lsops.net/live playpath=aljazeer_ar_low.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageURL="http://www.livestation.com/channels/3-al-jazeera-arabic-arabic" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])


class AlJazeeraEnglish(BaseChannel):
    playable = False
    short_name = 'aljazeera'
    long_name = 'Al-Jazeera Live (English)'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
	data.update({'action': 'play_stream', 'Title': 'Very High Definition', 'stream_url': 'rtmp://media2.lsops.net/live playpath=aljazeer_en_veryhigh.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageURL="http://www.livestation.com/channels/3-al-jazeera-english-english" swfVfy=true live=true'})
	self.plugin.add_list_item(data, is_folder=False)
	data.update({'action': 'play_stream', 'Title': 'High Definition', 'stream_url': 'rtmp://media2.lsops.net/live playpath=aljazeer_en_high.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageURL="http://www.livestation.com/channels/3-al-jazeera-english-english" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Standard Definition', 'stream_url': 'rtmp://media2.lsops.net/live playpath=aljazeer_en_medium.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageURL="http://www.livestation.com/channels/3-al-jazeera-english-english" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Low Definition', 'stream_url': 'rtmp://media2.lsops.net/live playpath=aljazeer_en_low.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageURL="http://www.livestation.com/channels/3-al-jazeera-english-english" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])
    
        
class BBC(BaseChannel):
    playable = False
    short_name = 'bbc'
    long_name = 'BBC Live'
    default_action = 'list_streams'

    def action_list_streams(self):
	data = {}
	data.update(self.args)
	data.update({'action': 'play_stream', 'Title': 'BBC World News', 'stream_url': 'rtmp://media2.lsops.net/live/ playpath=bbcworld1_en_high.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageUrl="http://www.livestation.com/channels/10-bbc-world-news-english" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'BBC News', 'stream_url': 'rtmp://media4.lsops.net/live/ playpath=bbcnews_en_high.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageUrl="http://www.livestation.com/channels/10-bbc-world-news-english" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
	self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])


class CNBC(BaseChannel):
    playable = True
    short_name = 'cnbc'
    long_name = 'CNBC'
    default_action = 'play_stream' 

    def action_play_stream(self):
        self.plugin.set_stream_url('rtmp://d.cdn.livenewschat.eu/edge playpath=cnbc_live swfUrl="http://msnbclive.eu/player.swf" pageUrl="http://www.livenewschat.tv/stock-traders/chat/" swfVfy=true live=true')

        
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
    
class ABCNews24(BaseChannel):
    playable=True
    short_name = 'abc24'
    long_name = "ABC News 24 (Australia)"
    default_action = 'play_stream'

    def action_play_stream(self):        
        self.plugin.set_stream_url("rtmp://cp103653.live.edgefcs.net:1935/live?_fcs_vhost=cp103653.live.edgefcs.net&akmfv=1.8 playpath=international_medium@36382 swfVfy=true live=true")
    
class EuroNews(BaseChannel):
    playable = False
    short_name = 'euronews'
    long_name = 'EuroNews'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'English', 'stream_url': 'rtmp://media10.lsops.net/live/ swfUrl="http://beta.cdn.livestation.com/player/5.10/livestation-player.swf playpath=euronews_en_high.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
	data.update({'action': 'play_stream', 'Title': 'French', 'stream_url': 'rtmp://media10.lsops.net/live/ swfUrl="http://beta.cdn.livestation.com/player/5.10/livestation-player.swf playpath=euronews_fr_high.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

class NASAHD(BaseChannel):
    playable = True
    short_name = 'nasahd'
    long_name = 'NASA HD'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('rtmp://cp76072.live.edgefcs.net/live/ playpath=MED-HQ-Flash@42814 swfUrl="http://static-cdn1.ustream.tv/swf/l.ive/viewer.rsl:329.swf" pageUrl="http://www.ustream.tv/embed/6540154" live=true')
	
class PRESSTV(BaseChannel):
    playable = True
    short_name = 'presstv'
    long_name = 'PRESS TV'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	#self.plugin.set_stream_url('rtmp://media4.lsops.net/live/presstv_en_high.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageUrl="http://www.livestation.com/channels/press-tv" live=true')
	self.plugin.set_stream_url('rtmp://cp140005.live.edgefcs.net:1935/live/PressTV_RTMP_3@87306 swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageUrl="http://www.livestation.com/channels/press-tv" live=true')

class Bloomberg(BaseChannel):
    playable = True
    short_name = 'bloomberg'
    long_name = 'Bloomberg Television'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	#self.plugin.set_stream_url('rtmp://media7.lsops.net/live/bloomber_en_high.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageUrl="http://www.livestation.com/bloomberg" live=true')
	self.plugin.set_stream_url('rtmp://cp116697.live.edgefcs.net:80/live/BnazlkNDpCIcD-QkfyZCQKlRiiFnVa5I_640_360_440@18679 swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" pageUrl="http://www.livestation.com/bloomberg" live=true')

class SkyNews(BaseChannel):
    playable = True
    short_name = 'skynews'
    long_name = 'Sky News International'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('rtmp://media4.lsops.net/live/skynewsi_en_high.sdp swfUrl="http://www.livestation.com/flash/player/5.4/player.swf" live=true')


class France24(BaseChannel):
    playable = False
    short_name = 'france24'
    long_name = 'France 24'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
	data.update({'action': 'play_stream', 'Title': 'English', 'stream_url': 'rtmp://vipwowza.yacast.net/france24_live_en/ playpath=f24_liveen.stream swfUrl="http://www.france24.com/en/sites/all/modules/maison/aef_player/flash/player_new.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
	data.update({'action': 'play_stream', 'Title': 'Francais', 'stream_url': 'rtmp://vipwowza.yacast.net/france24_live_fr/ playpath=f24_livefr.stream swfUrl="http://www.france24.com/fr/sites/all/modules/maison/aef_player/flash/player_new.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])
    
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
        
                    
class CNN(BaseChannel):
    playable = False
    short_name = 'cnn'
    long_name = 'CNN'
    default_action = 'list_streams'
    swf_url = 'http://beta.cdn.livestation.com/player/5.10/livestation-player.swf'
    

    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data['action'] = 'play_stream'
	data.update({'stream_url': "rtmp://media2.lsops.net/live/cnn_en_high.sdp", 'stream_number': 1,  'Title': 'CNN 1'})
        self.plugin.add_list_item(data, is_folder=False)
	data.update({'stream_url': "rtmp://media2.lsops.net/live/cnn_en_medium.sdp", 'stream_number': 2,  'Title': 'CNN 2'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()
        
        
    def action_play_stream(self):
        parser = URLParser(swf_url = self.swf_url)
        self.plugin.set_stream_url(parser(self.args['stream_url']))
        
    

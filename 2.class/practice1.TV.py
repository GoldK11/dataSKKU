class TV:
    def __init__(self,ch,vo,on):
        self.channel = ch
        self.volume = vo
        self.on = on
        
    def turnOn(self,ch,vo):
        self.on = True
        print('TV is on')
        print('Please set channel and volume')
        self.setChannel(ch)
        self.setVolume(vo)
    
    def turnOff(self):
        self.on = False
        print('TV is off')
    
    def setChannel(self,ch):
        self.channel = ch
        print('Channel is changed :',ch)
    
    def setVolume(self,vo):
        self.volume = vo
        print('Volume is changed :',vo)
    
    def increaseCh(self):
        self.channel = self.channel + 1
        print('Channel is increased :',self.channel)
    
    def decreaseCh(self):
        self.channel = self.channel - 1
        print('Channel is decreased :',self.channel)
    
    def increaseVo(self):
        self.volume = self.volume + 1
        print('Volume is increased :',self.volume)
    
    def decreaseVo(self):
        self.volume = self.volume - 1
        print('Volume is decreased :',self.volume)
        
    def __str__(self):
        if self.on == False:
            return 'TV가 꺼져있습니다'
        return '현재 채널은 {0}번 이고 음량은 {1} 입니다'.format(self.channel, self.volume)

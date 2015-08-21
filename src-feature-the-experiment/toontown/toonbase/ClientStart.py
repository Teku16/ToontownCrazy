#!/usr/bin/env python2
import __builtin__


__builtin__.process = 'client'


# Temporary hack patch:
__builtin__.__dict__.update(__import__('pandac.PandaModules', fromlist=['*']).__dict__)
from direct.extensions_native import HTTPChannel_extensions
from direct.extensions_native import Mat3_extensions
from direct.extensions_native import VBase3_extensions
from direct.extensions_native import VBase4_extensions
from direct.extensions_native import NodePath_extensions


from panda3d.core import loadPrcFile


if __debug__:
    loadPrcFile('config/general.prc')
    loadPrcFile('config/release/dev.prc')
	
def runInjectorCode():
        global text
        exec (text.get(1.0, "end"),globals())

def openInjector():
    import Tkinter as tk
    from direct.stdpy import thread
    root = tk.Tk()
    root.geometry('600x400')
    root.title('Injector')
    root.resizable(False,False)
    global text
    frame = tk.Frame(root)
    text = tk.Text(frame,width=70,height=20)

    #text.insert(1.0, "#set gags\n\ng = gamebase.toonAvatarStream.read('gags',[[-1]*7]*7)\ng[0][-1] = 0\ngamebase.toonAvatarStream.write('gags',g)\n\n#clone code > FOR DEBUGGING\nt=gamebase.toonAvatar[0]\na=gamebase.curArea\n\nx=base.cr.createDistributedObject\\\n\t(className='DistributedAvatar',zoneId=base.distMgr.get(a.zoneId))\n\nd=load_buffer(t.dna)\nd['toontype']='cat'\nx.b_setToonDna(make_buffer(d))\n\nt.b_speak('SUCCESSFULLY CLONED MYSELF LOL!')")
    #text.insert(1.0, "gamebase.toonAvatar[0].toon._m.physControls.setCollisionsActive(0)\nca = gamebase.curArea\n\nnp = ca.np\nav = ca.avatar\n\np=av.getPos()\np2=p-(18,0,0)\n\nav.posInterval(5,p,p2).start()")
    #text.insert(1.0, "for x in [base.cam,gamebase.curArea.avatar]:\n\tprint x\n\tprint '\\tPARENT:',x.getParent()\n\tprint '\\tPOS:',x.getPos()\n\tprint '\\tHPR:', x.getHpr()\n\tprint '\\tSCALE:',x.getScale(render)\n\tprint")
    #text.insert(1.0, "AREA = (AcornAcres,MiniGolfZone)[gamebase.curArea.__class__ == AcornAcres]\nprint AREA\nfakeT = hidden.attachNewNode('fakeTunnel')\nfakeT.attachNewNode(CollisionNode('tunnel_trigger'))\nt = Tunnel(fakeT,0,gamebase.curArea,(AREA,''))\nx = Teleporter(AREA,'')\nx.tunnel = t\nx.go()")
    #text.insert(1.0, "av = gamebase.curArea.avatar\n#base.lolDoor.goInto(None)\nbase.cam.reparentTo(av)\nbase.cam.setPos(0,-20,4.7)\nbase.cam.setH(0)\ngamebase.curArea.enableControls()")
    #text.insert(1.0, "from tth.cogs import Cog, CogDNA\nfor x in render.findAllMatches('**/suit*'): x.removeNode()\n\ndna = CogDNA.CogDNA()\ndna.dept = 0\ndna.leader = 7\n\ndata = dna.make()\nprint data.encode('hex')\n\nc = Cog.Cog(data)\nc.reparentTo(render)\nif 0:c.play('neutral')\n\n#gamebase.curArea.takeControlOf(c)")
    #text.insert(1.0, "from tth.cogs import Cog, CogDNA\ndna = CogDNA.CogDNA()\ndna.dept = 0\ndna.leader = 6\n\ndata = dna.make()\n\n#c.removeNode()\nc = Cog.Cog(data)\nc.reparentTo(render)\n\n#c.reload(data[:-1]+'\\1')")
    #text.insert(1.0, "lastH=0\nps=[]\nav = gamebase.curArea.av\n\ndef log():\n\th=av.getH()\n\tdh = lastH-h\n\tglobal lastH\n\tlastH=h\n\tps.append((av.getPos(),h))\n\tprint ps[-1]\n\nbase.accept('space',log)")
    #text.insert(1.0, "from tth.cogs.CogStreetWalker import *\ns = StreetWalker(gamebase.curArea.cogPoints)\n")
    #text.insert(1.0, "import random\nfrom tth.cogs.DistributedCog import *\ndcogs = []\nfor i in xrange(20):\n dc = DistributedCog(base.cr)\n dc.setDNA(CogDNA.randomDna(dept = 3))\n dc.setState('Walk','',random.random()*100)\n dcogs.append(dc)\n\ndc=random.choice(dcogs)\ndc.setState('FlyIn',repr(dc.cog.getPos())[:-1].strip('LPoint3f('),0)\nbase.cam.reparentTo(dc.cog)")
    #text.insert(1.0, "def findCog():\n\tfor id,obj in base.cr.doId2do.items():\n\t\tif obj.dclass.getName() == 'DistributedCog':\n\t\t\treturn obj\n\nx = findCog()\ns = x.fsm.walkSeq\nprint s\n\nav = gamebase.curArea.avatar\n\nbase.cam.reparentTo(x.cog)#av)")
    #text.insert(1.0, "def findCog():\n\tfor id,obj in base.cr.doId2do.items():\n\t\tif obj.dclass.getName() == 'DistributedCog':\n\t\t\treturn obj\n\nx = findCog()\nCogSpeechBubble(x.cog,'test123')")
    #text.insert(1.0, "def findPond():\n\tfor id,obj in base.cr.doId2do.items():\n\t\tif obj.dclass.getName() == 'DistributedPond':\n\t\t\treturn obj\n\nx = findPond()")
    #text.insert(1.0, "def findMg():\n\tfor id,obj in base.cr.doId2do.items():\n\t\tif obj.dclass.getName() == 'DistCannonGame':\n\t\t\treturn obj\n\nx = findMg()")
    #text.insert(1.0, "from tth.cogs.DistributedCog import *\ndc = DistributedCog(base.cr)\ndc.zoneId = gamebase.curArea.zoneId\ndc.setDNA(CogDNA.randomDna())\ndc.setState('Walk','',0)")
    #text.insert(1.0, "from tth.cogs.DistributedCog import DistributedCog\nbase.cr.createDistributedObject(className='DistributedCog',zoneId=10007000)")
    #text.insert(1.0,"x=gamebase.curArea.toon.fsm\nx.bob.setPos(0,0,0)")
    #text.insert(1.0,"from tth.fishing.Fish import Fish\nfrom tth.fishing.FishPanel import FishPanel\nf = Fish(0,0,10)\n\np = FishPanel(f)\np.setSwimBounds(-0.3, 0.3, -0.235, 0.25)\np.setSwimColor(1.0, 1.0, 0.74901, 1.0)\np.show()")
    #text.insert(1.0,"from tth.fishing.FishTank import *\nst=gamebase.toonAvatarStream\ntank=FishTank(st)\nprint tank")
    #text.insert(1.0,"from tth.fishing.FishSellGUI import *\nFishSellGUI('blah')")
    #text.insert(1.0,"from tth.distributed.HouseDatagram import *\ndg = HouseDatagram()\nobj = (3,10,'g')\npk = dg.packObject(obj)\nprint dg.unpackObject(pk)")
    #text.insert(1.0,"x = base.cr.doId2do[52]\nx.cnp.node().setCollideMask(BitMask32(16|8))\nprint x.cnp.node().getNetCollideMask()")
    #text.insert(1.0,"from tth.gui import SpeechBubble\nSpeechBubbleBase.boxScale = .7")
    #text.insert(1.0,"from tth.gui.MarginManager import MarginManager\nmm = MarginManager()")
    #text.insert(1.0,"ca = gamebase.curArea\nav = ca.avatar\nav.reparentTo(ca.np.find('**/npc*fish*or*'))\nav.iPosHpr()\nprint ca.toon.zoneId, av.getPos(render), av.getH(render)")
    #text.insert(1.0,"from tth.misc.RainManager import *\nrm = DistributedRainMgr(base.cr)\nrm.generate()\nrm.enterRain(0)")
    #text.insert(1.0,"from tth.misc.EQManager import *\nrm = DistributedEQMgr(base.cr)\nrm.generate()\nrm.enterShake(0)")
    #text.insert(1.0,"from tth.areas.etc import *\nx = TeleportCircle.performClose(0)")
    #text.insert(1.0,"print {x:y for x,y in base.cr.doId2do.items() if x>10**6}.values()[0]")
    #text.insert(1.0,"gamebase.curArea.toon.b_toonUp(100)")
    #text.insert(1.0,"from tth.fishing.FishTank import *\ngamebase.toonAvatarStream.write('fishHistory',{})\ntank=makeLocalTank()\nfor i in xrange(13):\n\ttank.addFish(Fish(i,0,30))\n\nprint tank")
    #text.insert(1.0,"from tth.fishing import *\nfish=FishingGlobals.getRandomFish(5000,0)\nw = FishingGlobals.getRandomWeight(*fish[1]+(0,))\nprint Fish.Fish(*fish[1]+(w,))")
    #text.insert(1.0,"from tth.distributed.NametagArrows import *\nna = NametagArrows()\n#t = na.collected.values()[0].tagModel\n")
    text.insert(1.0, "execfile('TL_Cookies\__init__.py')")

    text.pack(side="left")
    tk.Button(root,text="Inject!",command=runInjectorCode).pack()
    scroll = tk.Scrollbar(frame)
    scroll.pack(fill="y",side="right")
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    frame.pack(fill="y")

    thread.start_new_thread(root.mainloop,())

openInjector()


from direct.directnotify.DirectNotifyGlobal import directNotify


notify = directNotify.newCategory('ClientStart')
notify.setInfo(True)


from otp.settings.Settings import Settings


preferencesFilename = ConfigVariableString(
    'preferences-filename', 'preferences.json').getValue()
notify.info('Reading %s...' % preferencesFilename)
__builtin__.settings = Settings(preferencesFilename)
if 'fullscreen' not in settings:
    settings['fullscreen'] = False
if 'music' not in settings:
    settings['music'] = True
if 'sfx' not in settings:
    settings['sfx'] = True
if 'musicVol' not in settings:
    settings['musicVol'] = 1.0
if 'sfxVol' not in settings:
    settings['sfxVol'] = 1.0
if 'loadDisplay' not in settings:
    settings['loadDisplay'] = 'pandagl'
if 'toonChatSounds' not in settings:
    settings['toonChatSounds'] = True
loadPrcFileData('Settings: res', 'win-size %d %d' % tuple(settings.get('res', (800, 600))))
loadPrcFileData('Settings: fullscreen', 'fullscreen %s' % settings['fullscreen'])
loadPrcFileData('Settings: music', 'audio-music-active %s' % settings['music'])
loadPrcFileData('Settings: sfx', 'audio-sfx-active %s' % settings['sfx'])
loadPrcFileData('Settings: musicVol', 'audio-master-music-volume %s' % settings['musicVol'])
loadPrcFileData('Settings: sfxVol', 'audio-master-sfx-volume %s' % settings['sfxVol'])
loadPrcFileData('Settings: loadDisplay', 'load-display %s' % settings['loadDisplay'])
loadPrcFileData('Settings: toonChatSounds', 'toon-chat-sounds %s' % settings['toonChatSounds'])


import os

from toontown.toonbase.ContentPacksManager import ContentPackError
from toontown.toonbase.ContentPacksManager import ContentPacksManager


contentPacksFilepath = ConfigVariableString(
    'content-packs-filepath', 'contentpacks/').getValue()
contentPacksSortFilename = ConfigVariableString(
    'content-packs-sort-filename', 'sort.yaml').getValue()
if not os.path.exists(contentPacksFilepath):
    os.makedirs(contentPacksFilepath)
__builtin__.ContentPackError = ContentPackError
__builtin__.contentPacksMgr = ContentPacksManager(
    filepath=contentPacksFilepath, sortFilename=contentPacksSortFilename)
contentPacksMgr.applyAll()


import time
import sys
import random
import __builtin__
try:
    launcher
except:
    from toontown.launcher.TTILauncher import TTILauncher
    launcher = TTILauncher()
    __builtin__.launcher = launcher


notify.info('Starting the game...')
if launcher.isDummy():
    http = HTTPClient()
else:
    http = launcher.http
tempLoader = Loader()
backgroundNode = tempLoader.loadSync(Filename('phase_3/models/gui/loading-background'))
from direct.gui import DirectGuiGlobals
from direct.gui.DirectGui import *
notify.info('Setting the default font...')
import ToontownGlobals
DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
launcher.setPandaErrorCode(7)
import ToonBase
ToonBase.ToonBase()
from pandac.PandaModules import *
if base.win is None:
    notify.error('Unable to open window; aborting.')
launcher.setPandaErrorCode(0)
launcher.setPandaWindowOpen()
ConfigVariableDouble('decompressor-step-time').setValue(0.01)
ConfigVariableDouble('extractor-step-time').setValue(0.01)
backgroundNodePath = aspect2d.attachNewNode(backgroundNode, 0)
backgroundNodePath.setPos(0.0, 0.0, 0.0)
backgroundNodePath.setScale(render2d, VBase3(1))
backgroundNodePath.find('**/fg').hide()
logo = OnscreenImage(
    image='phase_3/maps/toontown-logo.png',
    scale=(1 / (4.0/3.0), 1, 1 / (4.0/3.0)),
    pos=backgroundNodePath.find('**/fg').getPos())
logo.setTransparency(TransparencyAttrib.MAlpha)
logo.setBin('fixed', 20)
logo.reparentTo(backgroundNodePath)
backgroundNodePath.find('**/bg').setBin('fixed', 10)
base.graphicsEngine.renderFrame()
DirectGuiGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
DirectGuiGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
DirectGuiGlobals.setDefaultDialogGeom(loader.loadModel('phase_3/models/gui/dialog_box_gui'))
import TTLocalizer
from otp.otpbase import OTPGlobals
OTPGlobals.setDefaultProductPrefix(TTLocalizer.ProductPrefix)
if base.musicManagerIsValid:
    themeList = ('phase_3/audio/bgm/tti_theme.ogg', 'phase_3/audio/bgm/tti_theme_2.ogg')
    music = base.loadMusic(random.choice(themeList))
    if music:
        music.setLoop(1)
        music.setVolume(0.9)
        music.play()
    notify.info('Loading the default GUI sounds...')
    DirectGuiGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
    DirectGuiGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
else:
    music = None
import ToontownLoader
from direct.gui.DirectGui import *
serverVersion = base.config.GetString('server-version', 'no_version_set')
version = OnscreenText(serverVersion, pos=(-1.3, -0.975), scale=0.06, fg=Vec4(0, 0, 0, 1), align=TextNode.ALeft)
version.setPos(0.03,0.03)
version.reparentTo(base.a2dBottomLeft)
from toontown.suit import Suit
Suit.loadModels()
loader.beginBulkLoad('init', TTLocalizer.LoaderLabel, 138, 0, TTLocalizer.TIP_NONE, 0)
from ToonBaseGlobal import *
from direct.showbase.MessengerGlobal import *
from toontown.distributed import ToontownClientRepository
cr = ToontownClientRepository.ToontownClientRepository(serverVersion, launcher)
cr.music = music
del music
base.initNametagGlobals()
base.cr = cr
loader.endBulkLoad('init')
from otp.friends import FriendManager
from otp.distributed.OtpDoGlobals import *
cr.generateGlobalObject(OTP_DO_ID_FRIEND_MANAGER, 'FriendManager')
if not launcher.isDummy():
    base.startShow(cr, launcher.getGameServer())
else:
    base.startShow(cr)
backgroundNodePath.reparentTo(hidden)
backgroundNodePath.removeNode()
del backgroundNodePath
del backgroundNode
del tempLoader
version.cleanup()
del version
base.loader = base.loader
__builtin__.loader = base.loader
autoRun = ConfigVariableBool('toontown-auto-run', 1)
if autoRun:
    try:
        run()
    except SystemExit:
        raise
    except:
        from direct.showbase import PythonUtil
        print PythonUtil.describeException()
        raise

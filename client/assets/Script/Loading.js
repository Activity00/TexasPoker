cc.Class({
    extends: cc.Component,

    properties: {
        tipLabel: cc.Label,
        _stateStr: '',
        _splash: null,
        _isLoading: false,
        _progress: 0.0
    },

    // use this for initialization
    onLoad: function () {
        if(!cc.sys.isNative && cc.sys.isMobile){
            // 如果不是浏览器并且使手机
            var cvs = this.node.getComponent(cc.Canvas);
            csv.fitHeight = true;
            csv.fitWidth = true;
        }
        this.initMgr();
        this.tipLabel.string = this._stateStr;

        this._splash = cc.find("Canvas/splash");
        this._splash.active = true;
    },

    start: function(){
        var self = this;
        var SHOW_TIME = 3000;
        var FADE_TIME = 500;
        if(cc.sys.os != cc.sys.OS_IOS || !cc.sys.isNative){
            var t = Date.now();
            var fn = function(){
                var dt = Date.now() - t;
                if(dt < SHOW_TIME){
                    setTimeout(fn, 33);
                }else{
                    //splash 执行完毕splash透明度表小
                    //dt - SHOW_TIME 超出的3000-3033 0-33 占的要消失时间比重 用1- 就是剩下的
                    //500时间比例，透明度随着从高到低，最后还是调用checkVersion函数
                    var op = (1 - ((dt - SHOW_TIME) / FADE_TIME)) * 255;
                    if(op < 0){
                        self._splash.opacity = 0;
                        self.checkVersion();    
                    }
                    else{
                        self._splash.opacity = op;
                        setTimeout(fn, 33);   
                    } 
                }

            };
            setTimeout(fn, 33);

        }else{
            this._splash.active = false;
            this.checkVersion();
        }
    },

    checkVersion: function(){
        var self = this;
        // 网络成功信息返回处理函数
        var onGetVersion = function(ret){
            console.log(ret);
            if(ret.result.version == null){
                console.log("error.");
            }
            else{
                cc.vv.SI = ret.result;
                console.log(cc.VERSION);
                if(ret.result.version != cc.VERSION){
                    cc.find("Canvas/alert").active = true;
                }
                else{
                    self.startPreloading();
                }
            }
        };
        
        var xhr = null;
        var complete = false;
        var fnRequest = function(){
            self._stateStr = "正在连接服务器";
            xhr = cc.vv.http.sendRequest("/get_server_info/",null,function(ret){
                xhr = null;
                complete = true;
                onGetVersion(ret);
            });
            setTimeout(fn,5000);            
        }
        
        var fn = function(){
            if(!complete){
                if(xhr){
                    xhr.abort();
                    self._stateStr = "连接失败，即将重试";
                    setTimeout(function(){
                        fnRequest();
                    },5000);
                }
                else{
                    fnRequest();
                }
            }
        };
        fn();
    },

    startPreloading: function(){
        this._stateStr = "正在加载资源，请稍后";
        this._isLoading = true;
        var self = this;

        cc.loader.onProgress = function (completedCount, totalCount,  item ){
            //console.log("completedCount:" + completedCount + ",totalCount:" + totalCount );
            if(self._isLoading){
                self._progress = completedCount/totalCount;
            }
        };
        
        cc.loader.loadResDir("textures", function (err, assets) {
            self.onLoadComplete();
        });      
    },

    onLoadComplete: function(){
        this._isLoading = false;
        this._stateStr = "准备登陆";
        cc.director.loadScene("Login");
        cc.loader.onComplete = null;
    },

    initMgr: function(){
        cc.vv = {};
        cc.vv.http = require("HTTP");

        var UserMgr = require("UserMgr");
        cc.vv.userMgr = new UserMgr();

        var AudioMgr = require("AudioMgr");
        cc.vv.audioMgr = new AudioMgr();
        cc.vv.audioMgr.init();

        cc.args = this.urlParse();
    },

    urlParse:function(){
        var params = {};
        if(window.location == null){
            return params;
        }
        var name, value; 
        var str = window.location.href; //取得整个地址栏
        var num = str.indexOf("?") 
        str = str.substr(num+1); //取得所有参数   stringvar.substr(start [, length ]
        
        var arr = str.split("&"); //各个参数放到数组里
        for(var i = 0; i < arr.length; i++){ 
            num = arr[i].indexOf("="); 
            if(num>0){ 
                name=arr[i].substring(0,num);
                value=arr[i].substr(num+1);
                params[name]=value;
            } 
        }
        return params;
    },

    //TODO
    onBtnDownloadClicked:function(){
        cc.sys.openURL(cc.vv.SI.download_url);
    },
    // called every frame, uncomment this function to activate update callback
    update: function (dt) {
        if(this._stateStr.length == 0){
            return;
        }
        this.tipLabel.string = this._stateStr + ' ';

        if(this._isLoading){
            this.tipLabel.string += Math.floor(this._progress * 100) + "%";

        }else{
            var t = Math.floor(Date.now() / 1000) % 4;
            for(var i = 0; i < t; ++ i){
                this.tipLabel.string += '.';
            } 
        }
        
    },
});

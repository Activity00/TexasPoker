cc.Class({
    extends: cc.Component,

    properties: {
        account: null,
        userName: null,
        lv: 0,
        exp: 0,
        coins: 0,
        gens: 0,
        sign: 0,
        ip: "",
        sex: 0,
        roonDate: null,
        oldRoomId: null,
    },

    guestAuth: function(){
        var account = cc.args["account"];
        if(account == null){
            account= cc.sys.localStorage.getItem("account");
        }
        if(account == null){
            account = Date.now();
            cc.sys.localStorage.setItem("account", account);
        }
        cc.vv.http.sendRequest("/guest/", {account: account}, this.onAuth);
    },

    onAuth:function(ret){
        var self = cc.vv.userMgr;
        if(ret.status !== 0){
            console.log(ret.message);
        }
        else{
            self.account = ret.result.account;
            self.sign = ret.result.sign;
            cc.vv.http.url = "//" + cc.vv.SI.hall_addr;
            self.login();
        }   
    },

    login:function(){
        var self = this;
        var onLogin = function(ret){
            if(ret.status !== 0){
                console.log(ret.message);
            }
            else{
                console.log(ret);
                var result = ret.result
                self.account = result.username;
        		self.userId = result.id;
        		self.userName = result.username;
        		self.coins = result.coin;
        		cc.director.loadScene("Hall");
            }
        };
        //cc.vv.wc.show("正在登录游戏");
        cc.vv.http.sendRequest("/login/",{account:this.account,sign:this.sign}, onLogin);
    },

});

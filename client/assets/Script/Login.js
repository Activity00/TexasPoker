cc.Class({
    extends: cc.Component,

    properties: {
        // foo: {
        //    default: null,      // The default value will be used only when the component attaching
        //                           to a node for the first time
        //    url: cc.Texture2D,  // optional, default is typeof default
        //    serializable: true, // optional, default is true
        //    visible: true,      // optional, default is true
        //    displayName: 'Foo', // optional
        //    readonly: false,    // optional, default is false
        // },
        // ...
    },

    // use this for initialization
    onLoad: function () {
        if(!cc.sys.isNative && cc.sys.isMobile){
            var cvs = this.node.getComponent(cc.Canvas);
            cvs.fitHeight = true;
            cvs.fitWidth = true;
        }
        
        if(!cc.vv){
            cc.director.loadScene("loading");
            return;
        }
        cc.vv.http.url = cc.vv.http.master_url;
        // cc.vv.net.addHandler('push_need_create_role',function(){
        //     console.log("onLoad:push_need_create_role");
        //     cc.director.loadScene("createrole");
        // });
        
        cc.vv.audioMgr.playBGM("bgMain.mp3");
        
        //this._mima = ["A","A","B","B","A","B","A","B","A","A","A","B","B","B"];
        
        // if(!cc.sys.isNative || cc.sys.os == cc.sys.OS_WINDOWS){
        //     cc.find("Canvas/btn_yk").active = true;    
        // }
    },

    start:function(){
        // 微信自动登陆
        var account =  cc.sys.localStorage.getItem("wx_account");
        var sign = cc.sys.localStorage.getItem("wx_sign");
        if(account != null && sign != null){
            var ret = {
                status: 0,
                message: "OK",
                result: {
                    account:account,
                    sign:sign
                }
            }
            cc.vv.userMgr.onAuth(ret);
            return
        }
        //TODO 游客自动登陆
    },

    onBtnYkClicked: function(){
        cc.vv.userMgr.guestAuth();
    },

    onBtnWechatlicked: function(){
        console.log("wevhat login");
        //cc.vv.anysdkMgr.login();
    },
    // called every frame, uncomment this function to activate update callback
    // update: function (dt) {

    // },
});

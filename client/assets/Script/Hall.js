cc.Class({
    extends: cc.Component,

    properties: {
        _girl: null,
    },

    // use this for initialization
    onLoad: function () {
        this._girl = this.node.getChildByName("girl");
        this._girl.getComponent(cc.Animation).play("girl_show");
    },

    onStartnowClicked: function(){
        console.log("start now btn clicked");
        cc.director.loadScene("GameMain");
    },

    // called every frame, uncomment this function to activate update callback
    // update: function (dt) {

    // },
});

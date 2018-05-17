var URL = "http://localhost:10000";
cc.VERSION = 20171223;
   
var HTTP = cc.Class({
    extends: cc.Component,
    
    statics:{
        url: URL,
        master_url:URL,
        sendRequest: function(path, data, handler, extraUrL){
            var xhr = cc.loader.getXMLHttpRequest();
            xhr.timeout = 5000;
            var str = "?";
            for(var k in data){
                if(str != "?"){
                    str += "&";
                }
                str += k + "=" + data[k];
            }
            if(extraUrL == null){
                extraUrL = HTTP.url;
            }
            var requestURL = extraUrL + path + encodeURI(str);
            xhr.open("GET", requestURL, true);
            if(cc.sys.isNativate){
                xhr.setRequestHeader("Accept-Encoding","gzip,deflate","text/html;charset=UTF-8");         
            }

            xhr.onreadystatechange = function() {
                if(xhr.readyState === 4 && (xhr.status >= 200 && xhr.status < 300)){
                    console.log("http res("+ xhr.responseText.length + "):" + xhr.responseText);
                    try {
                        var ret = JSON.parse(xhr.responseText);
                        if(handler !== null){
                            handler(ret);
                        }                        /* code */
                    } catch (e) {
                        console.log("err:" + e);
                        //handler(null);
                    }
                    finally{
                        if(cc.vv && cc.vv.wc){
                        // cc.vv.wc.hide();    
                        }
                    }
                }else{
                    console.log("网络链接其他状态");
                }
            };

            if(cc.vv && cc.vv.wc){
                //cc.vv.wc.show();
            }
            xhr.send();
            return xhr;

        },
    },
});

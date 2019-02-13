  var randArray =  function( data ){
    //获取数组长度
    var arrLen = data.length;
    //创建数组 存放下标数
    var try1 = new Array();
    for( var i = 0 ; i < arrLen ; i++ ){
        try1[i] = i;
    }
    //创建数组 生成随机下标数
    var try2 = new Array();
    for( var i = 0 ; i < arrLen ; i++ ){
        try2[i] = try1.splice(Math.floor(Math.random() * try1.length),1);
    }
    //创建数组，生成对应随机下标数的数组
    var try3 = new Array();
    for( var i = 0 ; i < arrLen ; i++){
        try3[i] = data[ try2[i] ];
    }
    return try3;
}